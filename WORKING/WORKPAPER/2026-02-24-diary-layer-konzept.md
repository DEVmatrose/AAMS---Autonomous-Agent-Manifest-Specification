# WORKPAPER — Diary Layer: Temporal Context in AAMS

**Session:** 2026-02-24
**Status:** OPEN
**Typ:** Architektur-Exploration / Feature-Konzept

---

## Ausgangslage

AAMS hat aktuell zwei Dokumentations-Layer:

| Layer | Funktion | Zeitdimension | Charakter |
|---|---|---|---|
| **Whitepaper** | Stabile System-Wahrheit | Langfristig | Normativ / strukturell |
| **Workpaper** | Session-Arbeit | Kurzfristig | Operativ / iterativ |

**Identifiziertes Gap:** Entscheidungen entstehen *zwischen* diesen Layern. Strategische Motive verschwinden. Gedankengänge gehen verloren. Niemand — weder Mensch noch Agent — kann später rekonstruieren: *„Warum haben wir das eigentlich so entschieden?"*

Das Workpaper ist dafür zu strukturiert. Das Whitepaper ist dafür zu stabil.

---

## Konzept: Diary Layer

### Einordnung

Ein dritter, **chronologischer** Layer — kein weiterer Komplexitätslayer, sondern eine Entkopplung von Zeitebenen:

| Layer | Funktion | Zeitdimension | Charakter |
|---|---|---|---|
| **Whitepaper** | Stabile Wahrheit | Langfristig | Normativ / strukturell |
| **Workpaper** | Session-Arbeit | Kurzfristig | Operativ / iterativ |
| **Diary** | Entscheidungs- und Denkspur | Chronologisch | Narrativ / reflexiv |

### Architekturelle Bezeichnung im AAMS-Kontext

> **Temporal Context Layer**

### Vorgeschlagene Struktur

```
WORKING/
  WHITEPAPER/     → Normen & feste Wahrheiten
  WORKPAPER/      → Sessionzustände
  DIARY/          → Chronologische Entscheidungs-Logs
    2026-02.md
    2026-03.md
```

Monatsweise. Kein Dateiwildwuchs.

---

## Warum "Tagebuch" und nicht "Notizen"

Notizen wirken technisch. Tagebuch impliziert Lesbarkeit und Zeitachse.

Genau das wird gebraucht:
- Telegrammstil
- Kurze Einträge (max. 10 Zeilen)
- Datum/Zeit-Stempel
- Keine Strukturzwänge
- Keine Formatregeln

Nicht als Dokumentationspflicht — als **Gedanken-Trace**.

---

## Mehrwert

**Für Menschen:**
- Reflektion und Mustererkennung
- Motivation über Iterationen
- Gedankentransparenz

**Für Agenten:**
- Entscheidungsherkunft rekonstruierbar
- Strategiewechsel nachvollziehbar
- Kontext-Drift reduzierbar
- Iterative Optimierung auf Metaebene möglich

> Dein Whitepaper beschreibt die Struktur.  
> Dein Workpaper beschreibt die Arbeit.  
> Dein Diary beschreibt die Reise.

---

## Kernregel: Nicht überregeln

Das Diary braucht **genau drei Regeln**, nicht mehr:

1. Maximal 10 Zeilen pro Eintrag
2. Nur Entscheidungen, Blocker, Erkenntnisse
3. Kein Perfektionismus

Ein Regelwerk tötet es.

---

## Offene Fragen / Entscheidungsbedarf

- [ ] **Zugehörigkeit:** `WORKING/DIARY/` vs. `DIARY/` im Repo-Root?
- [ ] **LTM-Integration:** Wird das Diary in ChromaDB ingested oder bleibt es rein human-readable?
- [ ] **Agent-Schreibrecht:** Darf ein Agent Diary-Einträge schreiben, oder ist das nur Human-Layer?
- [ ] **SPEC.md-Aufnahme:** Diary als offizieller optionaler Layer in der Spezifikation?
- [ ] **Schema-Update:** `.agent.json` / `AGENT.json` braucht neues Feld `diary_path` oder ähnlich?
- [ ] **Einstiegsdatei:** Wird `DIARY/2026-02.md` sofort angelegt oder erst bei erstem Eintrag?

---

## Vorläufige Entscheidungen

*(werden hier ergänzt sobald getroffen)*

---

## File Protocol

| Action | File | Detail |
|---|---|---|
| CREATE | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` | Dieses Workpaper |
