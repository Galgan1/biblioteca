/**
 * auth.js — autenticação multiusuário com papéis para o serviço pdf-service.
 *
 * Factory: makeAuth(secret) → { router, requireAuth, requireAdmin }
 *   - secret: a mesma chave HMAC (hex) que o host já usa (ver server.js ~linha 46).
 *
 * Sessão = cookie httpOnly assinado `mr_sess`:
 *   base64url(JSON {u,r,exp}) + "." + HMAC-SHA256(secret, payload) hex
 * Mesmo padrão de assinatura do server.js (signToken/checkToken ~linha 55).
 *
 * Store = users.json (array de {username, salt, hash, role, createdAt}).
 * Senhas via crypto.scryptSync (salt 16 bytes hex; hash hex). Comparação
 * constante via crypto.timingSafeEqual. Sem dependências externas — só
 * built-ins (crypto, fs). Cookies são lidos à mão de req.headers.cookie.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const express = require('express');

const USERS_FILE = path.join(__dirname, 'users.json');
const COOKIE = 'mr_sess';
const SESSION_TTL_MS = 1000 * 60 * 60 * 24 * 7; // 7 dias
const SCRYPT_KEYLEN = 64; // bytes → 128 hex chars
const ROLES = new Set(['admin', 'user']);

// throttle de login por IP — janela deslizante simples em memória
const THROTTLE_MAX = 10;
const THROTTLE_WINDOW_MS = 1000 * 60 * 5; // 5 min
const attempts = new Map(); // ip → [timestamps]

function tooManyAttempts(ip) {
  const now = Date.now();
  const list = (attempts.get(ip) || []).filter((t) => now - t < THROTTLE_WINDOW_MS);
  attempts.set(ip, list);
  return list.length >= THROTTLE_MAX;
}
function noteAttempt(ip) {
  const list = attempts.get(ip) || [];
  list.push(Date.now());
  attempts.set(ip, list);
}

// ------------------------------------------------------------- store em disco
function loadUsers() {
  try {
    const arr = JSON.parse(fs.readFileSync(USERS_FILE, 'utf8'));
    return Array.isArray(arr) ? arr : [];
  } catch {
    return [];
  }
}
function saveUsers(users) {
  fs.writeFileSync(USERS_FILE, JSON.stringify(users, null, 2), { mode: 0o600 });
}

// ------------------------------------------------------------- senhas (scrypt)
function hashPassword(password, salt) {
  const s = salt || crypto.randomBytes(16).toString('hex');
  const hash = crypto.scryptSync(String(password), s, SCRYPT_KEYLEN).toString('hex');
  return { salt: s, hash };
}
function verifyPassword(password, salt, expectedHex) {
  const { hash } = hashPassword(password, salt);
  const a = Buffer.from(hash, 'hex');
  const b = Buffer.from(expectedHex, 'hex');
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

module.exports = function makeAuth(secret) {
  if (!secret) throw new Error('makeAuth: secret HMAC é obrigatório');

  // ----------------------------------------------------------- sessão (HMAC)
  function signSession(payloadB64) {
    return crypto.createHmac('sha256', secret).update(payloadB64).digest('hex');
  }
  function makeSession(username, role) {
    const exp = Date.now() + SESSION_TTL_MS;
    const payload = Buffer.from(JSON.stringify({ u: username, r: role, exp }))
      .toString('base64url');
    return `${payload}.${signSession(payload)}`;
  }
  function readSession(token) {
    if (!token) return null;
    const i = String(token).lastIndexOf('.');
    if (i <= 0) return null;
    const payload = token.slice(0, i);
    const sig = token.slice(i + 1);
    const good = signSession(payload);
    if (sig.length !== good.length) return null;
    if (!crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(good))) return null;
    let data;
    try {
      data = JSON.parse(Buffer.from(payload, 'base64url').toString('utf8'));
    } catch {
      return null;
    }
    if (!data || typeof data.exp !== 'number' || data.exp < Date.now()) return null;
    return { username: data.u, role: data.r };
  }

  // ----------------------------------------------------------- cookies à mão
  function parseCookies(req) {
    const out = {};
    const raw = req.headers.cookie;
    if (!raw) return out;
    for (const part of raw.split(';')) {
      const eq = part.indexOf('=');
      if (eq < 0) continue;
      const k = part.slice(0, eq).trim();
      if (k) out[k] = decodeURIComponent(part.slice(eq + 1).trim());
    }
    return out;
  }
  function setSessionCookie(res, token) {
    res.setHeader('Set-Cookie',
      `${COOKIE}=${encodeURIComponent(token)}; HttpOnly; SameSite=Lax; Path=/; Max-Age=${Math.floor(SESSION_TTL_MS / 1000)}`);
  }
  function clearSessionCookie(res) {
    res.setHeader('Set-Cookie', `${COOKIE}=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0`);
  }
  function sessionFromReq(req) {
    return readSession(parseCookies(req)[COOKIE]);
  }

  // ----------------------------------------------------------- middlewares
  function requireAuth(req, res, next) {
    const sess = sessionFromReq(req);
    if (!sess) return res.status(401).json({ error: 'não autenticado' });
    req.user = { username: sess.username, role: sess.role };
    next();
  }
  function requireAdmin(req, res, next) {
    const sess = sessionFromReq(req);
    if (!sess) return res.status(401).json({ error: 'não autenticado' });
    if (sess.role !== 'admin') return res.status(403).json({ error: 'acesso restrito' });
    req.user = { username: sess.username, role: sess.role };
    next();
  }

  // ----------------------------------------------------------- seed do admin
  // Só na carga: se o store estiver vazio E houver ADMIN_USER/ADMIN_PASSWORD,
  // cria o admin inicial. Nunca há senha hardcoded.
  (function seedAdmin() {
    const users = loadUsers();
    if (users.length > 0) return;
    const u = process.env.ADMIN_USER;
    const p = process.env.ADMIN_PASSWORD;
    if (!u || !p) return;
    const { salt, hash } = hashPassword(p);
    saveUsers([{ username: u, salt, hash, role: 'admin', createdAt: new Date().toISOString() }]);
  })();

  // ----------------------------------------------------------- rotas
  const router = express.Router();

  router.post('/auth/login', (req, res) => {
    const ip = req.ip || req.socket.remoteAddress || 'unknown';
    if (tooManyAttempts(ip)) return res.status(429).json({ error: 'muitas tentativas' });
    const { username, password } = req.body || {};
    const user = loadUsers().find((x) => x.username === username);
    if (!user || !verifyPassword(String(password || ''), user.salt, user.hash)) {
      noteAttempt(ip);
      return res.status(401).json({ error: 'credenciais inválidas' });
    }
    setSessionCookie(res, makeSession(user.username, user.role));
    res.json({ user: user.username, role: user.role });
  });

  router.post('/auth/logout', (_req, res) => {
    clearSessionCookie(res);
    res.status(200).json({ ok: true });
  });

  router.get('/auth/me', (req, res) => {
    const sess = sessionFromReq(req);
    if (!sess) return res.status(401).json({ error: 'não autenticado' });
    res.json({ user: sess.username, role: sess.role });
  });

  router.post('/admin/users', requireAdmin, (req, res) => {
    const { username, password, role } = req.body || {};
    if (!username || !password || !ROLES.has(role)) {
      return res.status(400).json({ error: 'username, password e role (admin|user) obrigatórios' });
    }
    const users = loadUsers();
    if (users.some((x) => x.username === username)) {
      return res.status(409).json({ error: 'usuário já existe' });
    }
    const { salt, hash } = hashPassword(String(password));
    users.push({ username, salt, hash, role, createdAt: new Date().toISOString() });
    saveUsers(users);
    res.status(201).json({ user: username, role });
  });

  return { router, requireAuth, requireAdmin };
};

// expostos para teste/uso interno (não fazem parte do contrato da factory)
module.exports._hashPassword = hashPassword;
module.exports._verifyPassword = verifyPassword;
