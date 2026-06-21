// seed_admin.js — cria/atualiza o admin inicial em users.json a partir de
// ADMIN_USER / ADMIN_PASSWORD (você define a senha; ela nunca trafega por terceiros).
// Uso na VPS:
//   cd /opt/biblioteca-pdf && ADMIN_USER=admin ADMIN_PASSWORD='SuaSenhaForte' node seed_admin.js
const fs = require('fs');
const path = require('path');
const { _hashPassword } = require('./auth');

const U = process.env.ADMIN_USER;
const P = process.env.ADMIN_PASSWORD;
if (!U || !P) {
  console.error('Defina ADMIN_USER e ADMIN_PASSWORD no ambiente. Ex.:');
  console.error("  ADMIN_USER=admin ADMIN_PASSWORD='senha' node seed_admin.js");
  process.exit(1);
}

const file = path.join(__dirname, 'users.json');
let users = [];
try { users = JSON.parse(fs.readFileSync(file, 'utf8')); } catch { users = []; }

const { salt, hash } = _hashPassword(String(P));
const rec = { username: U, salt, hash, role: 'admin', createdAt: new Date().toISOString() };
const i = users.findIndex((x) => x.username === U);
if (i >= 0) users[i] = rec; else users.push(rec);

fs.writeFileSync(file, JSON.stringify(users, null, 2), { mode: 0o600 });
console.log(`admin "${U}" pronto (role=admin) em users.json`);
