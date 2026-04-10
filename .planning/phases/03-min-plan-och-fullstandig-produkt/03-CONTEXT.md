# Phase 3: Min Plan och fullständig produkt - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning
**Mode:** auto (all gray areas auto-selected with recommended defaults)

<domain>
## Phase Boundary

Add a "Min plan" section where students choose what to practice each period ("Jag ska..."-items) with localStorage persistence, and add a print stylesheet so the teacher can print the checklist and plan as a classroom handout. This phase completes the product before deployment.

</domain>

<decisions>
## Implementation Decisions

### Min Plan Structure
- **D-01:** "Min plan" is a separate section/tab alongside the course checklist. Accessed via a new tab or a section below the checklist — NOT a separate page. Keep the single-page architecture from Phase 2.
- **D-02:** Uses "Jag ska..." format (not "Jag kan...") per the existing source material. These are commitments/goals the student sets for themselves.
- **D-03:** Pre-filled suggestions per skill domain based on the existing "Min plan" material: Läsa, Skriva, Höra, Tala (4 categories matching the source). Each has 5-6 pre-written suggestions with checkboxes.
- **D-04:** Include 2-3 blank rows per domain where students can write their own "Jag ska..." goals. Use editable text inputs.
- **D-05:** "Min plan" is course-independent — it's about HOW the student will practice, not course-specific goals. One plan shared across B/C/D.
- **D-06:** localStorage key: `sfi-minplan`. Stores checked items and custom text inputs as JSON. Same persistence pattern as the checklist.

### Min Plan Visual Design
- **D-07:** Use the same domain color scheme from design-tokens. Map: Läsa=blue (lasforstaelse), Skriva=red (skriftlig-fardighet), Höra=amber (horforstaelse), Tala=green (muntlig-interaktion).
- **D-08:** Same component style as the checklist — colored domain headers with icons, checkbox rows below. Reuse DomainSection and GoalCheckbox components or create minimal variants.
- **D-09:** Header text: "Min plan — Vad ska jag träna?" with brief intro text explaining the purpose.

### Navigation
- **D-10:** Add "Min plan" as a 4th element in navigation. Could be a tab next to B/C/D or a separate button/link below the tabs. Visually distinct from the course tabs since it's a different kind of content.
- **D-11:** Tab colors: keep B/C/D as cyan/violet/rose. "Min plan" gets a neutral or warm color (e.g., emerald or orange) to distinguish it from course content.

### Print Stylesheet
- **D-12:** Use `@media print` CSS rules in global.css. No separate print page needed.
- **D-13:** Print hides: tab navigation, reset buttons, expand/collapse toggles, "Sparat!" indicators, Lexin audio buttons.
- **D-14:** Print shows: the currently active course's checklist with all goals visible (expanded), domain headers with icons (grayscale-safe), checked/unchecked state visible.
- **D-15:** Print also shows: "Min plan" section with checked items and custom text.
- **D-16:** Page title and student info area at top of print: "SFI Spår 2 — Kurs [B/C/D] — Kursmål" with a line for student name and date.
- **D-17:** Print-friendly: use black/white/gray, ensure checkboxes render as visible squares, adequate font size (12pt minimum).

### Claude's Discretion
- Whether "Min plan" data goes in a JSON file or is hardcoded in a component
- Exact layout of custom text input rows
- Print page breaks between sections
- Whether to add a "Skriv ut" button that triggers window.print()

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 2 Outputs (reuse patterns)
- `src/components/DomainSection.astro` — Domain header + goal list pattern to reuse
- `src/components/GoalCheckbox.astro` — Checkbox + expand pattern
- `src/components/TabNav.astro` — Tab navigation to extend
- `src/pages/index.astro` — Single-page architecture with client JS
- `src/styles/global.css` — Tailwind theme with domain colors

### Source Material
- `Kursmål och checklista för elever.md` — "Min plan" section (lines 36-88) with "Jag ska..." items per domain

### Project Specs
- `.planning/REQUIREMENTS.md` — INTER-03, DESIGN-06
- `.planning/ROADMAP.md` — Phase 3 success criteria

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `DomainSection.astro` — colored header + list container, can be reused for Min plan domains
- `GoalCheckbox.astro` — checkbox + text + expand, can be adapted for "Jag ska..." items
- `TabNav.astro` — sticky tabs, extend with 4th "Min plan" tab
- localStorage pattern in index.astro — loadState/saveState/updateProgressCounts already established
- `design-tokens.json` — domain colors and icons ready to map

### Established Patterns
- Single-page Astro with `define:vars` for client data injection
- Delegated event handlers for dynamic content
- `sfi-checklist-{course}` localStorage key pattern

### Integration Points
- TabNav needs a 4th tab
- index.astro script needs Min plan load/save/toggle logic
- global.css needs @media print rules

</code_context>

<specifics>
## Specific Ideas

- The existing source material has 4 domains for Min plan (Läsa, Skriva, Höra, Tala) — these map to the existing 5 skill domains but consolidated (muntlig-interaktion + muntlig-produktion = Tala).
- Each domain has 5 pre-filled "Jag ska..." items plus a blank "... (Jag ska)" for the student to fill in.
- "Min plan" is about study habits and practice strategies, not about competency goals. It's future-oriented ("I will...") vs the checklist ("I do...").
- Print should produce something a teacher would be happy to hand out in class or put on the wall.

</specifics>

<deferred>
## Deferred Ideas

- Progress visualization (bars, charts) — v2 TILLAG-01
- Accordion/collapsible sections — v2 TILLAG-04
- Offline/PWA support — v2 TILLAG-02

</deferred>

---

*Phase: 03-min-plan-och-fullstandig-produkt*
*Context gathered: 2026-04-11 via auto mode*
