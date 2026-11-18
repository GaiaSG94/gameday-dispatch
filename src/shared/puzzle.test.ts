import assert from 'node:assert/strict';
import { test } from 'node:test';

import { countSolutions, dailySeed, generateDispatch, isCorrectDispatch } from './puzzle.ts';

test('seed deterministe', () => {
  assert.equal(dailySeed('2026-12-01'), dailySeed('2026-12-01'));
});

test('la gare du jour est deterministe et unique', () => {
  const a = generateDispatch('2026-12-01');
  const b = generateDispatch('2026-12-01');
  assert.deepEqual(a.solution, b.solution);
  assert.deepEqual(a.clues, b.clues);
  assert.equal(countSolutions(a.clues), 1);
});

test('la solution verifie tous les indices', () => {
  for (const day of ['2026-12-01', '2026-12-03', '2026-12-09']) {
    const puzzle = generateDispatch(day);
    assert.ok(isCorrectDispatch(puzzle, puzzle.solution), day);
    assert.equal(countSolutions(puzzle.clues), 1, day);
  }
});

test('un aiguillage errone est rejete', () => {
  const puzzle = generateDispatch('2026-12-01');
  const wrong = [...puzzle.solution];
  wrong[0] = puzzle.solution[1] ?? 'express';
  wrong[1] = puzzle.solution[0] ?? 'freight';
  assert.equal(isCorrectDispatch(puzzle, wrong), false);
});
