'use strict';
const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { review } = require('../scripts/check-ru-humor-failures.cjs');

const bad = [
 ['imagined-calm', 'Начали с куска картона размером с дверь. Тут я ещё сохранял спокойствие.'],
 ['where-is-the-whole-car', 'В какой-то момент захотелось спросить: а сама Kia вообще на месте?'],
 ['jealous-car', 'Одну деталь завернули с такой заботой, что машина может приревновать.'],
 ['pickup-as-house-move', 'Пикап приехал за запчастями, а попал на переезд.'],
 ['assemble-over-weekend', 'Осталось приложить инструкцию: «Собери Kia за выходные».']
];
for (const [id, text] of bad) {
  test('flags rejected Kia pattern: ' + id, () => assert.ok(review(text).includes(id)));
}
test('passes honest process narration', () => {
  assert.deepEqual(review('Упаковали крышку багажника Kia и погрузили детали в пикап.'), []);
});
test('does not reject a literal house move', () => {
  assert.deepEqual(review('Переезд склада назначен на вторник. Запчасти упакованы.'), []);
});
test('does not reject another specific and ordinary observation', () => {
  assert.deepEqual(review('Крышку багажника в кузов поднимали вдвоём. Это видно на записи.'), []);
});
test('CLI strict distinguishes rejected and clean patterns', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'humor-regression-'));
  const f = path.join(dir, 'sample.txt');
  const script = path.join(__dirname, '..', 'scripts', 'check-ru-humor-failures.cjs');
  try {
    fs.writeFileSync(f, bad[3][1]);
    assert.equal(spawnSync(process.execPath, [script, '--strict', f]).status, 1);
    fs.writeFileSync(f, 'Запчасти Kia погрузили в кузов и подготовили к отправке.');
    assert.equal(spawnSync(process.execPath, [script, '--strict', f]).status, 0);
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
});
