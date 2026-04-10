# SFI Spår 2 -- Kursmål & Elevmedvetenhet

## What This Is

En webbsida för SFI spår 2-elever (kurs B, C och D) som gör Skolverkets kursmål begripliga och konkreta. Webbsidan har tre delar: förenklade kursmål med visuellt stöd, elevens egen plan för hur de ska nå målen, och en avprickningslista där eleven kan följa vilka förmågor de utvecklat. Materialet är utformat på enkel svenska med färgglada illustrationer och ikoner, i stil med det befintliga trädmaterialet.

## Core Value

Eleverna förstår vad de ska lära sig och kan följa sin egen utveckling -- kursmålen blir ett verktyg för eleven, inte bara för läraren.

## Requirements

### Validated

(None yet -- ship to validate)

### Active

- [ ] Förenklade kursmål för kurs B, C och D baserade på Skolverkets betygskriterier
- [ ] Kursmålen presenterade med visuellt stöd (ikoner, illustrationer, färgkodning)
- [ ] Elevens egen plan -- checklista där eleven väljer vad de ska träna (läsa, skriva, höra, tala)
- [ ] Avprickningsdokument -- eleven kryssar av uppnådda förmågor per kurs
- [ ] Webbsida som fungerar utan inloggning -- eleven öppnar och använder direkt
- [ ] Enkel svenska anpassad till varje kursnivå (B, C, D)
- [ ] Separata vyer/sektioner per kurs (B, C, D)
- [ ] Struktur som gör det enkelt att byta ut kursmål om Skolverket uppdaterar kursplanerna
- [ ] Responsiv design -- fungerar på mobil och dator
- [ ] Färgglad, visuell stil inspirerad av det befintliga trädmaterialet

### Out of Scope

- Inloggning/konton -- eleverna behöver inte logga in
- Lärarvy/admin -- lärare behöver inte följa elevernas framsteg digitalt
- Flerspråkigt stöd -- materialet är på enkel svenska (inte översättningar)
- Sparning av elevdata på server -- ingen backend
- Betygsättning eller bedömning -- detta är för medvetenhet, inte för bedömning

## Context

- **Skolkontext:** SFI (Svenska för invandrare) spår 2, som riktar sig till elever med viss utbildningsbakgrund. Kurserna B, C och D har progressivt högre krav.
- **Befintligt material:** Det finns utkast -- "Min plan" (checkboxar per färdighet), förenklade kursmål (trädbilder), förväntansdokument, årshjul med teman, och Skolverkets officiella kursplaner/betygskriterier.
- **Fem kunskapsområden:** Hörförståelse, läsförståelse, muntlig interaktion, muntlig produktion, skriftlig färdighet. Dessa är samma för alla kurser men med stigande komplexitet.
- **Årshjulets teman:** Relationer, Miljö, Bostad, Arbete och studier, Fritid och hälsa, Högtider, Samhälle.
- **Möjliga nya kursplaner:** Skolverket kan uppdatera kursplanerna under 2026. Materialet ska vara strukturerat så att kursmålen går att byta ut utan att bygga om hela sidan.

## Constraints

- **Språknivå**: Texten måste vara begriplig för SFI-elever på respektive kursnivå (B, C, D)
- **Ingen backend**: Statisk webbsida -- ingen server, databas eller inloggning
- **Uppdaterbarhet**: Kursmålen ska ligga i en separat datastruktur (t.ex. JSON) så att de enkelt kan bytas ut
- **Tillgänglighet**: Ska fungera på mobiltelefon (många elever använder mobil som primär enhet)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Statisk webbsida utan backend | Ingen inloggning behövs, enklare att underhålla och drifta | -- Pending |
| Kursmål i separat datafil (JSON) | Gör det möjligt att uppdatera kursmål utan att ändra koden vid nya kursplaner | -- Pending |
| Visuell stil som trädmaterialet | Eleverna känner igen stilen, färgglatt och tillgängligt | -- Pending |
| Enkel svenska + ikoner istället för flerspråkigt | Fokus på svenska som kommunikationsspråk, bilder som universellt stöd | -- Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? -> Move to Out of Scope with reason
2. Requirements validated? -> Move to Validated with phase reference
3. New requirements emerged? -> Add to Active
4. Decisions to log? -> Add to Key Decisions
5. "What This Is" still accurate? -> Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check -- still the right priority?
3. Audit Out of Scope -- reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-10 after initialization*
