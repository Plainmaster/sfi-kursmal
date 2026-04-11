# Uppdatera kursmål

Den här guiden förklarar hur du som lärare kan uppdatera kursmålen på webbsidan. Du behöver inte kunna programmera -- du gör alla ändringar direkt på GitHub.

## Vilka filer redigerar du?

Kursmålen finns i tre filer, en per kurs:

| Fil | Kurs |
|-----|------|
| `src/data/kurs-b.json` | Kurs B (CEFR A1) |
| `src/data/kurs-c.json` | Kurs C (CEFR A2) |
| `src/data/kurs-d.json` | Kurs D (CEFR B1) |

Varje fil innehåller alla mål för en kurs, uppdelade i domäner (hörförståelse, läsförståelse, muntlig produktion, skriftlig produktion, grammatik, uttal).

## Steg för steg: redigera på GitHub

1. Gå till [github.com/Plainmaster/sfi-kursmal](https://github.com/Plainmaster/sfi-kursmal)
2. Klicka på mappen `src`, sedan `data`
3. Klicka på filen du vill ändra, till exempel `kurs-b.json`
4. Klicka på pennikonen (redigera) uppe till höger
5. Hitta måltexten du vill ändra -- den står i fältet `"text"` inom citattecken
6. Ändra texten mellan citattecknen
7. Klicka på knappen **"Commit changes..."**
8. Skriv en kort beskrivning, till exempel: "Uppdaterade mål för hörförståelse kurs B"
9. Klicka på **"Commit changes"**
10. Vänta 1--2 minuter. Besök sedan webbsidan och kontrollera att ändringen syns.

## Vad du KAN ändra

- **`"text"`** -- Måltexten som eleven ser (meningarna som börjar med "Jag kan..." eller "Jag förstår...")
- **`"themes"`** -- Temataggar (lista med till exempel: `"relationer"`, `"fritid-och-halsa"`, `"arbete-och-studier"`, `"bostad-och-narmiljo"`, `"samhalle"`)

## Vad du INTE får ändra

- **`"id"`** (till exempel `"B-HORA-01"`) -- Dessa kopplar till elevernas sparade framsteg. Om du ändrar ett id förlorar eleverna sina ikryssade mål.
- **`"course"`**, **`"kursplan_year"`**, **`"cefr"`** -- Kursmetadata
- **`"domains"`** och domännamnen (till exempel `"horforstaelse"`) -- Domänstrukturen är fast
- **`"kursplan_year"`** inuti varje mål -- Ska matcha kursplanens år
- Ta INTE bort kommatecken, hakparenteser `[]`, klammerparenteser `{}` eller citattecken `""`

## Vanliga misstag

| Misstag | Vad händer | Lösning |
|---------|-----------|---------|
| Saknat kommatecken mellan mål | Webbsidan uppdateras inte (bygget misslyckas) | Kontrollera att varje `}` följs av `,` utom den allra sista i listan |
| Citattecken saknas | Bygget misslyckas | Varje `"` måste ha en matchande `"` |
| Ändrat ett id-fält | Elevernas ikryssade mål försvinner | Ångra ändringen och skriv tillbaka det gamla id:t |

Om webbsidan inte uppdateras efter 5 minuter: kontrollera att du har sparat (commit). Netlify skickar ett e-postmeddelande om bygget misslyckas.

## Exempel: ändra ett mål

**Före:**
```json
{
  "id": "B-HORA-01",
  "text": "Jag förstår enkelt tal i vanliga situationer.",
  "kursplan_year": 2018,
  "themes": []
}
```

**Efter** (du ändrar bara texten i `"text"`):
```json
{
  "id": "B-HORA-01",
  "text": "Jag förstår enkla ord och fraser i vardagliga situationer.",
  "kursplan_year": 2018,
  "themes": []
}
```

Observera: bara texten mellan citattecknen på raden `"text"` har ändrats. Allt annat är exakt likadant.
