# Roadmap: SFI Spar 2 -- Kursmal & Elevmedvetenhet

## Overview

Fyra faser levererar en statisk webbsida dar SFI-elever forstar sina kursmal och foljer sin egen utveckling. Fas 1 bygger innehallsgrunden -- JSON-datafiler med forenklade mal och ett stabilt schema -- eftersom innehallet ar det hogsta riskarbetet och blockerar allt annat. Fas 2 bygger den kompletta interaktiva produkten: Astro-sajten, checklistan med localStorage, navigering och responsiv design. Fas 3 avslutar produkten med "Min plan" och utskriftsstod. Fas 4 driftsatter och verifierar att kursplansuppdateringsfloden fungerar end-to-end.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Innehallsgrund** - JSON-schema, forenklade kursmal for B/C/D, designsystem
- [ ] **Phase 2: Interaktiv checklista** - Astro-sajt, localStorage-avprickning, flikar, responsiv layout
- [ ] **Phase 3: Min Plan och fullstandig produkt** - Ovningsvalssektionen och utskriftsvy
- [ ] **Phase 4: Driftsattning** - Netlify-deploy och verifierat kursplansuppdateringsflode

## Phase Details

### Phase 1: Innehallsgrund
**Goal**: Allt kursinnehall finns i stabila JSON-datafiler som lararen kan uppdatera utan att andra koden
**Depends on**: Nothing (first phase)
**Requirements**: KURS-01, KURS-02, KURS-03, KURS-04, KURS-05, KURS-06, DESIGN-05
**Success Criteria** (what must be TRUE):
  1. JSON-filer for kurs B, C och D innehaller forenklade "Jag kan..."-mal for alla fem fardighetsomraden
  2. Varje mal har ett stabilt ID och ett kursplan_year-falt
  3. Varje fardighetsomrade har en definierad ikon och fargkod
  4. Kursmal ar skrivna pa enkel svenska anpassad till respektive kursniva (B, C, D)
  5. Kopplingen mellan mal och arshjulets sju teman ar mappad i JSON
**Plans:** 2 plans

Plans:
- [x] 01-01-PLAN.md -- Design tokens and kurs B content (schema foundation + reference course)
- [x] 01-02-PLAN.md -- Kurs C and kurs D content (remaining courses following kurs B pattern)

### Phase 2: Interaktiv checklista
**Goal**: Eleven kan oppna sajten pa sin mobil, se sina kursmal med visuellt stod, och kryssa av uppnadda formagor -- och avprickningen sparas automatiskt
**Depends on**: Phase 1
**Requirements**: INTER-01, INTER-02, INTER-04, INTER-05, DESIGN-01, DESIGN-02, DESIGN-03, DESIGN-04
**Success Criteria** (what must be TRUE):
  1. Eleven kan vaxla mellan flikarna Kurs B, C och D utan att sidan laddas om
  2. Eleven kan kryssa av ett kursmal och se en "Sparat"-indikator direkt
  3. Avprickning kvarstar nar eleven stanger och ateropper webblesaren
  4. Eleven kan nollstalla sin avprickning via en knapp som kraver tvastegsbekraftelse
  5. Sajten fungerar och ar anvandbar pa en 375px-bred mobil
**Plans:** 3 plans

Plans:
- [x] 02-01-PLAN.md -- Scaffold Astro 6 project with Tailwind CSS 4, base layout, and global styles
- [x] 02-02-PLAN.md -- Build all Astro components (tabs, domain sections, checkboxes, reset) and compose index page
- [x] 02-03-PLAN.md -- Wire client-side JavaScript interactivity and human verification of complete checklist

### Phase 3: Min Plan och fullstandig produkt
**Goal**: Eleven kan valja vad de ska trana nasta period via "Min plan", och lararen kan skriva ut materialet for klassrumsanvandning
**Depends on**: Phase 2
**Requirements**: INTER-03, DESIGN-06
**Success Criteria** (what must be TRUE):
  1. Eleven kan kryssa i checkboxar i "Min plan" for att valja fardighetsomraden att trana (lasa, skriva, hora, tala)
  2. "Min plan"-val sparas i localStorage och kvarstar mellan sessioner
  3. En utskrift av sidan via webblesarens utskriftsfunktion ger ett anvandbart klassrumsdokument utan navigeringselement
**Plans:** 2 plans

Plans:
- [x] 03-01-PLAN.md -- Min plan tab with 4 skill domains, checkboxes, custom goals, and localStorage persistence
- [ ] 03-02-PLAN.md -- Print stylesheet and print preparation JS for classroom handouts

### Phase 4: Driftsattning
**Goal**: Sajten ar publikt tillganglig och lararen kan sjalvstandigt uppdatera kursmal nar Skolverket reviderar kursplanerna
**Depends on**: Phase 3
**Requirements**: (none -- operational delivery boundary)
**Success Criteria** (what must be TRUE):
  1. Sajten ar atkomlig via en publik URL utan inloggning
  2. En larare kan uppdatera en JSON-kursmalsfil, trigga en ny build och se de nya malen -- utan att andra nagon kod
  3. Sajten fungerar korrekt pa bade iOS Safari och Android Chrome
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Innehallsgrund | 2/2 | Complete | 2026-04-10 |
| 2. Interaktiv checklista | 0/3 | Planning complete | - |
| 3. Min Plan och fullstandig produkt | 0/2 | Planning complete | - |
| 4. Driftsattning | 0/? | Not started | - |
