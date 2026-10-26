'use strict';
const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { spawnSync } = require('node:child_process');
const { inspect } = require('../scripts/check-ru-script-style.cjs');
const ids = str => inspect(str).map(x => x.id);

test('blocks both long Unicode dash forms', () => {
  const result = inspect('Машина — детали. Контакт – менеджер.');
  assert.equal(result.filter(x => x.severity === 'block').length, 2);
  assert.deepEqual(result.map(x => x.id), ['em-dash', 'en-dash']);
});
test('flags formulaic contrast rather than all negation', () => {
  assert.ok(ids('Это не просто сайт, а новая философия.').includes('not-x-but-y'));
  assert.ok(ids('Это не просто сайт, а новая философия.').includes('not-just'));
  assert.equal(inspect('Название детали необязательно. Можно приложить фото.').length, 0);
});
test('flags hype, boilerplate and stagey dialogue', () => {
  assert.ok(ids('Важно отметить, что это революционный инструмент.').includes('scene-setting-filler'));
  assert.ok(ids('Важно отметить, что это революционный инструмент.').includes('grandiose-claim'));
  assert.ok(ids('И знаете что? Представьте себе.').includes('false-dialogue-cue'));
});
test('project-fact script passes', () => {
  const script = 'На телефоне заявка оформляется в три шага. Сначала указываешь марку, модель и год машины. Затем описываешь деталь. Можно приложить фотографию. Если нужно несколько деталей, добавляешь их в одну заявку.';
  assert.deepEqual(inspect(script), []);
});
test('reports line and column', () => {
  const result = inspect('Заявка готова.\nЭто не просто форма, а волшебство.');
  assert.equal(result.find(x => x.id === 'not-just').line, 2);
});
test('CLI blocks hard finding; strict also blocks review finding', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ru-style-'));
  const file = path.join(dir, 'sample.txt');
  const cli = path.resolve(__dirname, '../scripts/check-ru-script-style.cjs');
  try {
    fs.writeFileSync(file, 'Клиент — менеджер.');
    assert.equal(spawnSync(process.execPath, [cli, file]).status, 1);
    fs.writeFileSync(file, 'Это не просто форма, а мечта.');
    assert.equal(spawnSync(process.execPath, [cli, file]).status, 0);
    assert.equal(spawnSync(process.execPath, [cli, '--strict', file]).status, 1);
    fs.writeFileSync(file, 'На сайте можно добавить несколько деталей в одну заявку.');
    assert.equal(spawnSync(process.execPath, [cli, '--strict', file]).status, 0);
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
});
