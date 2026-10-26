#!/usr/bin/env node
'use strict';

// Opt-in review of known rejected comedy patterns for Ali's Russian social scripts.
// Never equate a regex match with proof that the copy was written by AI.
const fs = require('node:fs');

const rules = [
  { id: 'imagined-calm', pattern: /тут я ещё сохранял спокойствие/iu },
  { id: 'where-is-the-whole-car', pattern: /а сама (kia|киа|машина) вообще на месте/iu },
  { id: 'jealous-car', pattern: /(машина|kia|киа|автомобиль).{0,90}приревнов/iu },
  { id: 'pickup-as-house-move', pattern: /(пикап|грузовик|фургон).{0,140}(попал|превратился).{0,70}переезд/iu },
  { id: 'assemble-over-weekend', pattern: /собери.{1,45}за выходные/iu }
];

function review(text) {
  return rules.filter(rule => rule.pattern.test(text)).map(rule => rule.id);
}

function main(args) {
  const strict = args.includes('--strict');
  const filenames = args.filter(arg => !arg.startsWith('--'));
  if (!filenames.length) { process.stderr.write('Usage: node scripts/check-ru-humor-failures.cjs [--strict] FILE\n'); process.exitCode = 2; return; }
  let flagged = false;
  for (const filename of filenames) {
    const findings = review(fs.readFileSync(filename, 'utf8'));
    console.log(filename + ': ' + (findings.length ? findings.join(', ') : 'no known bad patterns'));
    flagged ||= findings.length > 0;
  }
  if (strict && flagged) process.exitCode = 1;
}

if (require.main === module) main(process.argv.slice(2));
module.exports = { review };
