#!/usr/bin/env node
'use strict';

// Editorial lint for Ali's Russian social copy. Not an AI detector.
const fs = require('node:fs');

const PATTERNS = [
  { id: 'not-x-but-y', severity: 'review', re: /(?<![\p{L}\p{N}_])не\s+[^.!?\n:;]{1,85}?,\s*а\s+[^.!?\n:;]{1,85}/giu,
    why: 'Formulaic contrast requires an editorial purpose.' },
  { id: 'not-just', severity: 'review', re: /(?<![\p{L}\p{N}_])не\s+просто(?![\p{L}\p{N}_])[^.!?\n]{0,110}/giu,
    why: 'Avoid automatic not-just exaggeration.' },
  { id: 'not-about', severity: 'review', re: /(?<![\p{L}\p{N}_])не\s+про\s+[^.!?\n:;]{1,60},?\s+а\s+про\s+[^.!?\n:;]{1,60}/giu,
    why: 'Avoid repeated не про X, а про Y wording.' },
  { id: 'scene-setting-filler', severity: 'review', re: /(?<![\p{L}\p{N}_])(?:в\s+современном\s+мире|в\s+постоянно\s+меняющемся\s+мире|важно\s+отметить|стоит\s+отметить|давайте\s+разбер[её]мся|и\s+вот\s+почему|а\s+теперь\s+самое\s+интересное|как\s+вы\s+уже\s+поняли|погрузимся\s+в|таким\s+образом)(?![\p{L}\p{N}_])/giu,
    why: 'Likely filler; check whether there is a useful fact instead.' },
  { id: 'grandiose-claim', severity: 'review', re: /(?<![\p{L}\p{N}_])(?:революционн(?:ый|ая|ое|ые)|уникальн(?:ый|ая|ое|ые)|новый\s+уровень|играет\s+ключевую\s+роль|бесшовн(?:ый|ая|ое|ые))(?![\p{L}\p{N}_])/giu,
    why: 'Hype requires evidence or revision.' },
  { id: 'false-dialogue-cue', severity: 'review', re: /(?<![\p{L}\p{N}_])(?:знакомо\?|спросите\s+вы\?|и\s+знаете\s+что\?|представьте\s+себе)(?![\p{L}\p{N}_])/giu,
    why: 'Stagey presenter dialogue; check spoken-language fit.' }
];
function locate(text, index) {
  const prefix = text.slice(0, index);
  return { line: prefix.split('\n').length, column: (prefix.split('\n').at(-1) || '').length + 1 };
}
function inspect(text) {
  const findings = [];
  for (const [mark, id] of [['—', 'em-dash'], ['–', 'en-dash']]) {
    let at = 0;
    while ((at = text.indexOf(mark, at)) !== -1) {
      findings.push({ id, severity: 'block', ...locate(text, at), match: mark,
        why: 'Project authorial preference: no long display dashes in public RU copy.' });
      at += mark.length;
    }
  }
  for (const item of PATTERNS) {
    for (const hit of text.matchAll(item.re)) {
      findings.push({ id: item.id, severity: item.severity,
        ...locate(text, hit.index), match: hit[0], why: item.why });
    }
  }
  return findings.sort((a, b) => a.line - b.line || a.column - b.column);
}
function main(argv) {
  const args = argv.slice(2);
  const json = args.includes('--json');
  const strict = args.includes('--strict');
  const paths = args.filter(x => !x.startsWith('--'));
  if (!paths.length) {
    process.stderr.write('Usage: node scripts/check-ru-script-style.cjs [--strict] [--json] file.txt [...] \n');
    process.exitCode = 2;
    return;
  }
  const output = [];
  let hard = false, review = false;
  for (const filename of paths) {
    let input;
    try { input = fs.readFileSync(filename, 'utf8'); }
    catch (error) { process.stderr.write(filename + ': ' + error.message + '\n'); process.exitCode = 2; return; }
    const findings = inspect(input);
    output.push({ filename, findings });
    hard ||= findings.some(x => x.severity === 'block');
    review ||= findings.some(x => x.severity === 'review');
  }
  if (json) process.stdout.write(JSON.stringify(output, null, 2) + '\n');
  else for (const item of output) {
    process.stdout.write(item.filename + ': ' + item.findings.length + ' findings\n');
    for (const f of item.findings) {
      process.stdout.write('  ' + f.severity + ' ' + f.id + ' ' + f.line + ':' + f.column + ' ' + JSON.stringify(f.match) + '\n');
    }
  }
  if (hard || (strict && review)) process.exitCode = 1;
}
if (require.main === module) main(process.argv);
module.exports = { inspect };
