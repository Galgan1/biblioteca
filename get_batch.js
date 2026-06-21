const fs = require('fs');
const file = 'C:/Users/User/.gemini/antigravity/scratch/biblioteca/refactoring_queue.json';
const queue = JSON.parse(fs.readFileSync(file, 'utf8'));

const batchSize = 60;
const toProcess = queue.pending.splice(0, batchSize);

toProcess.forEach(item => {
  queue.in_progress[item] = true;
});

fs.writeFileSync(file, JSON.stringify(queue, null, 2));

const chunks = [];
for (let i = 0; i < toProcess.length; i += 3) {
  chunks.push(toProcess.slice(i, i + 3));
}

console.log(JSON.stringify(chunks));
