export const TRAINS = ['express', 'freight', 'local', 'overnight', 'shuttle'] as const;
export type Train = (typeof TRAINS)[number];

export type Clue =
  | { kind: 'leftOf'; a: Train; b: Train }
  | { kind: 'adjacent'; a: Train; b: Train }
  | { kind: 'notPlatform'; a: Train; platform: number }
  | { kind: 'position'; a: Train; platform: number };

export type DispatchPuzzle = {
  day: string;
  clues: Clue[];
  solution: Train[];
};

export const dayKeyUTC = (now: Date = new Date()): string => now.toISOString().slice(0, 10);

export const dailySeed = (day: string): number => {
  let hash = 2166136261;
  const input = 'dispatch:' + day;
  for (let i = 0; i < input.length; i++) {
    hash ^= input.charCodeAt(i);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
};

export const mulberry32 = (seed: number): (() => number) => {
  let a = seed >>> 0;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
};

export const clueHolds = (clue: Clue, assignment: Train[]): boolean => {
  const platformOf = (train: Train): number => assignment.indexOf(train);
  switch (clue.kind) {
    case 'leftOf':
      return platformOf(clue.a) < platformOf(clue.b);
    case 'adjacent':
      return Math.abs(platformOf(clue.a) - platformOf(clue.b)) === 1;
    case 'notPlatform':
      return platformOf(clue.a) !== clue.platform;
    case 'position':
      return platformOf(clue.a) === clue.platform;
  }
};

export const countSolutions = (clues: Clue[]): number => {
  let total = 0;
  const assignment: Train[] = [...TRAINS];
  const walk = (depth: number): void => {
    if (depth === TRAINS.length) {
      if (clues.every((clue) => clueHolds(clue, assignment))) total++;
      return;
    }
    for (let i = depth; i < TRAINS.length; i++) {
      const picked = assignment[depth] ?? 'express';
      assignment[depth] = assignment[i] ?? 'express';
      assignment[i] = picked;
      walk(depth + 1);
      const back = assignment[depth] ?? 'express';
      assignment[depth] = assignment[i] ?? 'express';
      assignment[i] = back;
    }
  };
  walk(0);
  return total;
};

const randomClue = (rand: () => number, solution: Train[]): Clue => {
  const a = TRAINS[Math.floor(rand() * TRAINS.length)] ?? 'express';
  const b = TRAINS[Math.floor(rand() * TRAINS.length)] ?? 'freight';
  const platform = solution.indexOf(a);
  const kind = Math.floor(rand() * 4);
  if (kind === 0 && a !== b) return { kind: 'leftOf', a, b };
  if (kind === 1 && a !== b) return { kind: 'adjacent', a, b };
  if (kind === 2) {
    const wrong = (platform + 1 + Math.floor(rand() * 4)) % TRAINS.length;
    return { kind: 'notPlatform', a, platform: wrong };
  }
  return { kind: 'position', a, platform };
};

export const generateDispatch = (day: string): DispatchPuzzle => {
  const rand = mulberry32(dailySeed(day));
  const solution = [...TRAINS].sort(() => rand() - 0.5);
  const clues: Clue[] = [];
  let count = countSolutions(clues);
  for (let round = 0; round < 60 && count > 1; round++) {
    let best: Clue | null = null;
    let bestCount = count;
    for (let trial = 0; trial < 10; trial++) {
      const candidate = randomClue(rand, solution);
      if (!clueHolds(candidate, solution)) continue;
      if (clues.some((clue) => JSON.stringify(clue) === JSON.stringify(candidate))) continue;
      const next = countSolutions([...clues, candidate]);
      if (next >= 1 && next < bestCount) {
        best = candidate;
        bestCount = next;
        if (next === 1) break;
      }
    }
    if (!best) break;
    clues.push(best);
    count = bestCount;
  }
  return { day, clues, solution };
};

export const isCorrectDispatch = (puzzle: DispatchPuzzle, assignment: Train[]): boolean =>
  puzzle.solution.every((train, i) => assignment[i] === train);

export const clueText = (clue: Clue): string => {
  const name = (train: Train): string => `the ${train}`;
  switch (clue.kind) {
    case 'leftOf':
      return `${name(clue.a)} departs from a lower platform than ${name(clue.b)}.`;
    case 'adjacent':
      return `${name(clue.a)} and ${name(clue.b)} share adjacent platforms.`;
    case 'notPlatform':
      return `${name(clue.a)} is not on platform ${clue.platform + 1}.`;
    case 'position':
      return `${name(clue.a)} sits on platform ${clue.platform + 1}.`;
  }
};
