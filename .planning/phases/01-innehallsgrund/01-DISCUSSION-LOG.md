# Phase 1: Innehallsgrund - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md -- this log preserves the alternatives considered.

**Date:** 2026-04-10
**Phase:** 01-innehallsgrund
**Areas discussed:** JSON-schema, Kursmalstext, Tema-koppling, Designsystem-grund

---

## JSON-schema

| Option | Description | Selected |
|--------|-------------|----------|
| En fil per kurs | Tre separata filer (kurs-b.json, kurs-c.json, kurs-d.json) | |
| Allt i en fil | En gemensam fil med alla kurser | |
| Claude valjer | Claude valjer rimlig struktur | x |

**User's choice:** "Jag vill att du valjer rimliga forslag till vad som ska goras."
**Notes:** User delegated all decisions to Claude. Chose one file per course for teacher editability.

---

## Kursmalstext

| Option | Description | Selected |
|--------|-------------|----------|
| Fritt forenklade | Fri formulering av forenklad text | |
| Troget Skolverket | Tatt kopplat till Skolverkets originaltext | |
| Claude valjer | Claude valjer rimlig niva | x |

**User's choice:** Delegated to Claude.
**Notes:** Followed existing "Jag kan..." format from kurs B material. Concrete, checkable statements.

---

## Tema-koppling

| Option | Description | Selected |
|--------|-------------|----------|
| Ett mal per tema | Strikt 1:1-koppling | |
| Manga-till-manga | Varje mal kan ha flera teman | |
| Lost taggat | Frivillig taggning, inte alla mal behover tema | |
| Claude valjer | Claude valjer rimlig granularitet | x |

**User's choice:** Delegated to Claude.
**Notes:** Chose many-to-many with optional tagging. Not all goals need themes.

---

## Designsystem-grund

| Option | Description | Selected |
|--------|-------------|----------|
| Tradmaterialets stil | Direkt inspirerad av befintliga tradbilder | |
| Modern, platt | Ren, modern UI-palett | |
| Claude valjer | Claude valjer rimliga fargval och ikoner | x |

**User's choice:** Delegated to Claude.
**Notes:** Lucide icons mapped to 5 skill domains. Bright friendly palette, details deferred to planning.

---

## Claude's Discretion

All four areas were delegated to Claude with instruction: "Jag vill att du valjer rimliga forslag."

## Deferred Ideas

None.
