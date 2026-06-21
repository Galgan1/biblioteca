/**
 * youtube.test.js — teste mínimo do youtube.js (Node puro, sem deps externas).
 *
 * NÃO chama a API real do YouTube (não há token no sandbox). Verifica só:
 *   1) o require do módulo não quebra (libs google* são require-lazy lá dentro);
 *   2) a forma da API exportada (4 funções);
 *   3) buildMetadata() num roteiro real produz title/description/tags e
 *      status.containsSyntheticMedia === true.
 *
 * exit 0 = ok; exit 1 = qualquer falha.
 */
const path = require('path');

function fail(msg) {
  console.error(`FALHA: ${msg}`);
  process.exit(1);
}

// 1) require do módulo não pode quebrar.
let yt;
try {
  yt = require('./youtube');
} catch (e) {
  fail(`require('./youtube') quebrou: ${e.message}`);
}

// 2) forma do módulo: as 4 funções esperadas.
for (const fn of ['loadAuth', 'buildMetadata', 'publishVideo', 'setThumbnail']) {
  if (typeof yt[fn] !== 'function') fail(`export ausente ou não-função: ${fn}`);
}

// 3) buildMetadata num roteiro real.
const roteiro = path.join(__dirname, '..', 'videos', 'roteiros', 'arte-da-guerra.json');
let meta;
try {
  meta = yt.buildMetadata(roteiro);
} catch (e) {
  fail(`buildMetadata lançou erro: ${e.message}`);
}

if (!meta || !meta.snippet || !meta.status) fail('meta sem { snippet, status }');

const { snippet, status } = meta;
if (!snippet.title || typeof snippet.title !== 'string') fail('snippet.title ausente/inválido');
if (snippet.title.length > 100) fail(`snippet.title > 100 chars (${snippet.title.length})`);
if (!snippet.description || typeof snippet.description !== 'string') fail('snippet.description ausente/inválido');
if (!Array.isArray(snippet.tags) || snippet.tags.length === 0) fail('snippet.tags ausente/vazio');
if (snippet.categoryId !== '27') fail(`snippet.categoryId esperado '27', veio '${snippet.categoryId}'`);
if (snippet.defaultLanguage !== 'pt-BR') fail(`snippet.defaultLanguage esperado 'pt-BR', veio '${snippet.defaultLanguage}'`);

if (status.containsSyntheticMedia !== true) fail('status.containsSyntheticMedia !== true');
if (status.selfDeclaredMadeForKids !== false) fail('status.selfDeclaredMadeForKids !== false');
if (!status.privacyStatus) fail('status.privacyStatus ausente');

console.log('OK ✓ youtube.js — forma do módulo e buildMetadata validados');
console.log(`  title: ${snippet.title}`);
console.log(`  tags: ${snippet.tags.length} | privacidade: ${status.privacyStatus} | IA: ${status.containsSyntheticMedia}`);
process.exit(0);
