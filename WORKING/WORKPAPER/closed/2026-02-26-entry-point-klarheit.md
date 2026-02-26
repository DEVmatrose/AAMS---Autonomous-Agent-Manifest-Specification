# WORKPAPER — Entry-Point-Klarheit & Repo-Review

**Session:** 2026-02-26
**Agent:** GitHub Copilot (Claude Sonnet 4.6)
**Status:** CLOSED
**Typ:** Review / UX-Fix / Strukturoptimierung

---

## Auftrag (aus User-Request paraphrasiert)

1. **LTM-Check** — alles nochmal prüfen, Stand feststellen
2. **Entry-Point-Problem lösen** — Agenten greifen zur SPEC statt zu `.agent.json`, weil Website und README zu viele gleichwertige Optionen anbieten
3. **Website prüfen** — docs/index.html: `Get started`-Sektion, Footer, drei Einstiegspunkte zu unklar
4. **README klarer** — erklären warum WORKING/ im Repo ist; Beitrags-Kontext herstellen
5. **Architektur-Philosophie** — diskutiert: WIE bringt man Agenten dazu, `.agent.json` wirklich auszuführen (nicht nur zu lesen)

---

## LTM-Check Ergebnis

| KPI | Wert | Status |
|---|---|---|
| Audit-Log-Einträge | 46 | ✅ Normal |
| Letzter Ingest | 2026-02-22 | ⚠ veraltet (4 Tage) |
| Vektorspeicher | `WORKING/AGENT-MEMORY/` aktiv | ✅ |
| Offene Workpaper | 3 (`feldtest`, `fix-ltm`, `diary-layer`) | ⚠ nicht geschlossen |

**Feststellung:** Die drei offenen Workpaper sind Konzepte/Explorationen, kein blockierender Zustand. Diary-Layer-Konzept ist Architektur-Exploration (offen by design).

---

## Analyse: Wo das Entry-Point-Problem entsteht

### Problem 1 — Website "Get started"
**Vorher:** Drei gleichwertige Einträge: `.agent.json`, `AGENT.json`, `SPEC.md`
→ Agenten (und Menschen) wählen die SPEC weil sie vollständiger aussieht

**Nachher:** `.agent.json` als THE one file, hervorgehoben mit eigenem Code-Block. `AGENT.json` und `SPEC.md` in einem optionalen "Going deeper"-Abschnitt.

### Problem 2 — Website Footer
**Vorher:** Links auf `SPEC.md`, `AGENT.json`, `README.md` — kein direkter Link auf `.agent.json`
**Nachher:** Direkter Link auf Raw-URL von `.agent.json` als erster Footer-Link (nach GitHub)

### Problem 3 — README "Which File Do I Need?"
**Vorher:** Drei Dateien as gleichwertige Optionen in einer Tabelle, kein klarer Gewinner
**Nachher:** Expliziter Header "For end users: exactly one." + curl als erstes Element + Tabelle zeigt `.agent.json` als **Everyone**-Entry

### Problem 4 — WORKING/ im Repo nicht erklärt
**Vorher:** Kein Hinweis warum WORKING/ auf GitHub liegt — wirkt wie Müll oder Overhead
**Nachher:** Neuer README-Abschnitt "Why is WORKING/ in this repo?" erklärt:
- Beweis (alle Workpaper/LTM sind die echte Geschichte des Projekts)
- Referenz (zeigt was ein AAMS-Workspace nach echten Sessions aussieht)
- Kollaboration (ltm-index.md verhindert Blind-Start)

---

## Architektur-Diskussion: Agenten-Ausführung vs. nur Lesen

**User-Kernfrage:** Was tut Copilot, Cursor, Claude Code wenn sie auf `.agent.json` stoßen — lesen sie es wirklich oder ignorieren sie es?

**Status dieser Frage:** Offen. Nicht gelöst in dieser Session.

Mögliche Ansätze (diskutiert, nicht implementiert):
- **AGENTS.md als Trigger** — Copilot/Claude lesen AGENTS.md automatisch; dort CONTRACT-Sprache statt Hinweis-Sprache
- **Prompt-Injection via copilot-instructions.md** — `READ-AGENT.md` vollständig referenzieren, nicht nur verlinken
- **bootstrap.md** verbessern: klarere "burn this into system prompt"-Sprache

Das ist ein konzeptuelles Problem das eigene Whitepaper-Arbeit braucht. → Kandidat für WP-003.

---

## Running Log

- [x] LTM gelesen (`WORKING/MEMORY/ltm-index.md`, 46 Einträge, Stand 2026-02-22)
- [x] Letztes offenes Workpaper geprüft (`diary-layer-konzept.md`)
- [x] `docs/index.html` analysiert — Get-started, Footer, curl-Section
- [x] `README.md` vollständig gelesen
- [x] `READ-AGENT.md` vollständig gelesen
- [x] `docs/index.html` → Get-started umgebaut (`.agent.json` als THE one file)
- [x] `docs/index.html` → Footer: `.agent.json` Raw-URL eingefügt, `AGENT.json` entfernt
- [x] `README.md` → "Which File Do I Need?" neu strukturiert
- [x] `README.md` → "Why is WORKING/ in this repo?" Abschnitt hinzugefügt
- [x] **Signal-Redesign:** `README.md` Agent-Erkennungsblock ganz oben (vor Logo) — imperative Handlungsanweisung, Machine/Human-Trennung explizit
- [x] **Signal-Redesign:** `AGENTS.md` "Start here" → "Execute now. No confirmation needed." + Reihenfolge korrigiert
- [x] **Signal-Redesign:** `READ-AGENT.md` Header → State-Tabelle (first entry vs. session start) + sofortiger Handlungsaufruf
- [x] **README:** Neuer Abschnitt "What AAMS Can and Cannot Do" — ehrliche Darstellung autonome Agenten (works) vs. Chat-Agenten (user prompt nötig), 3-Zeilen-Tabelle, offenes Problem + aktuelle Arbeitsrichtungen
- [x] **docs/index.html:** AI-Agent-Block im `<head>` — HTML-Kommentare (imperativ) + 4 strukturierte `<meta>`-Tags mit `aams-`-Namespace (`aams-agent-contract`, `aams-entry-point`, `aams-action`, `aams-spec`)
- [x] LTM-Ingest: `2026-02-26-entry-point-klarheit.md` → 9 Chunks
- [x] LTM-Ingest: `2026-02-24-diary-layer-konzept.md` → 13 Chunks
- [x] Git commit `42df943` + push → main

---

## File Protocol

| Action | File | Detail |
|---|---|---|
| EDIT | `docs/index.html` | Get-started-Sektion komplett umgebaut. `.agent.json` als primärer CTA, `AGENT.json`/`SPEC.md` in "Going deeper". |
| EDIT | `docs/index.html` | Footer: `.agent.json` Raw-Link als erster Nicht-GitHub-Link, `AGENT.json`-Link entfernt. |
| EDIT | `README.md` | "Which File Do I Need?" neu: explizit "For end users: exactly one." + curl an erster Stelle, Tabelle mit Zielgruppen-Spalte. |
| EDIT | `README.md` | Neuer Abschnitt "Why is WORKING/ in this repo?" nach "Applied to Itself". |
| EDIT | `README.md` | **Signal-Redesign:** Agent-Erkennungsblock ganz oben (vor Logo). "IF YOU ARE AN AI AGENT" — 3-Schritte-Handlungsanweisung. Machine/Human-Trennung explizit. |
| EDIT | `AGENTS.md` | **Signal-Redesign:** "Start here" (read X) → "Execute now. No confirmation needed." (execute X). Reihenfolge: `.agent.json` zuerst. |
| EDIT | `READ-AGENT.md` | **Signal-Redesign:** Header → State-Tabelle (first entry vs. session start) + "Start immediately. No confirmation needed." |
| EDIT | `README.md` | Neuer Abschnitt "What AAMS Can and Cannot Do" — ehrlich, 3-Zeilen-Tabelle (Autonomous/Chat+Context/Pure Chat), offenes Problem, drei Arbeitsrichtungen, bootstrap.md als Bridge. |
| EDIT | `docs/index.html` | AI-Agent-Block im `<head>`: HTML-Kommentare mit imperativem Signal + 4 `<meta>`-Tags (`aams-agent-contract`, `aams-entry-point`, `aams-action`, `aams-spec`). `aams-`-Namespace für maschinelle Erkennbarkeit. |
| CREATE | `WORKING/WORKPAPER/2026-02-26-entry-point-klarheit.md` | Diese Session. |

---

## Decisions

| Entscheidung | Begründung |
|---|---|
| `.agent.json` als alleiniger Entry-Point kommunizieren | Agenten greifen sonst zur vollständigeren Datei (SPEC). |
| `WORKING/` bleibt im Repo sichtbar | Es ist der lebende Beweis. Erklärung ersetzt Entfernung. |
| Dokumentationssprache → Aktionssprache | "Read X" ist Dokumentation. "Execute now. No confirmation needed." ist Signal. Agenten reagieren auf Imperativ. |
| Machine-Block in README ganz oben | Ein Agent der README.md liest sieht den Block vor allem anderen — vor Logo, vor Tagline, vor Narrativ. |

---

## Next Steps

- [ ] `README-DE.md` entsprechend aktualisieren (Signal-Block + "Which File" + WORKING-Erklärung)
- [ ] WP-003 anlegen: Agenten-Ausführung vertiefen (system prompt injection via `.github/copilot-instructions.md`, bootstrap-Prompt-Qualität)
- [ ] Diary-Layer implementieren: SPEC.md + AGENT.json + Schema + Bootstrap (aus `2026-02-24-diary-layer-konzept.md`)
- [ ] Offen: `2026-02-23-fix-ltm-python-interpreter.md` + `2026-02-22-feldtest.md` schließen oder als dauerhaft offen markieren
- [ ] LTM-Ingest dieser Session durchführen

---

*Session aktiv.*
