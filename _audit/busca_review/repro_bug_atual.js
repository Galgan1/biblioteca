// Reproduz o bug da busca ATUAL (em produção): includes() não normaliza acentos.
// Espelha o queryOk real do script.js. Exit !=0 = bug reproduzido.
const livros = [
  { title: 'Hábitos Atômicos', author: 'James Clear' },
  { title: 'Meditações', author: 'Marco Aurélio' },
  { title: 'A Arte da Guerra', author: 'Sun Tzu' },
];
const queryOk = (b, q) => b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q);
let falhas = 0;
for (const [q, esperado] of [['habitos', 'Hábitos Atômicos'], ['meditacoes', 'Meditações'], ['estrategia', null]]) {
  const hits = livros.filter((b) => queryOk(b, q.toLowerCase()));
  if (esperado && !hits.some((b) => b.title === esperado)) {
    console.log(`  BUG: "${q}" NAO acha "${esperado}" (acento perdido)`); falhas++;
  } else console.log(`  ok:  "${q}" -> ${hits.length} hit(s)`);
}
console.log(falhas ? `\n  => ${falhas} buscas quebradas pelo acento (bug confirmado)` : '\n  ok');
process.exit(falhas ? 1 : 0);
