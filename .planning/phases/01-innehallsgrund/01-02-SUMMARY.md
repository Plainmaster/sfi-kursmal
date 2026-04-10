---
phase: 01-innehallsgrund
plan: 02
subsystem: data
tags: [json, sfi, kursmal, cefr-b1, cefr-b2, swedish-education]

# Dependency graph
requires:
  - phase: 01-01
    provides: "Kurs B goals, design tokens, canonical domain keys and ID pattern"
provides:
  - "Kurs C course goals (25 'Jag kan...' statements) at CEFR B1 level"
  - "Kurs D course goals (24 'Jag kan...' statements) at CEFR B2 level"
  - "Complete content foundation: 73 goals across 3 courses x 5 domains"
affects: [02-innehallsgrund, phase-2]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Language complexity increases B->C->D while JSON structure stays identical"
    - "Theme tags assigned more broadly at higher course levels (samhalle more frequent in D)"

key-files:
  created:
    - src/data/kurs-c.json
    - src/data/kurs-d.json
  modified: []

key-decisions:
  - "Kurs C goals use B1 vocabulary: subordinate clauses, broader topics (news, workplace, society)"
  - "Kurs D goals use B2 vocabulary: argumentation, formal register, structured presentations"
  - "Theme assignments broader for C and D since topics expand beyond personal life"
  - "muntlig-produktion has 4-5 goals per course (fewer than other domains) matching B pattern"

patterns-established:
  - "Cross-course structural consistency verified by automated script"
  - "73 total goals across 3 courses within target range (60-120)"

requirements-completed: [KURS-01, KURS-02, KURS-04, KURS-05, KURS-06, DESIGN-05]

# Metrics
duration: 2min
completed: 2026-04-10
---

# Phase 1 Plan 2: Kurs C and Kurs D Data Summary

**49 simplified "Jag kan..." goals for SFI kurs C (B1) and kurs D (B2) across all 5 skill domains, completing the 73-goal content foundation**

## Performance

- **Duration:** 2 min
- **Started:** 2026-04-10T18:57:58Z
- **Completed:** 2026-04-10T18:59:58Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments
- Authored 25 kurs C goals at CEFR B1 level: broader topics (news, workplace, society), subordinate clauses, opinion expression
- Authored 24 kurs D goals at CEFR B2 level: argumentation, formal register, structured texts, source comparison
- Verified cross-file domain key consistency across all 3 course files (B, C, D)
- Total content foundation complete: 73 goals across 15 domain/course combinations

## Task Commits

Each task was committed atomically:

1. **Task 1: Author kurs C goals** - `9323286` (feat)
2. **Task 2: Author kurs D goals** - `db3dd28` (feat)

## Files Created/Modified
- `src/data/kurs-c.json` - 25 course C goals with stable IDs (C-XXXX-NN), kursplan_year 2018, and theme assignments
- `src/data/kurs-d.json` - 24 course D goals with stable IDs (D-XXXX-NN), kursplan_year 2018, and theme assignments

## Decisions Made
- Kurs C goals target CEFR B1: students handle news, workplace instructions, society topics; can express opinions with reasoning
- Kurs D goals target CEFR B2: students handle argumentation, formal writing, structured presentations, source comparison
- Theme tags assigned more broadly at higher levels since topics expand beyond personal daily life
- samhalle theme used more frequently in D (societal focus); arbete-och-studier for workplace goals
- muntlig-produktion kept at 4-5 goals (matching kurs B pattern) since one-way speaking has fewer distinct checkable competencies

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered
None.

## User Setup Required
None -- no external service configuration required.

## Next Phase Readiness
- All 3 course data files complete (B: 24 goals, C: 25 goals, D: 24 goals)
- Domain keys match across all files and design-tokens.json
- All goal IDs stable and sequential -- safe for localStorage key generation in Phase 2
- Phase 01 content foundation is complete; ready for Phase 02 (UI components)

---
*Phase: 01-innehallsgrund*
*Completed: 2026-04-10*
