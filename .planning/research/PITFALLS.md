# Domain Pitfalls: SFI Digital Learning Tools

**Domain:** Static educational website for adult language learners (SFI spår 2)
**Researched:** 2026-04-10

---

## Critical Pitfalls

Mistakes that cause rewrites or major issues.

---

### Pitfall 1: Curriculum Content Baked Into Markup

**What goes wrong:** Course goal text is written directly in HTML templates instead of a separate data layer. When Skolverket publishes updated course plans — which is actively in progress (new SFI regulations took effect January 2026; new kursplaner are expected to be decided by government in late 2026) — every goal, criterion, and skill description must be hunted down and edited inside code files.

**Why it happens:** It feels faster to write HTML directly than to design a data structure first. The abstraction seems unnecessary until the first curriculum change arrives.

**Consequences:** A curriculum update that should take two hours takes two days. Non-technical teachers cannot make the change themselves. Risk of inconsistency between courses when only some goals are updated. Described explicitly as a risk in the project requirements.

**Prevention:**
- Put all course goal text, checklist items, and skill descriptions in a single `data/courses.json` file before any HTML is written.
- HTML templates reference data only via keys; no Swedish educational prose lives in `.html` files.
- JSON schema version field (e.g., `"schema_version": 1`) so breaking changes are detectable.

**Detection (warning signs):**
- Any Swedish sentence longer than a UI label appears in a `.html` or `.js` file.
- Copy-pasting course goal text between the B, C, and D sections during development.

**Phase to address:** Phase 1 (data modeling) — the JSON schema must be finalized before any UI work begins.

---

### Pitfall 2: Checked State Lost on Page Refresh (No Persistence Strategy)

**What goes wrong:** The self-assessment checklists work perfectly until the student closes the browser tab or shares a link with a classmate. All checked boxes reset. For adult learners with low digital literacy, this is catastrophic — they do not understand why their work disappeared, and they stop trusting the tool.

**Why it happens:** `localStorage` is the obvious solution for a no-backend site, but developers often implement it as an afterthought ("we'll add save later"), and the UX around data loss is not designed at all.

**Consequences:**
- Students lose motivation after one session.
- Teacher loses credibility of the tool ("det fungerar inte").
- Private/incognito mode silently loses all data (localStorage becomes sessionStorage in private mode — deleted on tab close).

**Prevention:**
- Decide on the persistence strategy in the data design phase, not the UI phase.
- Use `localStorage` with a clearly namespaced key (e.g., `sfi-spår2-kurs-b-checklist`).
- Write state on every checkbox change (`addEventListener('change', save)`), not on page unload.
- Display a visible "Sparat" indicator so students know their data is safe.
- Show a first-visit banner explaining that data is saved locally in this browser only, and will be lost if they clear their browser history.
- Do not use private/incognito mode as a test environment during development — it hides the persistence problem.

**Detection (warning signs):**
- Checked boxes don't persist after pressing F5 during development.
- No `localStorage.setItem` calls exist in the codebase by the end of the checklist implementation sprint.

**Phase to address:** Phase 2 (checklist/UI implementation). Design the persistence model in Phase 1 alongside the data schema.

---

### Pitfall 3: Language Calibrated to Developer, Not to Student

**What goes wrong:** UI labels, instructions, and error messages are written in standard Swedish — not simplified Swedish calibrated to each course level. A student in kurs B (lowest proficiency in spår 2) reads "Markera de förmågor du anser att du har uppnått" and does not understand the task.

**Why it happens:** The developer is fluent in Swedish and writes naturally. Instructions that seem obvious to a native speaker ("click the checkbox") are opaque to a B-level learner with limited vocabulary and no tradition of self-directed digital learning.

**Consequences:** The tool is technically deployed but not used. Teachers have to explain the interface verbally every class, defeating the self-service goal.

**Prevention:**
- Every UI string — not just course goal text — must go through a "kurs B test": would a student at the lowest level understand this word by word?
- Preferred pattern: verb + noun in plain Swedish (e.g., "Kryssa i" not "Markera", "Din plan" not "Studieplanering").
- Use icons *with* text labels, never icons alone (see Pitfall 5).
- Have the teacher (Minja) review all UI labels before any course content is added — UI language review is not the same as content review.

**Detection (warning signs):**
- Any UI label containing: "uppnå", "förmåga", "interaktion", "produktion", "bedömning" without a visual/icon gloss.
- No language review step in the development workflow.

**Phase to address:** Phase 1 (content planning) and Phase 2 (implementation). Build a UI string glossary early; do not write UI copy inline.

---

## Moderate Pitfalls

---

### Pitfall 4: Scroll-Heavy Layout That Breaks Visual Concentration

**What goes wrong:** Long pages with many checklist items force students to scroll. Nielsen Norman Group research on lower-literacy users shows that scrolling breaks visual concentration because these users cannot scan to reacquire their position — they must re-read from a recognizable landmark.

**Why it happens:** Responsive design often means long single-column pages on mobile. Developers test on desktop first, where the same content is multi-column and manageable.

**Prevention:**
- Divide content into course-level tabs or accordions, not one long page per course.
- Each visible section should fit one phone screen without scrolling when possible.
- Test every screen on a 375px-wide viewport (iPhone SE size — common among low-income students) before considering it done.
- Sticky section headers so students always know which part of the checklist they are in.

**Detection (warning signs):**
- Any section requires more than 3 scroll gestures to read fully on a 375px viewport.
- No mobile testing step in the review process.

**Phase to address:** Phase 2 (layout/UI). Establish mobile viewport testing as a done criterion.

---

### Pitfall 5: Icons Without Text Labels Cause Cross-Cultural Misinterpretation

**What goes wrong:** Icons are used as the primary navigation or action affordance without accompanying text. Research on cross-cultural icon comprehension shows that icons are consistently misinterpreted across cultural contexts — the populations using this tool come from dozens of different countries with different symbol conventions.

**Why it happens:** Icons feel clean and multilingual. Designers underestimate how culturally specific even "universal" icons are (e.g., a checkmark means "wrong" in some East Asian educational contexts; a house icon for "home" is not universal).

**Consequences:** Students tap wrong things, get lost, and cannot self-correct because the icons that should help them navigate instead confuse them.

**Prevention:**
- Every icon must have a visible text label, not just an `aria-label`.
- Icon + label pattern: icon on top, label below, no icon-only buttons.
- Prefer very concrete pictograms (a mouth for speaking, an ear for listening, a pencil for writing, a book for reading) over abstract metaphors.
- The five SFI skill areas (hörförståelse, läsförståelse, muntlig interaktion, muntlig produktion, skriftlig färdighet) are abstract — pair each with both an icon AND a one-line plain-Swedish description.

**Detection (warning signs):**
- Any clickable element has an icon but no visible text.
- Icon selection done without showing candidates to someone unfamiliar with the metaphor.

**Phase to address:** Phase 1 (design system). Establish icon + label as a non-negotiable pattern before implementation.

---

### Pitfall 6: Three Parallel Course Structures That Diverge in Code

**What goes wrong:** Courses B, C, and D have the same five skill areas at increasing complexity. Developers build course B first, then copy-paste and modify for C and D. When the layout needs to change, there are now three nearly-identical HTML sections to update. One gets missed. The B view looks different from D.

**Why it happens:** Copy-paste is faster than parameterization. The temptation is even stronger when the differences between courses feel small.

**Consequences:** Visual inconsistency between courses. Bug fixes applied to B not propagated to C or D. Curriculum updates require editing three places instead of one.

**Prevention:**
- Build a single course view component that accepts a course identifier as a parameter.
- The component renders from JSON data; it never hardcodes which course it is rendering.
- There is one HTML template for all three courses, not three copies.

**Detection (warning signs):**
- Any HTML section contains the string "Kurs B", "Kurs C", or "Kurs D" hardcoded in a structural (non-data) position.
- The same CSS class name appears in three separate HTML blocks.

**Phase to address:** Phase 2 (component architecture). This must be a design constraint, not a refactor.

---

### Pitfall 7: Print and Share Workflow Ignored

**What goes wrong:** The tool is designed as a purely digital experience. Students want to print their personal plan or share it with their teacher. Because no print stylesheet exists, printing the page produces a broken layout with overflow, cut-off text, and non-functional checkboxes.

**Why it happens:** Print is treated as an afterthought. Developers test in browser only.

**Consequences:** Teachers reject the tool and revert to paper worksheets. The "Min plan" feature — the core differentiator — loses value because it cannot be shared in the format teachers actually use (paper or PDF).

**Prevention:**
- Add a `@media print` stylesheet that renders the checklist as a clean, black-and-white form.
- "Skriv ut / Spara som PDF" button that triggers `window.print()`.
- Test print output for every major view before marking a milestone complete.

**Detection (warning signs):**
- No `print.css` or `@media print` block anywhere in the codebase.
- "Print" not mentioned in any acceptance criteria.

**Phase to address:** Phase 2 or 3. Should be designed alongside the checklist feature, not added at the end.

---

## Minor Pitfalls

---

### Pitfall 8: Touch Targets Too Small for Mobile Input

**What goes wrong:** Checkboxes and navigation links are rendered at browser default size (typically 16-18px square). For adult users with less experience using touchscreens — a common profile in SFI populations — this causes missed taps, accidental checks, and frustration.

**Prevention:**
- Minimum touch target size: 44×44px (Apple HIG) or 48×48dp (Material Design).
- Custom checkbox styling (CSS `appearance: none`) with explicit size and tap area.
- Label element wraps the checkbox input so the entire label text is also a tap target.

**Phase to address:** Phase 2 (UI implementation). Add touch target size to the CSS component review checklist.

---

### Pitfall 9: Color-Only Differentiation Between Courses

**What goes wrong:** Courses B, C, and D are color-coded (as the existing tree material suggests). Color is the only visual differentiator. Students with color vision deficiency — approximately 8% of male-presenting students — cannot distinguish courses.

**Prevention:**
- Use color + shape + label together (e.g., different icon shape per course, not just color).
- Test the color palette with a color-blindness simulator before finalizing.
- Each course section has a text heading that is unambiguous without color.

**Phase to address:** Phase 1 (design system). Color decisions made here affect all subsequent phases.

---

### Pitfall 10: No Offline Capability Assumption Broken by School Network

**What goes wrong:** The static site is hosted online, but school computer labs and some student mobile connections are unreliable. The site loads slowly or not at all. No offline fallback exists.

**Prevention:**
- Add a minimal Service Worker that caches the app shell and JSON data on first load.
- This is a one-day addition with significant impact on reliability in school network conditions.

**Phase to address:** Phase 3 (polish/deployment). Not critical for MVP but high value for adoption.

---

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Data modeling / JSON schema | Baking content into HTML instead of data | Define schema before writing any HTML |
| Checklist component | No persistence strategy | Implement localStorage save on every Phase 2 checkbox |
| Language / copywriting | Standard Swedish in UI strings | Teacher review of all UI labels, not just course content |
| Mobile layout | Scroll-heavy single-column pages | 375px viewport test as done criterion |
| Course B/C/D views | Copy-paste divergence | Single parameterized component from day one |
| Icon selection | Cross-cultural misinterpretation | Icon + text label rule, concrete pictograms only |
| Print/share | No print stylesheet | Design print view alongside digital view |
| Curriculum update (2026) | Skolverket new kursplaner expected late 2026 | JSON schema versioning; update = edit JSON only |

---

## Skolverket Curriculum Risk (Specific to This Project)

Skolverket is actively developing new SFI course structures under a government assignment from April 2024. The consultation period ran June–September 2025. The assignment is to be reported to government in April 2026, after which the government decides on regulatory changes before Skolverket can publish new curricula. This means new kursplaner could arrive at any point in late 2026 — potentially shortly after the tool is deployed.

**Specific risk:** The simplified course goal texts (kurs B, C, D) written for this tool are based on current Skolverket criteria. If the course structure changes (e.g., courses renamed, skill areas reorganized, new progression model), the JSON content needs replacement.

**Mitigation already designed into the project:** The JSON data file approach directly addresses this. The additional safeguard is to include a `source_version` or `kursplan_year` field in the JSON so that anyone updating the content knows which Skolverket document the current text is derived from.

---

## Sources

- Nielsen Norman Group, "Lower-Literacy Users: Writing for a Broad Consumer Audience": https://www.nngroup.com/articles/writing-for-lower-literacy-users/
- Skolverket, "Nya kurser i komvux i sfi": https://www.skolverket.se/styrning-och-ansvar/forandringar-inom-skolomradet/skolverket-ser-over-kursplaner-i-komvux/nya-kurser-i-komvux-i-sfi
- Skolverket, "Skärpta krav i sfi" (2026 rule changes): https://www.skolverket.se/styrning-och-ansvar/anordna-utbildning/nyanlandas-utbildning/mottagande-och-utbildning-i-komvux/skarpta-krav-i-sfi
- ALT Texts 2025, "Enhancing Accessibility for Second Language Learners": https://pressbooks.pub/alttexts2025/chapter/enhancing-accessibility-for-second-language-learners-in-higher-education/
- Cieden, "How to ensure icon designs are universal": https://cieden.com/book/sub-atomic/iconography/icon-universal-design
- MDN, "Client-side storage / localStorage": https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Client-side_storage
- Microsoft Research, "Designing Mobile Interfaces for Novice and Low-Literacy Users": https://www.microsoft.com/en-us/research/publication/designing-mobile-interfaces-for-novice-and-low-literacy-users/
- Readability Guidelines, "Plain English": https://readabilityguidelines.co.uk/clear-language/plain-english/
