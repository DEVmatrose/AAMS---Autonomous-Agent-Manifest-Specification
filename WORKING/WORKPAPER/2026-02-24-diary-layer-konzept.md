# WORKPAPER — Diary Layer: Temporal Context in AAMS

**Session:** 2026-02-24 (Review: 2026-02-26)
**Status:** OPEN — Diary ist **mandatory**. Implementierung ausstehend.
**Typ:** Architektur-Entscheidung / Feature-Spezifikation

---

## Ausgangslage

AAMS hat aktuell zwei Dokumentations-Layer:

| Layer | Funktion | Zeitdimension | Charakter |
|---|---|---|---|
| **Whitepaper** | Stabile System-Wahrheit | Langfristig | Normativ / strukturell |
| **Workpaper** | Session-Arbeit | Kurzfristig | Operativ / iterativ |

**Identifiziertes Gap:** Entscheidungen entstehen *zwischen* diesen Layern. Strategische Motive verschwinden. Gedankengänge gehen verloren. Niemand — weder Mensch noch Agent — kann später rekonstruieren: *„Warum haben wir das eigentlich so entschieden?"*

Das Workpaper ist dafür zu strukturiert. Das Whitepaper ist dafür zu stabil.

**Entscheidung (2026-02-26):** Das Gap wird geschlossen. Diary ist **verpflichtender dritter Dokumentations-Layer**. Optional ist Aufgeben.

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

Dokumentationspflicht — aber mit minimalen Regeln. Die Pflicht gilt dem *Vorhandensein*, nicht der *Perfektion*.

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

*(mit LTM-Kontext bewertet am 2026-02-26)*

| Frage | LTM-Kontext | Bewertung / Verdict |
|---|---|---|
| **Zugehörigkeit:** `WORKING/DIARY/` vs. Repo-Root | WORKING/ ist der definierte Agent-Workspace (WP-001 §4, LTM #007). Repo-Root soll sauber bleiben. | ✅ `WORKING/DIARY/` — konsistent mit AAMS-Workspace-Prinzip |
| **LTM-Integration:** Ingest in ChromaDB? | LTM-Architektur: Audit-Log (Git) + Vektorspeicher (ChromaDB). Beide Layers verbindlich (LTM #022). Kurze narrative Entries sind hochwertiger ChromaDB-Input (hohe Signaldichte). | ✅ Ja — after-session-ingest. Diary-Chunks sind prime LTM-Material. |
| **Agent-Schreibrecht:** Nur Human oder auch Agent? | AAMS-Prinzip: Agent dokumentiert jede Entscheidung (Session Contract, READ-AGENT.md). Diary-Einträge bei Architektur-Entscheidungen sind natürliche Agent-Outputs. | ✅ Beide. Agent schreibt Rationale-Entries bei Arch-Entscheidungen. Human schreibt strategische Reflexionen. |
| **SPEC.md-Aufnahme** | Drei-Schichten-Modell ist "Herzstück" (WP-001 §4, LTM #007). Diary ist additiv, kein Ersatz. | ✅ Ja, als **mandatory** 4. Layer. Optional ist Aufgeben. Drei Regeln — aber verbindlich. |
| **Schema-Update** | AGENT.json `workspace.structure` definiert alle Pfade (LTM #003, #015). | ✅ `diary_path: "./WORKING/DIARY/"` — **required**, fester Default. |
| **Einstiegsdatei** | AAMS-Prinzip "Bootstrap creates, never destroys" — idempotent (WP-001 §7). Leere Dummy-Dateien widersprechen diesem Prinzip. | ✅ Lazy creation — Datei entsteht beim ersten Eintrag. Bootstrap erstellt nur `WORKING/DIARY/` als Ordner. |

---

## LTM-Query (durchgeführt 2026-02-26)

**Query-Kontext:** "Diary Layer Temporal Context Dokumentation Layer Architektur"

| LTM-Eintrag | Relevanz | Aussage |
|---|---|---|
| #007 / WP-001 | Hoch | Drei-Schichten-Modell als "Herzstück": Workpaper / Whitepaper / Memory. Diary = 4. Layer — kein Konflikt, sondern Ergänzung auf neuer Zeitachse. |
| #022 | Hoch | Dual-LTM-Architektur: Audit-Log (Git) + ChromaDB. Diary ist naturgemäß LTM-Material — kurze, hochverdichtete Entries. |
| #048 | Direkt | Issue #5: "Running Log" in Workpaper-Template eingefügt. Diese Lösung deckt *intra-session* Gedanken. Diary deckt *inter-session* Narrative. Kein Overlap — Komplementarität. |
| WP-001 §7 | Mittel | Kernprinzipien: Deklarativ, Idempotent, Nie löschen, Secret-frei, Local-first, Portabel. Diary verletzt keines davon. |
| READ-AGENT.md | Mittel | Agent Contract: Session start → session end. Kein expliziter "zwischen Sessions"-Kanal. Diary füllt genau diesen Kanal. |

**LTM-Fazit:** Konzept ist kontexttreu. Kein Widerspruch zur bestehenden Architektur. Vier-Schichten ist die Entscheidung — Whitepaper / Workpaper / Diary / Memory. Alle vier mandatory.

---

## Kontexttreue-Check (AAMS-Philosophie)

| AAMS-Prinzip | Diary-Konzept | Bewertung |
|---|---|---|
| **Explicit over implicit** | Diary macht implizite Gedanken explizit | ✅ Voll konform |
| **Workspace-driven** | Liegt in `WORKING/DIARY/` — Teil des definierten Workspace | ✅ Konform |
| **Continuity** | Genau das ist der Zweck: Kontext über Sessions erhalten | ✅ Kernmotivation des Konzepts |
| **Local-first** | Markdown-Dateien, kein Service, kein API | ✅ Konform |
| **Machine-readable** | Narrativ → ChromaDB-Ingest macht es querybar | ✅ Mit Ingest konform |
| **Versionable** | In Git, monatsweise Dateien = saubere History | ✅ Konform |
| **Extensible ohne Core-Break** | Diary wird Teil des Mandatory-Core — Core wächst um eine Zeitachse | ✅ Konform |

**Spannungspunkt aufgelöst:** "Kernregel: Nicht überregeln" gilt für den *Inhalt* des Diary, nicht für dessen *Existenz*. Drei Regeln, verbindlich. Diary-Sektion in SPEC.md kurz halten.

---

## Abgrenzung: Running Log vs. Diary

*(nach Issue #5 / LTM #048 — jetzt explizit nötig)*

| Dimension | Running Log (Workpaper §2) | Diary |
|---|---|---|
| **Scope** | Intra-session | Inter-session / zeitübergreifend |
| **Format** | Tabelle, strukturiert | Freitext, Telegrammstil |
| **Inhalt** | Was ich gerade tue | Warum ich das tue / was mich dabei beschäftigt |
| **Zeitpunkt** | Während der Session | Zwischen Sessions, bei Erkenntnissen |
| **Autor** | Agent primär | Mensch primär, Agent sekundär |
| **Leser** | Nächste Session dieses Projekts | Zukunft — nach Wochen/Monaten |
| **Pflicht** | Ja (ab Issue #5) | **Ja** (ab Diary-Einführung) |

---

## Vorläufige Entscheidungen

*(2026-02-26)*

| Entscheidung | Status |
|---|---|
| Diary liegt in `WORKING/DIARY/` | ✅ Entschieden |
| Monatsweise Dateien (`2026-02.md`) | ✅ Entschieden |
| Lazy creation — kein Bootstrap-Leer-File | ✅ Entschieden |
| Ingest in ChromaDB nach jeder Diary-Ergänzung | ✅ Entschieden |
| **Mandatory** 4. Layer in SPEC.md — kein Optional | ✅ Entschieden |
| Drei Regeln maximal — Pflicht gilt dem Vorhandensein, nicht der Perfektion | ✅ Entschieden |
| **Vier-Schichten-Modell**: Whitepaper / Workpaper / Diary / Memory — alle mandatory | ✅ Entschieden |
| `diary_path` als **required** Feld in AGENT.json/Schema | ⏳ Ausstehend — nächste SPEC-Session |

---

## Next Steps

- [ ] SPEC.md: Neuen **mandatory** Abschnitt "Diary Layer (Temporal Context)" — max. 1 Seite, drei Regeln, gleicher Rang wie Workpaper/Whitepaper
- [ ] AGENT.json: `workspace.diary_path` als **required** Feld
- [ ] AGENT_SCHEMA.json: `diary_path` als required ergänzen
- [ ] Bootstrap: Schritt `create_diary_folder` (Ordner anlegen, keine Datei)
- [ ] Erstes Diary-File anlegen: `WORKING/DIARY/2026-02.md`

---

## File Protocol

| Action | File | Detail |
|---|---|---|
| CREATE | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` | Initiales Workpaper (2026-02-24) |
| EDIT | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` | Review 2026-02-26: LTM-Query, Kontexttreue-Check, Abgrenzung Running Log/Diary, Fragen mit Verdicts, Entscheidungen getroffen |
| EDIT | `WORKING/WORKPAPER/2026-02-24-diary-layer-konzept.md` | Entscheidung 2026-02-26: optional → **mandatory**. Vier-Schichten-Modell beschlossen. |
