---
phase: 02-interaktiv-checklista
reviewed: 2026-04-10T12:00:00Z
depth: standard
files_reviewed: 10
files_reviewed_list:
  - src/pages/index.astro
  - src/components/TabNav.astro
  - src/components/CoursePanel.astro
  - src/components/DomainSection.astro
  - src/components/GoalCheckbox.astro
  - src/components/ResetButton.astro
  - src/layouts/BaseLayout.astro
  - src/styles/global.css
  - astro.config.mjs
  - package.json
findings:
  critical: 1
  warning: 4
  info: 3
  total: 8
status: issues_found
---

# Phase 02: Code Review Report

**Reviewed:** 2026-04-10T12:00:00Z
**Depth:** standard
**Files Reviewed:** 10
**Status:** issues_found

## Summary

The codebase implements a clean, static SFI checklist application with tab-based navigation, localStorage persistence, and progress tracking. The architecture follows Astro conventions well and the component decomposition is sensible. The main concerns are: (1) a DOM injection risk via unsanitized localStorage data used in a query selector, (2) missing Swedish diacritical characters throughout user-facing text, and (3) several non-null assertions that could throw at runtime.

## Critical Issues

### CR-01: DOM Selector Injection via Unsanitized localStorage Data

**File:** `src/pages/index.astro:136`
**Issue:** The `goalId` value read from localStorage is interpolated directly into a `querySelector` attribute selector (`[data-goal-id="${goalId}"]`). If localStorage is tampered with (e.g., via browser devtools, XSS on the same origin, or a malicious browser extension), a crafted key containing `"]` could break out of the attribute selector and cause unexpected DOM queries. While the impact is limited (no server, no sensitive data), this is a defense-in-depth concern -- `querySelector` with unsanitized input is a known anti-pattern.
**Fix:**
```javascript
// Sanitize goalId before using in selector -- reject anything that isn't alphanumeric/hyphens
const safeId = goalId.replace(/[^a-zA-Z0-9_-]/g, '');
if (safeId !== goalId) continue; // skip corrupted entries
const cb = document.querySelector(`[data-goal-id="${safeId}"]`) as HTMLInputElement | null;
```

## Warnings

### WR-01: Missing Swedish Diacritical Characters in User-Facing Text

**File:** `src/components/ResetButton.astro:15,21,24`
**Issue:** Swedish characters are missing throughout: "Borja om" should be "Borja om" with proper diacritics, "Ar du saker" should use proper Swedish, "forsvinner" is missing its diacritic. The project CLAUDE.md specifies this is for SFI students learning Swedish -- incorrect character rendering undermines the educational purpose.
**Fix:** Replace with correct Swedish text:
```astro
<!-- Line 15 -->
Borja om  -->  Borja om (with proper Swedish characters: Borja om)

<!-- Line 21 -->
Ar du saker? Alla markeringar for Kurs {course} forsvinner.
-->  use proper Swedish diacritics throughout

<!-- Line 24 -->
Ja, borja om  -->  use proper Swedish diacritics
```
Note: Also affects `src/layouts/BaseLayout.astro:10` where `SFI Spar 2 -- Kursmal` should be `SFI Spar 2 -- Kursmal` with proper diacritics matching the project description.

### WR-02: Unsafe Non-Null Assertions on DOM Dataset Properties

**File:** `src/pages/index.astro:41,91,92`
**Issue:** Three non-null assertions (`!`) on `dataset.course` and `dataset.goalId` assume data attributes are always present. If any checkbox or tab element is rendered without the expected data attribute (e.g., due to a data file with missing fields), these will throw `TypeError: Cannot read properties of undefined`.
**Fix:**
```typescript
// Line 41: Guard with early return
tab.addEventListener('click', () => {
  const course = (tab as HTMLElement).dataset.course;
  if (course) switchTab(course);
});

// Lines 91-92: Guard with early return
cb.addEventListener('change', () => {
  const el = cb as HTMLInputElement;
  const course = el.dataset.course;
  const goalId = el.dataset.goalId;
  if (!course || !goalId) return;
  // ... rest of handler
});
```

### WR-03: Unsafe Non-Null Assertion on parentNode

**File:** `src/pages/index.astro:70`
**Issue:** `indicator.parentNode!` uses a non-null assertion. If the saved-indicator element exists but has been detached from the DOM (e.g., during rapid re-renders or framework hydration), this throws.
**Fix:**
```typescript
if (!indicator || !indicator.parentNode) return;
indicator.parentNode.replaceChild(clone, indicator);
```

### WR-04: Loose `any` Types in Component Props

**File:** `src/components/CoursePanel.astro:8-9`
**Issue:** `courseData: any` and `tokens: any` bypass all type checking. If the JSON data structure changes (e.g., `domains` is renamed or a field is removed), errors will only surface at runtime in the browser, not at build time.
**Fix:**
```typescript
interface CourseData {
  domains: Record<string, { goals: Array<{ id: string; text: string }> }>;
}
interface Tokens {
  domains: Record<string, { label: string; icon: string }>;
}

interface Props {
  course: string;
  courseData: CourseData;
  tokens: Tokens;
  initiallyHidden?: boolean;
}
```

## Info

### IN-01: Tab Buttons Missing Accessibility Attributes

**File:** `src/components/TabNav.astro:13-22`
**Issue:** Tab buttons lack `role="tab"`, `aria-selected`, and `aria-controls` attributes. The `<nav>` should use `role="tablist"`. This matters for screen reader users.
**Fix:** Add ARIA attributes:
```astro
<div role="tablist" class="flex justify-around">
  {tabs.map((tab, i) => (
    <button
      role="tab"
      aria-selected={i === 0 ? "true" : "false"}
      aria-controls={`panel-${tab.course}`}
      class:list={[...]}
      data-course={tab.course}
    >
      {tab.label}
    </button>
  ))}
</div>
```
Also update `aria-selected` in the `switchTab` function in `index.astro`.

### IN-02: Missing Meta Description

**File:** `src/layouts/BaseLayout.astro:9`
**Issue:** No `<meta name="description">` tag. While not a bug, this affects SEO and link previews when the page is shared.
**Fix:** Add after the viewport meta tag:
```html
<meta name="description" content="SFI spar 2 kursmal och checklista for kurs B, C och D" />
```

### IN-03: `iconMap` Uses `any` Type

**File:** `src/components/DomainSection.astro:16`
**Issue:** `Record<string, any>` loses type information for the icon components. Minor since these are build-time Astro components, but could mask typos in icon names from the JSON data.
**Fix:** Use the Astro component type or leave as-is if no suitable type exists in the lucide-astro package.

---

_Reviewed: 2026-04-10T12:00:00Z_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
