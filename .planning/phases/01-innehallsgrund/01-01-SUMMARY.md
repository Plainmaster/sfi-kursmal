---
phase: 01-innehallsgrund
plan: 01
subsystem: data
tags: [json, sfi, kursmal, design-tokens, swedish-education]

# Dependency graph
requires: []
provides:
  - "Design tokens (icon, color, label) for 5 skill domains"
  - "Kurs B course goals (24 'Jag kan...' statements) across all 5 domains"
  - "Canonical domain keys and ID format pattern for kurs C and D"
affects: [01-02, 02-innehallsgrund, phase-2]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "One JSON file per course in src/data/"
    - "Domain keys: ASCII-only, hyphen-separated (horforstaelse, muntlig-interaktion)"
    - "Goal ID format: {COURSE}-{DOMAIN}-{NN} (e.g., B-HORA-01)"
    - "Design tokens separate from content data"

key-files:
  created:
    - src/data/design-tokens.json
    - src/data/kurs-b.json
  modified: []

key-decisions:
  - "Used RESEARCH.md recommended color palette (amber, blue, green, violet, red) for WCAG AA compliance"
  - "kursplan_year set to 2018 per plan specification (may need teacher confirmation)"
  - "Theme tags assigned conservatively -- generic language skills get empty themes array"

patterns-established:
  - "Goal text always starts with 'Jag kan' (first person singular)"
  - "Domain keys are the canonical join key between all JSON files"
  - "Theme values use only the 7 canonical arshjul strings without diacritics"
  - "4-8 goals per domain per course"

requirements-completed: [KURS-01, KURS-02, KURS-03, KURS-04, KURS-05, KURS-06, DESIGN-05]

# Metrics
duration: 2min
completed: 2026-04-10
---

# Phase 1 Plan 1: Design Tokens and Kurs B Data Summary

**Design token file with 5 color-coded skill domains and 24 simplified "Jag kan..." course goals for SFI kurs B**

## Performance

- **Duration:** 2 min
- **Started:** 2026-04-10T18:53:30Z
- **Completed:** 2026-04-10T18:55:20Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments
- Created design-tokens.json with icon (Lucide), color (WCAG AA palette), and Swedish labels for all 5 skill domains
- Authored 24 concrete "Jag kan..." goals for kurs B: 5 horforstaelse, 5 lasforstaelse, 5 muntlig-interaktion, 4 muntlig-produktion, 5 skriftlig-fardighet
- Established canonical ID format (B-XXXX-NN), domain keys, and theme mapping pattern for kurs C and D to follow

## Task Commits

Each task was committed atomically:

1. **Task 1: Create design-tokens.json and kurs-b.json skeleton** - `031f457` (feat)
2. **Task 2: Author kurs B goals with themes** - `aeb9e78` (feat)

## Files Created/Modified
- `src/data/design-tokens.json` - Icon, color, and label mappings for 5 skill domains (Ear/amber, BookOpen/blue, MessageCircle/green, Mic/violet, PenLine/red)
- `src/data/kurs-b.json` - 24 course B goals with stable IDs, kursplan_year 2018, and conservative theme assignments

## Decisions Made
- Used the color palette from RESEARCH.md (amber #D97706, blue #2563EB, green #16A34A, violet #7C3AED, red #DC2626) which targets WCAG AA contrast ratios
- Set kursplan_year to 2018 as specified in plan -- teacher should confirm this matches their current Skolverket document
- Assigned themes conservatively: only 8 of 24 goals have theme tags; generic language skills get empty arrays

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered
None.

## User Setup Required
None -- no external service configuration required.

## Next Phase Readiness
- Design tokens and kurs B data are complete and ready for consumption
- Kurs C and D (plan 01-02) can follow the exact same schema and ID pattern
- Domain keys match between both files (verified by automated script)
- All goal IDs are stable and sequential -- safe for localStorage key generation in Phase 2

---
*Phase: 01-innehallsgrund*
*Completed: 2026-04-10*
