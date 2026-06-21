const fs = require('fs');
const path = 'C:/Users/User/.gemini/config/skills/drdolabela';
const dirs = fs.readdirSync(path).filter(f => fs.statSync(path + '/' + f).isDirectory());

const report = fs.readFileSync('C:/Users/User/.gemini/antigravity/brain/4fe95e9d-2be3-4edd-9c23-7e8c24f39b06/audit_report.md', 'utf8');
const redList = [];
const lines = report.split('\n');
for (let line of lines) {
  if (line.includes('|')) {
    const parts = line.split('|').map(s => s.trim());
    if (parts.length >= 3 && parts[2]) {
      const score = parseFloat(parts[2]);
      if (!isNaN(score) && score < 7.0) {
        const skill = parts[1].replace(/`/g, '');
        redList.push(skill);
      }
    }
  }
}

const pending = dirs.filter(d => !redList.includes(d));
const queue = {
  pending: pending,
  in_progress: {},
  completed: redList
};

fs.writeFileSync('C:/Users/User/.gemini/antigravity/scratch/biblioteca/refactoring_queue.json', JSON.stringify(queue, null, 2));
console.log(`Total dirs: ${dirs.length}`);
console.log(`Red list (already completed): ${redList.length}`);
console.log(`Pending: ${pending.length}`);
