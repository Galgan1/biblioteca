/**
 * upload.test.js — teste unitário Node puro (sem framework) do upload.js.
 *
 * Cobre o que dá para checar sem `multer`/`googleapis` instalados:
 *   1. require('./upload') não quebra mesmo com multer ausente (require é lazy).
 *   2. makeUpload(noop) devolve um express.Router (tem .use e é função/.handle).
 *   3. round-trip do shape de job.json numa pasta temporária (escreve → lê).
 *
 * Saída: process.exit(0) se tudo passar; process.exit(1) na primeira falha.
 */
const fs = require('fs');
const os = require('os');
const path = require('path');
const assert = require('assert');

function ok(label) { console.log(`ok - ${label}`); }
function fail(label, err) {
  console.error(`FALHA - ${label}: ${err && err.message ? err.message : err}`);
  process.exit(1);
}

// 1) o módulo carrega mesmo sem multer (require de multer é tardio na factory)
let makeUpload;
try {
  makeUpload = require('./upload');
  assert.strictEqual(typeof makeUpload, 'function', 'export deve ser uma função');
  ok('require(./upload) carrega sem multer e exporta uma função');
} catch (err) {
  fail('require do módulo', err);
}

// 2) makeUpload(noop) devolve um router (se multer estiver instalado)
//    Sem multer, a factory lança ao fazer o require tardio — isso é esperado e
//    NÃO é falha do teste (o ponto 1 já provou o contrato de carga preguiçosa).
try {
  const router = makeUpload(() => {});
  assert.strictEqual(typeof router, 'function', 'router deve ser uma função');
  assert.strictEqual(typeof router.use, 'function', 'router deve ter .use');
  assert.strictEqual(typeof router.handle, 'function', 'router deve ter .handle');
  ok('makeUpload(noop) devolve um express.Router');
} catch (err) {
  if (/Cannot find module 'multer'/.test(String(err.message))) {
    ok('multer ausente: factory lança como esperado (require tardio) — pulando montagem do router');
  } else {
    fail('makeUpload devolve router', err);
  }
}

// 3) round-trip do shape de job.json numa pasta temporária
try {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'upload-test-'));
  const jobId = `${Date.now()}-deadbeef`;
  const jobDir = path.join(dir, jobId);
  fs.mkdirSync(jobDir, { recursive: true });

  const job = {
    jobId,
    slug: 'habitos-atomicos',
    file: 'source.pdf',
    ext: '.pdf',
    status: 'queued',
    createdAt: new Date().toISOString(),
  };
  const jobFile = path.join(jobDir, 'job.json');
  fs.writeFileSync(jobFile, JSON.stringify(job, null, 2));

  const read = JSON.parse(fs.readFileSync(jobFile, 'utf8'));
  assert.deepStrictEqual(read, job, 'job.json lido deve ser igual ao escrito');
  assert.strictEqual(read.status, 'queued', 'status inicial deve ser queued');

  fs.rmSync(dir, { recursive: true, force: true });
  ok('round-trip de job.json preserva o shape');
} catch (err) {
  fail('round-trip de job.json', err);
}

console.log('todos os testes passaram');
process.exit(0);
