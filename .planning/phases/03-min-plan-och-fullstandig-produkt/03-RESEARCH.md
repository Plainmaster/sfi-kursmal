# Phase 03: Min Plan och fullstandig produkt - Research

**Researched:** 2026-04-10
**Domain:** Astro component extension, localStorage persistence, CSS print media
**Confidence:** HIGH

## Summary

This phase extends the existing Phase 2 single-page Astro app with two features: (1) a "Min plan" section where students select practice strategies via checkboxes, and (2) a `@media print` stylesheet for classroom handouts. Both features build directly on established patterns -- the component architecture (DomainSection, GoalCheckbox, TabNav), the localStorage persistence pattern, and the Tailwind-based styling already in place.

No new libraries or technologies are needed. The work is pure extension of existing code: a new tab in navigation, a new panel with domain sections, JS for persistence, and CSS print rules in global.css. The "Jag ska..." content comes from the source material document and needs to be structured into a JSON data file (or hardcoded in a component -- Claude's discretion per D-04).

**Primary recommendation:** Reuse existing component patterns with minimal adaptation. Create a MinPlanPanel component parallel to CoursePanel. Add print CSS as a single `@media print` block in global.css.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- D-01: "Min plan" is a separate tab alongside B/C/D, NOT a separate page. Single-page architecture preserved.
- D-02: Uses "Jag ska..." format (commitments), not "Jag kan..." (competencies).
- D-03: Pre-filled suggestions per domain (Lasa, Skriva, Hora, Tala -- 4 categories). Each has 5-6 items.
- D-04: Include 2-3 blank rows per domain for custom student goals (editable text inputs).
- D-05: "Min plan" is course-independent -- one plan shared across B/C/D.
- D-06: localStorage key: `sfi-minplan`. JSON format. Same persistence pattern as checklist.
- D-07: Domain color mapping: Lasa=blue (lasforstaelse), Skriva=red (skriftlig-fardighet), Hora=amber (horforstaelse), Tala=green (muntlig-interaktion).
- D-08: Same component style as checklist -- colored domain headers with icons, checkbox rows.
- D-09: Header: "Min plan -- Vad ska jag trana?" with brief intro text.
- D-10: Add "Min plan" as 4th navigation element. Visually distinct from course tabs.
- D-11: Tab colors: B=cyan, C=violet, D=rose, Min plan=neutral/warm (e.g., emerald or orange).
- D-12: Print CSS via `@media print` in global.css. No separate print page.
- D-13: Print hides: tab nav, reset buttons, expand/collapse toggles, "Sparat!" indicators, Lexin audio buttons.
- D-14: Print shows: active course checklist with all goals expanded, domain headers with icons (grayscale-safe).
- D-15: Print also shows: "Min plan" section with checked items and custom text.
- D-16: Print header: "SFI Spar 2 -- Kurs [B/C/D] -- Kursmal" with lines for student name and date.
- D-17: Print-friendly: black/white/gray, visible checkbox squares, 12pt minimum font.

### Claude's Discretion
- Whether "Min plan" data goes in a JSON file or is hardcoded in a component
- Exact layout of custom text input rows
- Print page breaks between sections
- Whether to add a "Skriv ut" button that triggers window.print()

### Deferred Ideas (OUT OF SCOPE)
- Progress visualization (bars, charts) -- v2 TILLAG-01
- Accordion/collapsible sections -- v2 TILLAG-04
- Offline/PWA support -- v2 TILLAG-02
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| INTER-03 | "Min plan" -- eleven valjer vad de ska trana (lasa, skriva, hora, tala) med checkboxar | Min plan data structure, component reuse patterns, localStorage persistence pattern |
| DESIGN-06 | Utskriftsvy via @media print for klassrumsanvandning | CSS print media patterns, hiding interactive elements, grayscale-safe domain headers |
</phase_requirements>

## Standard Stack

No new libraries needed. This phase uses only what Phase 2 already installed.

### Core (already installed)
| Library | Version | Purpose | Status |
|---------|---------|---------|--------|
| Astro | 6.x | Site framework | Already installed [VERIFIED: existing package.json] |
| Tailwind CSS | 4.x | Styling + print utilities | Already installed [VERIFIED: global.css @import] |
| lucide-astro | latest | Icons (Ear, BookOpen, MessagesSquare, PenLine) | Already installed [VERIFIED: DomainSection.astro imports] |
| Vanilla JS | browser native | localStorage persistence, tab switching | No install needed |

### Supporting
None new required.

## Architecture Patterns

### Existing Structure (extend, don't restructure)
```
src/
  components/
    TabNav.astro          # ADD: 4th "Min plan" tab
    CoursePanel.astro      # REFERENCE: pattern for MinPlanPanel
    DomainSection.astro    # REUSE: domain header + goals container
    GoalCheckbox.astro     # ADAPT: for "Jag ska..." items (simpler -- no expand/examples)
    ResetButton.astro      # Existing, no changes needed
    MinPlanPanel.astro     # NEW: Min plan panel component
    PlanCheckbox.astro     # NEW: simpler checkbox for plan items (no expand button)
    PlanCustomRow.astro    # NEW: editable text input row
  pages/
    index.astro            # EXTEND: add MinPlanPanel, add min-plan JS logic
  data/
    min-plan.json          # NEW (recommended): structured plan items per domain
    design-tokens.json     # EXISTING: domain colors and icons to reuse
  styles/
    global.css             # EXTEND: add @media print block
```

### Pattern 1: Min Plan Data Structure
**What:** JSON file with 4 domains, each containing 5 pre-filled "Jag ska..." items [VERIFIED: source material has exactly this structure]
**Recommendation:** Use a JSON data file (like kurs-b.json pattern) rather than hardcoding. This follows the project constraint that course goals live in separate data structures for easy updating.

```json
{
  "domains": {
    "lasforstaelse": {
      "items": [
        { "id": "plan-lasa-01", "text": "lasa bocker pa latt svenska" },
        { "id": "plan-lasa-02", "text": "lasa reklam fran affarer" },
        { "id": "plan-lasa-03", "text": "lasa ord och meningar i svenska tidningar" },
        { "id": "plan-lasa-04", "text": "lasa information pa anslagstavlor" },
        { "id": "plan-lasa-05", "text": "lasa vad jag har skrivit pa kursen" }
      ]
    },
    "skriftlig-fardighet": {
      "items": [
        { "id": "plan-skriva-01", "text": "skriva dagbok varje dag" },
        { "id": "plan-skriva-02", "text": "skriva fem nya ord varje vecka" },
        { "id": "plan-skriva-03", "text": "skriva fem meningar varje vecka" },
        { "id": "plan-skriva-04", "text": "kopiera en text varje vecka" },
        { "id": "plan-skriva-05", "text": "skriva ord pa mitt forstasprak och oversatta till svenska" }
      ]
    },
    "horforstaelse": {
      "items": [
        { "id": "plan-hora-01", "text": "titta och lyssna pa svensk tv" },
        { "id": "plan-hora-02", "text": "lyssna pa svensk radio varje dag" },
        { "id": "plan-hora-03", "text": "lyssna pa personer som pratar svenska" },
        { "id": "plan-hora-04", "text": "lyssna pa horforstaeelser pa natet" },
        { "id": "plan-hora-05", "text": "lyssna pa information, till exempel pa en tagstation" }
      ]
    },
    "muntlig-interaktion": {
      "items": [
        { "id": "plan-tala-01", "text": "prata svenska med personal i affarer" },
        { "id": "plan-tala-02", "text": "prata svenska med mig sjalv nar jag ar ensam" },
        { "id": "plan-tala-03", "text": "saga tva nya meningar varje vecka" },
        { "id": "plan-tala-04", "text": "ga till ett sprakcafe och prata svenska" },
        { "id": "plan-tala-05", "text": "fraga en person om nagot pa svenska" }
      ]
    }
  }
}
```
[VERIFIED: content extracted from "Kursmal och checklista for elever.md" lines 36-85]

**Key mapping decision (D-07):** Min plan uses 4 domains, not the checklist's 5-7. The mapping to existing design-tokens:
- Lasa -> `lasforstaelse` (blue, BookOpen icon)
- Skriva -> `skriftlig-fardighet` (red, PenLine icon)
- Hora -> `horforstaelse` (amber, Ear icon)
- Tala -> `muntlig-interaktion` (green, MessagesSquare icon)

### Pattern 2: Min Plan localStorage
**What:** Single key `sfi-minplan` storing both checked pre-filled items and custom text inputs [VERIFIED: D-06]
**Structure:**
```javascript
// localStorage key: sfi-minplan
{
  "checked": {
    "plan-lasa-01": true,
    "plan-hora-03": true
  },
  "custom": {
    "lasforstaelse-custom-1": "lasa tidningen varje morgon",
    "lasforstaelse-custom-2": "",
    "horforstaelse-custom-1": "lyssna pa poddar"
  }
}
```
[ASSUMED: structure design -- follows the established pattern from Phase 2 but adds custom text field]

### Pattern 3: Tab Navigation Extension
**What:** Add 4th tab to TabNav.astro for "Min plan"
**Key difference:** Min plan is NOT a course -- it's a cross-cutting section. It should visually differ from B/C/D tabs.
**Implementation:** Add to the tabs array in TabNav.astro. Use `data-course="plan"` attribute. The `switchTab()` function in index.astro needs to handle the "plan" case (show `panel-plan`, hide course panels).

```astro
// In TabNav.astro tabs array, add:
{ course: "plan", label: "Min plan", color: "border-emerald-600 text-emerald-700", activeColor: "bg-emerald-600" }
```
[ASSUMED: emerald color choice -- D-11 suggests emerald or orange; emerald feels more aligned with a "growth/plan" concept]

### Pattern 4: Print Stylesheet
**What:** `@media print` CSS in global.css
**Key rules:**
```css
@media print {
  /* Hide interactive elements */
  nav, .course-tab, [data-reset], [data-confirm],
  .expand-btn, .saved-indicator, [data-lexin-word],
  .print-hide { display: none !important; }

  /* Show all panels and expand all details */
  .course-panel { display: block !important; }
  .course-panel.hidden { display: none !important; }
  .goal-details { display: block !important; }

  /* Typography */
  body { font-size: 12pt; color: black; background: white; }

  /* Checkbox visibility */
  input[type="checkbox"] {
    -webkit-appearance: auto;
    appearance: auto;
    width: 16px; height: 16px;
  }

  /* Domain headers -- grayscale-safe */
  [class*="bg-domain-"] {
    background: #444 !important;
    color: white !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* Page header for student info */
  .print-header { display: block !important; }
}
```
[ASSUMED: specific CSS selectors -- will need refinement based on actual DOM]

### Anti-Patterns to Avoid
- **Separate page for Min plan:** D-01 explicitly locks single-page architecture. No new Astro page.
- **Course-specific Min plan:** D-05 says one plan shared across B/C/D. Don't create separate plan states per course.
- **Complex custom input:** The blank rows should be simple `<input type="text">` with a checkbox. Don't build a rich text editor or auto-save-on-type debouncer -- just save on blur or on checkbox change.
- **Print JavaScript:** Don't use JS for print layout. Pure CSS `@media print` is the right approach per D-12.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Print styling | Custom print JS / PDF generation | `@media print` CSS | Browser print is well-supported, zero dependencies, teacher just hits Ctrl+P |
| Checkbox state | Custom state management | Simple localStorage JSON | Pattern already established in Phase 2 |
| Domain color theming | Inline styles | Existing Tailwind @theme variables | Already defined in global.css and design-tokens.json |
| Responsive layout | Media queries | Tailwind responsive utilities | Already in use across all Phase 2 components |

## Common Pitfalls

### Pitfall 1: Print Hides Active Panel Only
**What goes wrong:** Print CSS shows all three course panels (B, C, D) instead of only the active one.
**Why it happens:** The `hidden` class is toggled by JS, but print CSS might override `display` on `.course-panel`.
**How to avoid:** In print CSS, only override `.course-panel.hidden` carefully. Keep the JS-applied `hidden` class respected. Or use a print-specific class that marks the active course.
**Warning signs:** Print preview shows all 3 courses stacked.

### Pitfall 2: localStorage Key Collision
**What goes wrong:** Min plan data overwrites checklist data or vice versa.
**Why it happens:** Using wrong key prefix.
**How to avoid:** D-06 locks the key as `sfi-minplan` (not `sfi-checklist-plan`). Keep them distinct.

### Pitfall 3: Custom Text Inputs Not Persisting
**What goes wrong:** Student types custom goals but they disappear on reload.
**Why it happens:** Text inputs need explicit save-on-change (blur or input event), unlike checkboxes which have a clear change event.
**How to avoid:** Save on `blur` event for text inputs. Also save on `input` event with a simple approach (no debounce needed -- the data is tiny).

### Pitfall 4: Print Checkbox Rendering
**What goes wrong:** Checkboxes appear as empty rectangles or disappear entirely in print.
**Why it happens:** Browser default checkbox rendering in print varies. Custom-styled checkboxes (accent-color, custom SVG) may not print.
**How to avoid:** Use `appearance: auto` in print CSS to force native checkbox rendering. Test in Chrome print preview.

### Pitfall 5: Tab State and Print
**What goes wrong:** User prints from "Min plan" tab but expects to see both checklist AND plan.
**Why it happens:** D-14 says print shows "currently active course's checklist" AND D-15 says "Min plan section."
**How to avoid:** Print should show the last-viewed course panel (not Min plan tab panel) PLUS the Min plan section. May need a hidden print-header element and logic to track which course was last active.
**Warning signs:** Print from Min plan tab shows only the plan, no checklist.

### Pitfall 6: Domain Mismatch Between Checklist and Min Plan
**What goes wrong:** Min plan has 4 domains (Lasa, Skriva, Hora, Tala) but checklist has 5-7 (adds muntlig-produktion, uttal, grammatik).
**Why it happens:** Source material consolidates speaking into one "Tala" category.
**How to avoid:** This is intentional per the source material. Min plan maps to 4 of the existing domain keys. Don't try to force 1:1 mapping with all checklist domains.

## Code Examples

### Reusing DomainSection for Min Plan
The existing DomainSection component can be reused directly if the Min plan items follow the same `{ id, text }` goal structure. The component accepts `domainKey`, `label`, `labelShort`, `icon`, `colorClass`, `goals`, and `course`.

For Min plan, `course` could be set to `"plan"` to namespace checkbox data-attributes differently from course checkboxes. However, since Min plan uses a different localStorage key (`sfi-minplan` vs `sfi-checklist-{course}`), the JS handler needs to distinguish plan checkboxes from course checkboxes.

**Option A -- Reuse DomainSection directly:**
Set `course="plan"` and handle `data-course="plan"` specially in JS. Downside: GoalCheckbox has expand button and example loading that Min plan doesn't need.

**Option B -- Create MinPlanSection (recommended):**
A simpler variant of DomainSection without expand buttons, with custom text input rows added at the bottom. Keeps components focused and avoids conditional complexity.

```astro
// MinPlanSection.astro -- simplified DomainSection for Min plan
---
interface Props {
  domainKey: string;
  label: string;
  icon: string;
  colorClass: string;
  items: Array<{ id: string; text: string }>;
  customRowCount: number;
}
const { domainKey, label, icon, colorClass, items, customRowCount = 2 } = Astro.props;
---
<section class="mb-6">
  <div class={`${colorClass} rounded-t-lg px-4 py-3 flex items-center gap-2`}>
    <IconComponent size={24} class="text-white" />
    <h2 class="text-white font-semibold text-lg">{label}</h2>
  </div>
  <div class="bg-white rounded-b-lg border border-t-0 border-gray-200">
    {items.map(item => (
      <label class="flex items-center gap-3 py-2 px-3 min-h-[44px] cursor-pointer border-b border-gray-100">
        <input type="checkbox" class="w-6 h-6 shrink-0" data-plan-id={item.id} />
        <span class="text-base">Jag ska {item.text}</span>
      </label>
    ))}
    {Array.from({ length: customRowCount }).map((_, i) => (
      <label class="flex items-center gap-3 py-2 px-3 min-h-[44px] border-b border-gray-100">
        <input type="checkbox" class="w-6 h-6 shrink-0" data-plan-custom={`${domainKey}-custom-${i+1}`} />
        <span class="text-base shrink-0">Jag ska</span>
        <input type="text" class="flex-1 border-b border-gray-300 focus:border-gray-500 outline-none text-base"
          data-plan-text={`${domainKey}-custom-${i+1}`} placeholder="..." />
      </label>
    ))}
  </div>
</section>
```
[ASSUMED: exact component API -- follows existing pattern from DomainSection.astro]

### Print CSS Pattern
```css
@media print {
  /* Hide all interactive/nav elements */
  nav, [data-reset], [data-confirm],
  .expand-btn, .saved-indicator,
  [data-lexin-word], .print-hide {
    display: none !important;
  }

  /* Force show the print header (hidden on screen) */
  .print-header {
    display: block !important;
  }

  /* Make Min plan always visible in print */
  #panel-plan {
    display: block !important;
  }

  /* Base print typography */
  body {
    font-size: 12pt;
    color: #000;
    background: #fff;
  }

  /* Ensure checkboxes render */
  input[type="checkbox"] {
    -webkit-appearance: checkbox;
    appearance: checkbox;
    print-color-adjust: exact;
  }
}
```
[ASSUMED: specific selectors will need tuning to match final DOM]

### Print Header (hidden on screen, visible in print)
```astro
<div class="print-header hidden">
  <h1 class="text-xl font-bold">SFI Spar 2 -- Kurs <span class="print-course">B</span> -- Kursmal</h1>
  <div class="flex gap-8 mt-2 mb-4 border-b border-gray-300 pb-2">
    <p>Namn: ____________________</p>
    <p>Datum: ____________________</p>
  </div>
</div>
```
[ASSUMED: exact markup -- follows D-16 requirements]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | localStorage structure with `checked` + `custom` sub-objects for Min plan | Architecture Patterns | LOW -- easy to restructure, no migration needed |
| A2 | Emerald color for Min plan tab | Architecture Patterns | LOW -- purely aesthetic, trivially changed |
| A3 | Creating separate MinPlanSection component vs reusing DomainSection | Code Examples | LOW -- either approach works, recommendation is for cleaner code |
| A4 | Print CSS selectors | Code Examples | LOW -- will be refined during implementation based on actual DOM |
| A5 | Print shows last-active course + Min plan together | Pitfalls | MEDIUM -- D-14/D-15 imply both visible, but behavior when printing from Min plan tab needs clarification |

## Open Questions

1. **Print from Min plan tab -- which course shows?**
   - What we know: D-14 says print shows "currently active course's checklist." D-15 says print also shows Min plan.
   - What's unclear: If the user is on the Min plan tab (no course active), should the print show the last-viewed course, or prompt the user?
   - Recommendation: Track last-active course in a variable. When printing from Min plan tab, show that last course. Default to Kurs B if no course was viewed.

2. **"Skriv ut" button -- add one?**
   - What we know: Claude's discretion per CONTEXT.md.
   - Recommendation: Yes, add a simple "Skriv ut" button that calls `window.print()`. Place it in the page header or footer area. Hide it in print CSS. Low effort, high usability for teachers who may not know Ctrl+P.

3. **Custom text input persistence timing**
   - What we know: Checkboxes save on `change` event. Text inputs could save on `blur`, `input`, or both.
   - Recommendation: Save on `input` event (immediate). The data is tiny (a few strings). No debounce needed.

## Sources

### Primary (HIGH confidence)
- `src/pages/index.astro` -- existing tab switching, localStorage, and checkbox patterns
- `src/components/DomainSection.astro` -- domain section component pattern
- `src/components/GoalCheckbox.astro` -- checkbox component pattern
- `src/components/TabNav.astro` -- tab navigation structure
- `src/data/design-tokens.json` -- domain color/icon mapping
- `src/styles/global.css` -- Tailwind theme configuration
- `Kursmal och checklista for elever.md` -- source material for Min plan items (lines 36-85)

### Secondary (MEDIUM confidence)
- CSS `@media print` is a well-established web standard -- no version-specific concerns [ASSUMED: based on established web standards knowledge]

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- no new dependencies, all existing
- Architecture: HIGH -- direct extension of established Phase 2 patterns
- Pitfalls: MEDIUM -- print CSS edge cases may surface during implementation
- Min plan content: HIGH -- source material provides exact items

**Research date:** 2026-04-10
**Valid until:** 2026-05-10 (stable -- no external dependencies to go stale)
