# Requirements: SFI Spar 2 -- Kursmal & Elevmedvetenhet

**Defined:** 2026-04-10
**Core Value:** Eleverna forstar vad de ska lara sig och kan folja sin egen utveckling

## v1 Requirements

### Kursinnehall

- [x] **KURS-01**: Forenklade kursmal i "Jag kan..."-format for kurs B, C och D baserade pa Skolverkets betygskriterier
- [x] **KURS-02**: Kursmal uppdelade i fem fardighetsomraden: horforstaelse, lasforstaelse, muntlig interaktion, muntlig produktion, skriftlig fardighet
- [x] **KURS-03**: Visuellt stod med ikoner och fargkodning per fardighetsomrade
- [x] **KURS-04**: Kursmal lagrade i separata JSON-datafiler (en per kurs) for enkel uppdatering
- [x] **KURS-05**: JSON-schema med stabil mal-ID och kursplan_year-falt for framtida kursplansandringar
- [x] **KURS-06**: Koppling mellan kursmal och arshjulets teman (relationer, miljo, bostad, arbete, fritid, hogtider, samhalle)

### Interaktion

- [x] **INTER-01**: Avprickningslista dar eleven kryssar av uppnadda formagor per kurs
- [x] **INTER-02**: Checkbox-state sparas i webblasarens localStorage per kurs
- [x] **INTER-03**: "Min plan" -- eleven valjer vad de ska trana (lasa, skriva, hora, tala) med checkboxar
- [x] **INTER-04**: Synlig "Sparat"-indikator nar eleven kryssar i nagot
- [x] **INTER-05**: Aterstallningsknapp med tvastegsbekraftelse

### Design och Layout

- [x] **DESIGN-01**: Mobilforst responsiv design (375px viewport som minimum)
- [x] **DESIGN-02**: Flikar/navigation for att vaxla mellan kurs B, C och D utan omladdning
- [x] **DESIGN-03**: Fargglad visuell stil inspirerad av tradmaterialet med illustrationer och ikoner
- [x] **DESIGN-04**: Ikoner alltid parade med textbeskrivning (aldrig ikon utan text)
- [x] **DESIGN-05**: Enkel svenska anpassad till respektive kursniva
- [ ] **DESIGN-06**: Utskriftsvy via @media print for klassrumsanvandning

## v2 Requirements

### Tillganglighet och Utvidgning

- **TILLAG-01**: Progressindikator per fardighetsomrade (validera med elever forst)
- **TILLAG-02**: Offline-stod via Service Worker / PWA
- **TILLAG-03**: Kursjamforelsevy -- se skillnaden mellan B, C och D
- **TILLAG-04**: Hopfallbara sektioner (accordion) per fardighetsomrade

## Out of Scope

| Feature | Reason |
|---------|--------|
| Inloggning / anvandarkonton | Ingen backend; statisk sajt |
| Lararvy / admin-panel | Larare behover inte folja framsteg digitalt |
| Betygsattning / poang | Sjalvbedomning, inte bedomning -- kan skada motivation |
| Flersprakigt stod | Fokus pa svenska; bilder som universellt stod |
| Notifikationer | Ingen server att skicka fran |
| Gamification | Risk att avleda fran larmalen |
| AI-feedback | For komplex for v1; inget uppenbart behov |
| Analytics / tracking | Integritetskanslig malgrupp |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| KURS-01 | Phase 1 | Complete |
| KURS-02 | Phase 1 | Complete |
| KURS-03 | Phase 1 | Complete |
| KURS-04 | Phase 1 | Complete |
| KURS-05 | Phase 1 | Complete |
| KURS-06 | Phase 1 | Complete |
| DESIGN-05 | Phase 1 | Complete |
| INTER-01 | Phase 2 | Complete |
| INTER-02 | Phase 2 | Complete |
| INTER-04 | Phase 2 | Complete |
| INTER-05 | Phase 2 | Complete |
| DESIGN-01 | Phase 2 | Complete |
| DESIGN-02 | Phase 2 | Complete |
| DESIGN-03 | Phase 2 | Complete |
| DESIGN-04 | Phase 2 | Complete |
| INTER-03 | Phase 3 | Complete |
| DESIGN-06 | Phase 3 | Pending |

**Coverage:**
- v1 requirements: 17 total
- Mapped to phases: 17
- Unmapped: 0

---
*Requirements defined: 2026-04-10*
*Last updated: 2026-04-10 -- traceability updated after roadmap creation*
