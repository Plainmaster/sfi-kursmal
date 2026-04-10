# Feature Landscape

**Domain:** Educational self-assessment / course goal awareness tool for adult language learners (SFI spår 2, kurs B/C/D)
**Researched:** 2026-04-10
**Confidence:** HIGH for UX/accessibility patterns; MEDIUM for SFI-specific digital tool conventions (limited prior art in this niche)

---

## Table Stakes

Features users expect. Missing = product feels incomplete or confusing.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Readable course goals per course (B, C, D) | Core purpose; without this the site has nothing to show | Low | Content work is the real effort, not the UI |
| Separate view per course | Users are in one course; seeing all three creates cognitive overload | Low | Tab or page-per-course navigation |
| "I can..." statement format | CEFR-aligned phrasing is the international standard for learner self-assessment; instantly understandable | Low | Translate Skolverket's betygskriterier into this format |
| Icon/illustration per skill area | Low-literacy and low-digital-literacy audiences comprehend icons faster than text; UX research consensus | Medium | Must pair icon with text label (never icon alone) |
| Color coding per skill area | Hörförståelse / Läsförståelse / Muntlig / Skriftlig — distinct color anchors spatial memory | Low | Use consistent palette across all three courses |
| Checklist with checkboxes | Core interaction; learners tick off achieved competencies | Low | localStorage for persistence; no login required |
| State persists between sessions | Without persistence, every visit resets progress — kills motivation | Low | localStorage per course; key on course + competency ID |
| Mobile-first layout | Many SFI students use smartphones as primary device; this is confirmed by school context | Medium | Responsive, large tap targets (min 44px), no hover-only interactions |
| Simple Swedish language level | Language at B-level for kurs B pages, C-level for kurs C, etc.; mismatch breaks trust and comprehension | Low (UX) / High (content) | Requires careful editorial process per course |
| Print-friendly output | Teachers hand out paper; students take home and show family; physical copy is culturally expected in classroom settings | Low | CSS @media print, hide UI chrome, show clean checklist |

---

## Differentiators

Features that set this product apart. Not expected by default but valued when present.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Course comparison view | Show how kurs B, C, D build on each other; gives students perspective on progression and motivates advancement | Medium | Side-by-side or progressive reveal of what changes per level |
| "Min plan" — practice selection | Student actively chooses what to focus on this week; builds agency and metacognition | Low-Medium | Simple multi-select checklist; not tracking, just intent-setting |
| Visual progress indicator per skill area | Percentage or filled bar showing how many competencies ticked per domain (Hörförståelse, etc.) | Medium | Derived from checkbox state; motivating but risk of gamification pressure |
| Thematic grouping (årshjulets teman) | Group competencies under yearly themes (Relationer, Miljö, Bostad, etc.) so goals feel contextually relevant, not abstract | Medium | Requires mapping Skolverket goals to themes; content decision |
| Teacher sharing link / print per course | Teacher prints one course sheet for the whole class; clean A4 layout for distribution | Low | CSS @media print per course section |
| Reset button with confirmation | Lets student start fresh on a new term or if they shared a device | Low | Must require two-step confirm to prevent accidental reset |
| Skill-area toggle (show/hide) | Students who want to focus on one skill (e.g., only Muntlig) can collapse others | Low | Pure CSS/JS accordion; reduces visual overwhelm |
| Offline capability (PWA) | Students in low-connectivity environments (commuting, rural areas) can still access | Medium | Service worker + cache; adds complexity but meaningful for target group |

---

## Anti-Features

Features to explicitly NOT build.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| User accounts / login | Out of scope per PROJECT.md; adds friction that will lose users before they reach content; no server permitted | Store state in localStorage, document the limitation clearly |
| Teacher dashboard / progress reporting | Creates backend dependency; also changes the power dynamic — this tool is for the student, not surveillance | If teachers need reports, the print feature serves that need |
| Grading or scoring | Conflates self-assessment (formative, growth-oriented) with evaluation (summative); research shows this damages intrinsic motivation | Keep framing as "what I can do" not "how many points I have" |
| Notifications / reminders | Requires device permissions, feels intrusive; out of scope for static site | Teacher handles engagement in class |
| Multilingual UI (translations) | Out of scope per PROJECT.md; dilutes focus on Swedish as medium; icons serve as universal bridge | Pair every text label with an icon for language-independent anchoring |
| AI feedback or chat | Over-engineering; adds complexity, cost, and trust risk; the value here is clarity of goals, not AI coaching | Clear, simple content is the product |
| Social features (share progress, compare with peers) | Privacy risk; not appropriate for this population | None needed |
| Gamification (badges, streaks, XP) | Extrinsic motivation undermines the self-regulation goals; creates anxiety in low-confidence learners | Progress bars per skill area (optional, see Differentiators) are sufficient |
| Version history / undo | Overcomplicates localStorage management for no clear user need | Reset button with confirmation covers the need |

---

## Feature Dependencies

```
Course content (B/C/D goals in JSON)
  └── Course view (separate per course)
        ├── Competency checklist
        │     └── localStorage persistence
        │           └── Progress indicator (derived from checkbox state)
        │                 └── Reset button (clears localStorage for that course)
        ├── Skill-area color coding
        │     └── Icon per skill area (paired with text label)
        └── Print view (CSS @media print)

"Min plan" (practice selection)
  └── Separate from competency checklist — independent feature, no dependency

Course comparison view
  └── Requires all three course content sets to be complete first
```

---

## MVP Recommendation

Build in this order:

1. **Content before code** — Write and edit the simplified course goals for kurs B, C, D in JSON format. This is the highest-risk work (language level, accuracy, Skolverket alignment). Everything else is blocked on it.

2. **Course view with competency checklist** — One page per course, skill areas color-coded with icons, "I can..." statements, checkboxes. localStorage persistence. This is the core product.

3. **Print view** — CSS @media print. Low effort, high classroom value. Teachers will use this immediately.

4. **Min plan (practice selection)** — Student picks what to practice. Simple multi-select. Adds agency without adding complexity.

Defer to later:
- Course comparison view (needs all content done first; medium complexity)
- Progress indicators (validate that users want them before building)
- Offline PWA (only add if there is evidence of connectivity problems)
- Skill-area accordion toggle (evaluate after first user feedback round)

---

## Feature Prioritization Matrix

| Feature | User Value | Build Effort | Priority |
|---------|-----------|-------------|----------|
| Simplified course goals (content) | Critical | High (content) / Low (code) | P0 — blocks everything |
| Checklist with localStorage | Critical | Low | P0 |
| Mobile-first responsive layout | Critical | Medium | P0 |
| Icon + color per skill area | High | Low-Medium | P0 |
| Simple Swedish per course level | Critical | High (editorial) | P0 |
| Print view | High | Low | P1 |
| Min plan checklist | High | Low-Medium | P1 |
| Reset with confirmation | Medium | Low | P1 |
| Progress indicator per skill area | Medium | Medium | P2 — validate first |
| Course comparison view | Medium | Medium | P2 — after content complete |
| Skill-area accordion toggle | Low-Medium | Low | P2 |
| Offline PWA | Medium | Medium | P3 — only if evidence of need |

---

## Sources

- European Language Portfolio / CEFR "can-do" statement format: https://www.actfl.org/educator-resources/ncssfl-actfl-can-do-statements
- CARLA self-assessment research: https://archive.carla.umn.edu/assessment/vac/improvement/p_3.html
- UX for low-literacy users (ACM): https://dl.acm.org/doi/10.1145/3449210
- UX for low-literacy users (UX Bulletin): https://www.ux-bulletin.com/designing-low-digital-literacy-users/
- localStorage for no-login progress tracking: https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
- Digital accessibility for immigrant learners: https://pressbooks.pub/alttexts2025/chapter/bridging-the-digital-accessibility-gap/
- WCAG 2.2 guidance: https://www.w3.org/TR/WCAG21/
