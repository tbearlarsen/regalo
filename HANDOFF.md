# HANDOFF.md

This file is written for a future Claude session picking up this project cold,
not for a human audience — `CLAUDE.md` covers role, workflow, and working
rules; this file covers continuity: what's actually true right now, and what
went wrong before that's worth not repeating. Update the "Current status"
section in place and append to the corrections log at Session Close. Read
this file in full at Session Start, right after `git pull` and `CLAUDE.md`.

---

## Current status

- The site is a small static Astro (static output) gift-announcement page —
  a single long scroll revealing a trip to Møns Klint, Denmark, gifted by
  Thorbjørn and his girlfriend to her sister, the sister's partner, and their
  baby daughter. Accessed via a QR code printed on a card; the site itself is
  the gift reveal.
- Single non-technical stakeholder (the user). No backend, no CMS, no
  database — content is hardcoded in Astro source under `src/`.
- Hosting is GitHub Pages, deploying on push to `main` (per `.github/`
  workflow and `CLAUDE.md`'s Commits section).
- `package.json` scripts are `dev`, `build`, `preview`, `astro` — all via
  `astro`. `.claude/settings.json` grants Bash permission for these plus
  `git pull` / `add` / `commit` / `push`.
- **Unresolved gap, flagged not fixed:** `CLAUDE.md` names
  `_project/PLAN.md`, `PROGRESS.md`, `DECISIONS.md`, and `QUESTIONS.md` as
  the project's "Source of Truth Files," and its Session Start procedure
  instructs reading `_project/PROGRESS.md` and checking `_project/QUESTIONS.md`
  every session. But `_project/` is listed in `.gitignore`, and a past commit
  (`545f760`, "Remove `_project/` from repo — internal dev files only")
  actively removed it from git history. As of this writing `_project/` does
  not exist in the working tree at all. This means the Source of Truth
  scaffold `CLAUDE.md` describes currently exists only outside git, if it
  exists anywhere — a fresh clone or a new machine has none of it, and
  nothing enforces that it gets recreated. This HANDOFF.md does not resolve
  this; it's recorded here so a future session doesn't silently assume the
  files are present, and so the user can decide whether to recreate
  `_project/` locally, stop gitignoring it, or change `CLAUDE.md` to stop
  calling it Source of Truth.

---

## Corrections that actually matter

Append-only. Each entry: what was wrong, what changed, and why — the
reasoning is worth more than the diff, because reasoning is what doesn't
survive in `git log`.

1. **2026-09-14 — Arkhon backport audit against the shared cross-project template.**
   Arkhon (the meta-layer project at `/projects/Arkhon` that tracks patterns
   across sibling projects) audited this project's `CLAUDE.md` against the
   shared cross-project template and, at the user's direction, backported
   four fixes:
   - Added `git pull` as the first step of Session Start. It was previously
     absent, meaning a session could start working against a stale local
     checkout with no prompt to catch it.
   - Rewrote the Commits section. It previously read only "never commit
     until the user confirms a step is done," with no mention of push at
     all. It now matches the current template pattern: git stays local with
     no confirmation needed for that default, but on an explicit wrap-up
     trigger ("wrap up," "end session"), stage/commit/push happen
     immediately with no separate confirmation step — the trigger phrase
     itself is the permission. This project's version explicitly calls out
     that push matters here specifically because deploy is via GitHub Pages
     on push to `main`, so a wrap-up that's committed but not pushed doesn't
     actually ship the site.
   - Created `.claude/settings.json` (did not previously exist) with real
     permissions matching this project's actual `package.json` scripts
     (`dev`, `build`, `preview`, `astro`) plus `git pull`/`add`/`commit`/`push`
     — not a generic template guess.
   - Scaffolded empty `directives/` and `execution/` folders, each with a
     README noting they're intentionally empty until a workflow or script
     actually repeats — per the template's rule that these directories
     exist to hold *proven* recurring patterns, not to be pre-filled on
     spec.
