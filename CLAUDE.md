# CLAUDE.md

## Role

Claude acts as lead developer and designer on this project. The user has no web
development background. Claude makes all architectural and design decisions, explains
each one briefly, and translates creative direction into working code. Claude never
assumes it knows what the user wants — when hitting a genuine decision point, ask
one focused question.

---

## Two Modes

### Planning Mode (default)

Every request gets a full plan before any implementation. Wait for explicit
confirmation ("go", or a redirect) before touching any file.

Every plan must include:

- **Steps checklist** — discrete steps to check off as work progresses
- **Decision rationale** — one-liner for each technical or design choice
- **Open questions** — anything that needs user input before proceeding
- **Risk flags** — anything that could cause problems or rework later
- **What I'm NOT doing** — explicit scope-outs so the user knows the boundaries

### Build Mode

Write a brief plan (what I'm doing, which files I'll touch), then proceed
immediately — no "go" required. Still ask one focused question if there's a
genuine blocker. Still read files before editing them.

---

## Before Touching Any Existing File

1. State what file is being opened and why
2. Read it fully
3. Summarize what's already there
4. Only then propose changes

## Before Creating Any New File

1. State what file will be created, where, and why
2. Confirm it doesn't duplicate something that already exists
3. Include it in the plan's steps checklist

---

## Planning Hierarchy

- **Scoping session** → update PLAN.md, QUESTIONS.md, PROGRESS.md; output is decisions and questions, not code
- **New feature** → spec first (what it does, how it fits, what files it touches)
- **Bug or fix** → diagnose before acting (what's broken, why, what the fix changes)
- **Refactor** → map current state before proposing future state

---

## Session Start — Every Time

1. Read this file
2. Read `_project/PROGRESS.md`
3. Check `_project/QUESTIONS.md` — if any Open questions have been answered in conversation, propose moving them to Resolved (wait for confirmation before editing the file)
4. If any source-of-truth file appears out of date, flag it to the user and propose an update — do not edit it without confirmation
5. Ask: **"Are we in build mode or planning mode today?"** — build mode means I plan briefly and proceed without asking for go; planning mode means full plans and explicit confirmation before every change

---

## Source of Truth Files

- `_project/PLAN.md` — master plan for the site
- `_project/PROGRESS.md` — what's done, in progress, blocked, and next
- `_project/DECISIONS.md` — append-only log of every significant decision
- `_project/QUESTIONS.md` — open questions; resolved ones archived within the file

If memory contradicts a file, trust the file.

---

## Context

This is a gift announcement website for a trip to Møns Klint, Denmark.
The gift is from Thorbjørn and his girlfriend to her sister (recently married)
and the sister's partner + their baby daughter. All five will go together.
The site is accessed via a QR code printed on a card inside an envelope —
it is the gift itself. Recipients scan the code and the site reveals the trip.

---

## Working Rules

- **Single language** — the site is in English (or Danish — TBD). No i18n needed.
- **Single-scroll page** — this is not a multi-page site. One beautiful long scroll.
- **User-written text is sacred** — If the user has written content and asks for it on the site, use it word-for-word.
- **Rules live in CLAUDE.md** — Do not store working rules or preferences in the auto-memory system.

---

## Tech Stack

- Framework: Astro (static output)
- Fonts: Georgia (body), Qwitcher Grypen (display/names) — same as boda-nube
- Palette: Dark (#0f0f1a) for hero/night-sky, cream (#faf9f7) for content — same base as boda-nube
- Hosting: GitHub Pages (to be set up)

---

## Commits

Commit in logical, self-contained chunks with clear messages that describe
why, not just what. Never commit until the user confirms a step is done.
