/**
 * upload.js — router de upload de livros pelo admin (a montar no server.js).
 *
 * Factory: makeUpload(requireAdmin) → express.Router()
 *   - requireAdmin: o middleware de papel-admin já exportado por makeAuth (auth.js).
 *
 * Rotas (todas sob requireAdmin):
 *   POST /admin/upload              → multipart, 1 arquivo `book` (+ slug opcional)
 *   GET  /admin/upload/:job/status  → estado do job (lê job.json do disco)
 *
 * Cada upload cria uma pasta de job em UPLOAD_DIR/<jobId>/ com:
 *   - source.<ext>  → o arquivo enviado
 *   - job.json      → { jobId, slug, file, ext, status, createdAt }
 *
 * `multer` é exigido em tempo de execução (lazy, dentro da factory) para que
 * o simples `require('./upload')` não quebre quando a dependência ainda não
 * estiver instalada (ex.: no teste unitário).
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { spawn } = require('child_process');
const express = require('express');

// pasta-raiz onde os jobs de upload são gravados (sobrescrevível por env)
const UPLOAD_DIR = process.env.UPLOAD_DIR || '/opt/biblioteca-pdf/uploads';
const MAX_BYTES = 30 * 1024 * 1024; // 30 MB

// portão humano: build env (staging) → site ao vivo, p/ o publish_to_live.py
const BUILD_DIR = process.env.BUILD_DIR || '/opt/biblioteca-build';
const LIVE_DIR = process.env.LIVE_DIR || '/var/www/andregalgani/biblioteca';
const SITE_URL = process.env.SITE_URL || 'https://www.andregalgani.com.br/biblioteca';

// extensões aceitas (espelha o que o book-to-skill consegue ingerir)
const ALLOWED_EXT = new Set(['.pdf', '.epub', '.txt', '.docx', '.md', '.html', '.rtf']);

// slug em kebab-case, 2–60 chars (mais restrito que o SLUG_RE do server.js)
const SLUG_RE = /^[a-z0-9-]{2,60}$/;
// id de job seguro contra path traversal (sem ponto, sem barra)
const JOB_RE = /^[0-9a-z-]+$/;

// id de job único e ordenável por tempo: <timestamp>-<aleatório>
function newJobId() {
  return `${Date.now()}-${crypto.randomBytes(4).toString('hex')}`;
}

module.exports = function makeUpload(requireAdmin) {
  if (typeof requireAdmin !== 'function') {
    throw new Error('makeUpload: requireAdmin (middleware) é obrigatório');
  }

  // require tardio: só toca em `multer` quando a factory roda de fato
  const multer = require('multer');

  // grava o arquivo direto na pasta do job, como source.<ext>
  const storage = multer.diskStorage({
    destination(req, _file, cb) {
      const jobId = newJobId();
      const dir = path.join(UPLOAD_DIR, jobId);
      fs.mkdir(dir, { recursive: true }, (err) => {
        if (err) return cb(err);
        req._jobId = jobId; // repassa o id ao handler
        req._jobDir = dir;
        cb(null, dir);
      });
    },
    filename(_req, file, cb) {
      const ext = path.extname(file.originalname).toLowerCase();
      cb(null, `source${ext}`);
    },
  });

  // só aceita as extensões da lista — rejeita o resto antes de gravar
  function fileFilter(_req, file, cb) {
    const ext = path.extname(file.originalname).toLowerCase();
    if (!ALLOWED_EXT.has(ext)) {
      return cb(new Error(`extensão não suportada: ${ext || '(sem extensão)'}`));
    }
    cb(null, true);
  }

  const upload = multer({ storage, fileFilter, limits: { fileSize: MAX_BYTES } });

  const router = express.Router();

  // ----------------------------------------------------------- POST upload
  // requireAdmin → multer (campo único `book`) → handler. Erros do multer
  // (limite/filtro) caem no errorHandler ao final via `next(err)`.
  router.post('/admin/upload', requireAdmin, (req, res, next) => {
    upload.single('book')(req, res, (err) => {
      if (err) return next(err);
      if (!req.file) return res.status(400).json({ error: 'arquivo `book` ausente' });

      // slug opcional: se vier, precisa ser kebab-case válido
      const slug = req.body && req.body.slug ? String(req.body.slug) : '';
      if (slug && !SLUG_RE.test(slug)) {
        return res.status(400).json({ error: 'slug inválido (use kebab-case, 2–60 chars)' });
      }

      const ext = path.extname(req.file.filename).toLowerCase();
      const job = {
        jobId: req._jobId,
        slug: slug || null,
        file: req.file.filename,
        ext,
        status: 'queued',
        createdAt: new Date().toISOString(),
      };
      try {
        fs.writeFileSync(path.join(req._jobDir, 'job.json'), JSON.stringify(job, null, 2));
      } catch (e) {
        return next(e);
      }
      res.status(201).json({ jobId: job.jobId, status: job.status });
    });
  });

  // ----------------------------------------------------------- GET status
  router.get('/admin/upload/:job/status', requireAdmin, (req, res) => {
    const job = String(req.params.job);
    if (!JOB_RE.test(job)) return res.status(400).json({ error: 'job inválido' });
    let data;
    try {
      data = JSON.parse(fs.readFileSync(path.join(UPLOAD_DIR, job, 'job.json'), 'utf8'));
    } catch {
      return res.status(404).json({ error: 'job não encontrado' });
    }
    res.json({ status: data.status, stage: data.stage, slug: data.slug,
      error: data.error, url: data.url, summary: data.summary });
  });

  // ------------------------------------------------- POST publish (PORTÃO HUMANO)
  // Só publica jobs em 'ready' (já construídos no staging). Copia o livro do
  // build env → site ao vivo via publish_to_live.py. O deploy roda AQUI (Node),
  // FORA do agente — a fronteira de segurança do Akita (pilar 8).
  router.post('/admin/upload/:job/publish', requireAdmin, (req, res) => {
    const job = String(req.params.job);
    if (!JOB_RE.test(job)) return res.status(400).json({ error: 'job inválido' });
    const jpath = path.join(UPLOAD_DIR, job, 'job.json');
    let data;
    try { data = JSON.parse(fs.readFileSync(jpath, 'utf8')); }
    catch { return res.status(404).json({ error: 'job não encontrado' }); }
    if (data.status !== 'ready') {
      return res.status(409).json({ error: `job não está pronto p/ publicar (status: ${data.status})` });
    }
    const slug = String(data.slug || '');
    if (!SLUG_RE.test(slug)) return res.status(400).json({ error: 'slug inválido no job' });

    const args = ['publish_to_live.py', slug, '--build-dir', BUILD_DIR, '--live-dir', LIVE_DIR];
    const child = spawn('python3', args, { cwd: BUILD_DIR });
    let out = '';
    child.stdout.on('data', (d) => { out += d; });
    child.stderr.on('data', (d) => { out += d; });
    child.on('error', (e) => res.status(500).json({ error: `falha ao rodar publish_to_live: ${e.message}` }));
    child.on('close', (code) => {
      if (res.headersSent) return;
      if (code !== 0) {
        return res.status(500).json({ error: `publish_to_live falhou (rc=${code})`, log: out.slice(-2000) });
      }
      data.status = 'published';
      data.url = `${SITE_URL}/${slug}.html`;
      try { fs.writeFileSync(jpath, JSON.stringify(data, null, 2)); } catch (e) { /* não-fatal */ }
      res.json({ ok: true, url: data.url });
    });
  });

  // ------------------------------------------------- tratamento de erros
  // Erros do multer (LIMIT_FILE_SIZE etc.) e do fileFilter viram 400 com mensagem.
  router.use((err, _req, res, _next) => {
    if (err instanceof multer.MulterError) {
      const msg = err.code === 'LIMIT_FILE_SIZE' ? 'arquivo maior que 30MB' : err.message;
      return res.status(400).json({ error: msg });
    }
    return res.status(400).json({ error: err.message || 'upload inválido' });
  });

  return router;
};
