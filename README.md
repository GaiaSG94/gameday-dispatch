# Dispatch

A daily timetable puzzle for Reddit, built on [Devvit Web](https://developers.reddit.com/).

Tonight's yard: five trains (express, freight, local, overnight, shuttle) and five
platforms. The signalman's log gives a few facts - who departs before whom, who
shares adjacent platforms, who is banned from platform 3 - and the timetable is
generated so the assignment is unique.

## How to play

1. Pick a train from the row above the yard.
2. Tap its platform.
3. Tap Clear the signals when every platform is set.

One yard per day, the same for everyone; streaks stored per user in Redis.

## Stack

- React 19 + Tailwind 4 + Vite (client inside a Reddit post)
- Hono server on Devvit (`/api/init`, `/api/submit`), Redis persistence
- Deterministic daily generation (UTC seed), uniqueness brute-forced (120 shunts),
  unit-tested

## Development

``bash
npm install
npm run dev
npm test
npm run type-check
npm run build
``

## Submission (Reddit's Game of the Day Hackathon)

- App listing: `developers.reddit.com/apps/gameday-dispatch` (private until judging ends)
- Demo post: public test subreddit, post running the game

