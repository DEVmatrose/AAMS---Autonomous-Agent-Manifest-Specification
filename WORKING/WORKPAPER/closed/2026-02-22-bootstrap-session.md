# Workpaper: 2026-02-22 — Bootstrap Session

- **Date:** 2026-02-22
- **Agent:** GitHub Copilot / Claude Sonnet 4.6
- **Topic:** Bootstrap — AAMS eigener Workspace

---

## Session Scope

Initialer Bootstrap des AAMS-Projekts mit dem eigenen Standard.  
Wir testen den Standard an uns selbst: Das Projekt, das den Standard beschreibt, wird das erste Projekt, das ihn live anwendet.

---

## Goal (one sentence)

Workspace-Struktur gemäß `.agent.json` anlegen und den Bootstrap-Prozess als funktionalen Beweis des Standards dokumentieren.

---

## Context from previous sessions

Keine. Dies ist Session 1.

Vorangegangene Analyse:
- AGENT.json vollständig vorhanden (AAMS/1.0)
- AGENT_SCHEMA.json vollständig vorhanden
- SPEC.md / SPEC-DE.md vorhanden
- Offene Issues: Secret Exclusion, Projektanalyse-Struktur, Strukturelle Unschärfen — alle im Manifest bereits adressiert
- Konzeptionelle Verschiebung abgeschlossen: Manifest = Architekturskill, kein Framework

---

## Session Overview

1. `.agent.json` (Minimal-Form) erstellt — portabler Bootstrap-Contract für jedes Repo
2. WORKING-Struktur angelegt (idempotent, via PowerShell, entspricht `.agent.json`)
3. `READ-AGENT.md` erstellt — Entry Point für jeden Agenten der dieses Repo betritt
4. Dieses Workpaper erstellt

---

## Results

- `.agent.json` existiert → portable Minimal-Form des Standards
- `WORKING/` Struktur vollständig:
  - `WHITEPAPER/`
  - `WORKPAPER/` + `WORKPAPER/closed/`
  - `MEMORY/`
  - `LOGS/`
  - `GUIDELINES/`
  - `TOOLS/`
- `READ-AGENT.md` existiert → jeder Agent weiß sofort wo er ist

---

## File Protocol

| Action | File |
|---|---|
| CREATED | `.agent.json` |
| CREATED | `READ-AGENT.md` |
| CREATED | `WORKING/WHITEPAPER/` |
| CREATED | `WORKING/WORKPAPER/` |
| CREATED | `WORKING/WORKPAPER/closed/` |
| CREATED | `WORKING/MEMORY/` |
| CREATED | `WORKING/LOGS/` |
| CREATED | `WORKING/GUIDELINES/` |
| CREATED | `WORKING/TOOLS/` |
| CREATED | `WORKING/WORKPAPER/2026-02-22-bootstrap-session.md` (this file) |

---

## Decisions and Rationale

| Decision | Rationale |
|---|---|
| `.agent.json` als separate Minimal-Datei neben `AGENT.json` | `AGENT.json` ist vollständiges Manifest. `.agent.json` ist die kleinste portable Form — nur Bootstrap-Contract. Jedes Repo kann `.agent.json` einbinden ohne das volle Manifest zu übernehmen. |
| Kein Python-Script als primärer Bootstrap | Standard ist deklarativ, nicht tool-gebunden. Ein Agent liest `.agent.json` und versteht direkt was zu tun ist — unabhängig von Sprache oder Framework. |
| Drei-Schichten-Dokumentationsmodell verbindlich | Workpaper/Whitepaper/Memory ist der einzige bewiesene Weg um Kontextverlust über Sessions zu verhindern. |

---

## Next Steps

- [ ] `.gitignore` um `WORKING/MEMORY/` und `WORKING/LOGS/` ergänzen
- [ ] Erstes Whitepaper: AAMS-Architekturübersicht in `WORKING/WHITEPAPER/`
- [ ] `bootstrap_workspace` als formalen Skill in `AGENT.json` eintragen
- [ ] `.agent.json` als eigenständigen Standard im README positionieren

---

## Session Closing Checklist

- [x] File protocol complete
- [x] No secrets in this workpaper
- [x] Next steps konkret formuliert
- [ ] LTM ingest (MEMORY noch leer — wird mit erstem Whitepaper ausgeführt)
