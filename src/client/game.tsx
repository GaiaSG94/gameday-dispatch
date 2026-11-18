import './index.css';

import { useCallback, useEffect, useState } from 'react';
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { clueText } from '../shared/puzzle';
import type { Clue, Train } from '../shared/puzzle';

type Init = {
  day: string;
  username: string;
  streak: number;
  solvedToday: boolean;
  startedAt: number;
  trains: Train[];
  clues: Clue[];
};

type Result = { won: boolean; streak: number; elapsedMs: number };

const ICONS: Record<Train, string> = {
  express: '🚄',
  freight: '🚛',
  local: '🚆',
  overnight: '🌙',
  shuttle: '🚃',
};

const App = () => {
  const [init, setInit] = useState<Init | null>(null);
  const [assignment, setAssignment] = useState<(Train | '')[]>([]);
  const [active, setActive] = useState<Train | null>(null);
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [seconds, setSeconds] = useState(0);

  const load = useCallback(async () => {
    try {
      const res = await fetch('/api/init');
      const data = await res.json();
      if (data.status === 'error') throw new Error(data.message);
      setInit(data);
      setAssignment(Array.from({ length: data.trains.length }, () => ''));
      setActive(data.trains[0] ?? null);
      setResult(null);
      setSeconds(0);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'load failed');
    }
  }, []);

  useEffect(() => {
    void load();
  }, [load]);

  useEffect(() => {
    const timer = setInterval(() => setSeconds((s) => s + 1), 1000);
    return () => clearInterval(timer);
  }, []);

  const place = (platform: number) => {
    if (!active) return;
    setAssignment((current) =>
      current.map((v, i) => {
        if (i === platform) return active;
        if (v === active) return '';
        return v;
      })
    );
    const remaining = init?.trains.filter((t) => !assignment.includes(t) && t !== active) ?? [];
    setActive(remaining[0] ?? null);
  };

  const submit = async () => {
    try {
      const res = await fetch('/api/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ assignment, startedAt: Date.now() - seconds * 1000 }),
      });
      const data = await res.json();
      if (data.status === 'error') throw new Error(data.message);
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'submit failed');
    }
  };

  if (error) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#101f18] text-[#d3e8db]">
        <p>{error}</p>
      </div>
    );
  }
  if (!init) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#101f18] text-[#6f9a80]">
        <p className="animate-pulse">Switching the yard…</p>
      </div>
    );
  }

  const placed = assignment.filter(Boolean).length;
  const clock = `${String(Math.floor(seconds / 60)).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}`;

  return (
    <div className="flex min-h-screen flex-col items-center gap-4 bg-[#101f18] px-4 py-6 text-[#d3e8db]">
      <header className="flex w-full max-w-md items-center justify-between">
        <h1 className="text-xl font-black tracking-[0.3em] text-[#ffd166]">DISPATCH</h1>
        <div className="text-sm font-semibold text-[#6f9a80]">
          <span className="mr-3">{clock}</span>
          <span>🔥 {result ? result.streak : init.streak}</span>
        </div>
      </header>
      <p className="max-w-md text-center text-[13px] leading-snug text-[#6f9a80]">
        Five trains, five platforms, one timetable that works. Pick a train, then tap its
        platform.
      </p>
      <div className="flex w-full max-w-md flex-wrap justify-center gap-1.5">
        {init.trains.map((train) => (
          <button
            key={train}
            onClick={() => setActive(train)}
            disabled={assignment.includes(train)}
            className={`rounded-full border-2 px-3 py-1.5 text-xs font-bold capitalize disabled:opacity-30 ${
              active === train
                ? 'border-[#ffd166] bg-[#ffd166] text-[#101f18]'
                : 'border-[#234632] bg-[#16291e] text-[#d3e8db]'
            }`}
          >
            {ICONS[train]} {train}
          </button>
        ))}
      </div>
      <div className="flex w-full max-w-md gap-2 rounded-xl border-2 border-[#234632] bg-[#16291e] p-3">
        {Array.from({ length: init.trains.length }, (_, platform) => (
          <button
            key={platform}
            onClick={() => place(platform)}
            className="flex h-20 flex-1 flex-col items-center justify-center gap-1 rounded-lg border-2 border-dashed border-[#2d5a3f] bg-[#101f18] text-2xl"
            aria-label={`platform ${platform + 1}`}
          >
            {assignment[platform] ? ICONS[assignment[platform] as Train] : <span className="text-xs text-[#6f9a80]">P{platform + 1}</span>}
          </button>
        ))}
      </div>
      <ul className="w-full max-w-md space-y-1.5 rounded-xl border-2 border-[#234632] bg-[#16291e] p-4 text-[13px]">
        {init.clues.map((clue, i) => (
          <li key={i} className="flex items-start gap-2">
            <span className="inline-block h-1.5 w-1.5 rounded-full bg-[#ffd166] mt-1.5" />
            {clueText(clue)}
          </li>
        ))}
      </ul>
      {!result ? (
        <button
          onClick={() => void submit()}
          disabled={placed < init.trains.length}
          className="w-full max-w-md rounded-full bg-[#ffd166] py-3 text-base font-black uppercase tracking-widest text-[#101f18] transition-transform active:scale-[0.98] disabled:opacity-40"
        >
          Clear the signals ({placed}/{init.trains.length})
        </button>
      ) : (
        <div className="flex w-full max-w-md flex-col items-center gap-3 rounded-xl border-2 border-[#234632] bg-[#16291e] p-5 text-center">
          <p className="text-2xl font-black tracking-widest">
            {result.won ? 'ALL TRAINS OUT' : 'DEADLOCK'}
          </p>
          <p className="text-sm text-[#6f9a80]">
            {result.won
              ? `Cleared in ${clock} — streak 🔥 ${result.streak}. The yard resets tomorrow.`
              : 'Two trains want the same path. Re-shunt and try again.'}
          </p>
          <button
            onClick={() => setResult(null)}
            className="rounded-full border-2 border-[#ffd166] px-6 py-2 text-sm font-bold uppercase tracking-widest text-[#ffd166]"
          >
            Back to the yard
          </button>
        </div>
      )}
    </div>
  );
};

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);
