# Phase 2: Interaktiv checklista - Context

**Gathered:** 2026-04-10
**Status:** Ready for planning

<domain>
## Phase Boundary

A complete interactive Astro web application where SFI students can see their course goals with visual support, check off achieved competencies, and switch between courses B, C, and D. This phase scaffolds the Astro project and delivers the full interactive product: tab navigation, goal display grouped by skill domain, checkbox persistence via localStorage, save feedback, and responsive mobile-first layout.

</domain>

<decisions>
## Implementation Decisions

### Project Scaffolding
- **D-01:** Scaffold Astro 6 project with Tailwind CSS 4 integration per CLAUDE.md stack recommendation. Install lucide-astro for icons and @fontsource/inter for typography.
- **D-02:** Project root is the current directory. `src/data/` already exists with JSON files from Phase 1.

### Tab Navigation and Course Switching
- **D-03:** Tabs at the TOP of the page, always visible (sticky). Three tabs labeled "Kurs B", "Kurs C", "Kurs D" -- full course names, not just letters. Students need clear labels.
- **D-04:** Tab switching uses vanilla JS (no page reload). When switching tabs, scroll to top of content area. Active tab gets a colored underline matching the course.
- **D-05:** Default tab is "Kurs B" (the first course most spar 2 students encounter).
- **D-06:** Tab state is NOT persisted in localStorage -- students should consciously choose their course each visit.

### Goal Card Layout and Visual Style
- **D-07:** Goals grouped by skill domain with colored section headers. Each domain section has: the domain icon (from design-tokens.json), the domain label, and a colored background/border matching the domain color.
- **D-08:** Each goal is a checkbox row: checkbox + "Jag kan..." text. Simple, not cards -- cards add visual noise for this audience. Clean list within each domain section.
- **D-09:** Domain sections are expanded by default (no accordion). Students should see all goals immediately without extra interaction.
- **D-10:** Colorful style: domain header bars use the design-tokens colors as background. White text on colored background. Inspired by the tree material's bright, friendly look.
- **D-11:** Icons always paired with text labels per DESIGN-04. Icon size appropriate for mobile touch (at least 24px).

### Checkbox Feedback and Saved Indicator
- **D-12:** When a checkbox is toggled, show a brief inline "Sparat!" text near the checkbox that fades after 1.5 seconds. No toast/popup -- too intrusive for rapid checking.
- **D-13:** Each domain section shows a progress count: "3 av 5 avklarade" below the domain header. Updates immediately on check/uncheck.
- **D-14:** localStorage key format: `sfi-checklist-{course}` (e.g., `sfi-checklist-B`). Value is JSON object mapping goal IDs to boolean. Saves on every toggle.

### Reset Flow and Data Safety
- **D-15:** Reset button at the bottom of each course tab. Labeled "Borja om" (Start over) with a subdued style (not primary button).
- **D-16:** Two-step confirmation: first click shows "Ar du saker? Alla markeringar for Kurs {X} forsvinner." with "Ja, borja om" and "Avbryt" buttons.
- **D-17:** Reset is per-course, not global. Students may be on different courses and should only reset one at a time.
- **D-18:** No browser close warning -- localStorage persists automatically. Warning would confuse students.

### Responsive Design
- **D-19:** Mobile-first: designed for 375px viewport as primary. Desktop is a wider version of the same layout (max-width container, centered).
- **D-20:** Touch targets minimum 44px height for checkboxes and tabs per WCAG.
- **D-21:** Font size minimum 16px for body text to prevent iOS zoom on focus.

### Claude's Discretion
- Exact Tailwind configuration and theme setup
- Astro page structure (single page with client-side tabs vs multi-page)
- Specific animation/transition details for the "Sparat!" indicator
- Whether to use Astro islands or plain script tags for interactivity
- Exact spacing, padding, and margin values

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 1 Outputs
- `src/data/design-tokens.json` -- Domain icons, colors, labels (5 domains)
- `src/data/kurs-b.json` -- 24 goals, CEFR A1
- `src/data/kurs-c.json` -- 25 goals, CEFR A2
- `src/data/kurs-d.json` -- 24 goals, CEFR B1

### Project Specs
- `.planning/REQUIREMENTS.md` -- INTER-01, INTER-02, INTER-04, INTER-05, DESIGN-01 through DESIGN-04
- `.planning/ROADMAP.md` -- Phase 2 success criteria (5 items)
- `CLAUDE.md` -- Technology stack (Astro 6, Tailwind 4, lucide-astro, Inter font, vanilla JS)

### Existing Course Material
- `Kursmal och checklista for elever.md` -- Visual reference for checklist style
- `Arshjul for sfi 2 kurs B, C och D .md` -- Theme context

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `src/data/design-tokens.json` -- ready to import for domain colors/icons
- `src/data/kurs-{b,c,d}.json` -- ready to import for goal rendering

### Established Patterns
- JSON data files use consistent schema: `{ course, kursplan_year, cefr, domains: { [key]: { goals: [...] } } }`
- Domain keys are ASCII (no diacritics): horforstaelse, lasforstaelse, muntlig-interaktion, muntlig-produktion, skriftlig-fardighet
- Labels with diacritics are in design-tokens.json

### Integration Points
- Astro imports JSON at build time via `import`
- Design tokens provide the icon name (Lucide component name), color hex, and label for each domain
- Goal IDs (B-HORA-01 etc.) are the keys for localStorage checkbox state

</code_context>

<specifics>
## Specific Ideas

- The site should feel warm and inviting, not clinical. Bright colors from the tree material style.
- Students primarily use mobile phones -- every interaction must work well with thumb navigation.
- "Sparat!" feedback is important because students may not trust that their progress is saved without a server.
- The progress count per domain ("3 av 5") gives students a sense of accomplishment and motivation.

</specifics>

<deferred>
## Deferred Ideas

- "Min plan" section with "Jag ska..." items (Phase 3 scope)
- Print view via @media print (Phase 3 scope)
- Accordion/collapsible domain sections (v2 -- TILLAG-04)
- Progress indicator visualization like progress bars (v2 -- TILLAG-01)

</deferred>

---

*Phase: 02-interaktiv-checklista*
*Context gathered: 2026-04-10*
