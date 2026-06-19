# PLAN.md — Master Site Plan

## Concept

A gift announcement website for a weekend trip to Møns Klint, delivered via QR code
inside an envelope. Recipients scan the code at the wedding and the site reveals the trip.

The experience: **dark → light**. The hero is a night sky over the chalk cliffs (referencing
Møns Klint's status as Europe's largest Dark Sky Park). As you scroll, the page opens into
warm cream — the gift unwrapping itself section by section.

---

## Tech Stack

- Framework: Astro (static)
- Fonts: Georgia + Qwitcher Grypen (same as boda-nube)
- Palette: Dark (#0f0f1a) hero → cream (#faf9f7) content
- Hosting: GitHub Pages (to be configured)

---

## Page Structure (single long-scroll)

| Section | Status | Description |
| --- | --- | --- |
| Hero | 🔲 | Full-viewport dark sky, CSS star field, cliff silhouette SVG, "Møns Klint" title |
| Reveal | 🔲 | "We're taking you on a trip." — the gift message, who's going |
| The Place | 🔲 | 3–4 cards about what Møns Klint is (cliffs, dark sky, sea, trails) |
| The Details | 🔲 | Dates (TBD), countdown timer, add-to-calendar |
| Photo Wall | 🔲 | Empty polaroid frames — placeholder for post-trip photos |

---

## Confirmed Decisions

- Single-page, no nav
- English (TBD — could be Danish)
- Astro static build
- Same visual DNA as boda-nube (Georgia, Qwitcher Grypen, restrained palette)
- Hero is dark/night-sky; content is cream — a visual contrast that references the Dark Sky Park

---

## Open Questions

See `_project/QUESTIONS.md`

---

## Out of Scope (for now)

- Multiple pages / nav
- i18n / multiple languages
- RSVP / date coordination form (could add later)
- Photo upload (post-trip feature, not launch scope)
