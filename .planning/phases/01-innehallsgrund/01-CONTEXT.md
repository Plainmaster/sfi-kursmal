# Phase 1: Innehallsgrund - Context

**Gathered:** 2026-04-10
**Status:** Ready for planning

<domain>
## Phase Boundary

All course content exists in stable JSON data files that the teacher can update without changing code. This phase delivers: JSON schema design, simplified "Jag kan..." course goals for courses B/C/D across all five skill domains, icon and color assignments per skill domain, and theme-to-goal mapping.

</domain>

<decisions>
## Implementation Decisions

### JSON Schema Design
- **D-01:** One JSON file per course: `kurs-b.json`, `kurs-c.json`, `kurs-d.json` in `src/data/`. Teacher edits one file at a time.
- **D-02:** Goal ID format: `{COURSE}-{DOMAIN}-{NN}` (e.g., `B-LASA-01`, `C-HORA-03`). Stable across curriculum updates.
- **D-03:** Each goal object has: `id`, `text` (the "Jag kan..." statement), `kursplan_year` (integer, e.g. 2018), `themes` (string array).
- **D-04:** Goals grouped by skill domain within each file. Top-level structure: `{ kursplan_year: 2018, domains: { horforstaelse: { goals: [...] }, lasforstaelse: { goals: [...] }, ... } }`.

### Course Goal Text (Kursmalstext)
- **D-05:** Follow the existing "Jag kan..." format from the kurs B material. Each goal is a concrete, checkable statement.
- **D-06:** Simplify Skolverket's official criteria text to plain Swedish appropriate for each course level (B = simplest, D = most complex language).
- **D-07:** Same structural format for B, C, and D. Complexity increases in the text content, not in the data structure.
- **D-08:** Use the existing `Kursmal och checklista for elever.md` as the primary source for kurs B goals. Kurs C and D goals must be authored following the same pattern based on Skolverket's official criteria.

### Theme Mapping (Tema-koppling)
- **D-09:** Many-to-many relationship: each goal has a `themes` array with 0-N theme strings.
- **D-10:** Theme values match the 7 arshjul themes exactly: `relationer`, `miljo`, `bostad`, `arbete-och-studier`, `fritid-och-halsa`, `hogtider`, `samhalle`.
- **D-11:** Not all goals require a theme tag. Generic language skills (e.g., "Jag kan skriva fem nya ord varje vecka") may have an empty themes array.

### Design System Foundation
- **D-12:** Five distinct colors assigned to the five skill domains. Bright, friendly palette inspired by the tree material.
- **D-13:** Lucide icon assignments: horforstaelse = Ear, lasforstaelse = BookOpen, muntlig interaktion = MessageCircle, muntlig produktion = Mic, skriftlig fardighet = PenLine.
- **D-14:** Color and icon mappings stored in a separate `design-tokens.json` (or equivalent) in `src/data/` so they can be updated independently from goal content.

### Claude's Discretion
- Exact hex color values for the 5 skill domain colors (should be high-contrast, colorblind-friendly, and visually warm/inviting)
- JSON file indentation and formatting conventions
- Whether to include a JSON schema validation file (recommended but optional)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Existing Course Material
- `Kursmal och checklista for elever.md` -- Primary source for kurs B goals and "Min plan" checklist format
- `Forvantansdokumentet.md` -- Student expectations document (context for tone and language level)
- `Arshjul for sfi 2 kurs B, C och D .md` -- The 7 yearly themes that goals must map to

### Project Specs
- `.planning/REQUIREMENTS.md` -- Requirements KURS-01 through KURS-06 and DESIGN-05
- `.planning/ROADMAP.md` -- Phase 1 success criteria (5 items)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- No source code exists yet. This is the first phase.

### Established Patterns
- No patterns established. This phase sets the data foundation.

### Integration Points
- JSON files in `src/data/` will be imported by Astro at build time (Phase 2)
- Design tokens will be consumed by Tailwind configuration and Astro components (Phase 2)

</code_context>

<specifics>
## Specific Ideas

- The existing kurs B material uses a mix of Skolverket's official text and simplified "Du kan..." / "Jag kan..." statements. The JSON should contain only the simplified "Jag kan..." versions.
- The "Min plan" section (with "Jag ska..." items) is Phase 3 scope, not Phase 1. Phase 1 focuses on course goals ("Jag kan..."), not training plans ("Jag ska...").
- Five skill domains (not four): horforstaelse, lasforstaelse, muntlig interaktion, muntlig produktion, skriftlig fardighet. The existing material sometimes merges "muntligt" into one category -- the JSON must keep all five separate per Skolverket's structure.

</specifics>

<deferred>
## Deferred Ideas

None -- discussion stayed within phase scope

</deferred>

---

*Phase: 01-innehallsgrund*
*Context gathered: 2026-04-10*
