# LTM — Long-Term Memory Index
## Autonomous Agent Manifest Specification

> Dieser Index dokumentiert was im LTM gespeichert ist, wann es ingested wurde und was der Inhalt ist.
> Jeder Agent pflegt diesen Index bei jedem Ingest-Vorgang.

---

## ⚠️ Schwellenwert-Regel (verbindlich)

| Einträge | Zustand | Pflichtaktion |
|---|---|---|
| < 100 | Markdown-Index ausreichend | Weiter pflegen |
| ≥ 90 | **Warnung** | Agent informiert Entwickler aktiv: Migration zu Vektorspeicher empfohlen |
| ≥ 100 | **Kritisch** | Agent lädt nur die letzten 20 Einträge — älterer Kontext ist blind. Migration überfällig. |

**Warum:** Ab 100 Einträgen ist der vollständige Index zu groß für einen Agenten-Kontext. Jeder vollständige Abruf erzeugt enormen Overhead. Ältere Einträge werden de facto unsichtbar.

**Empfohlene Backends:** ChromaDB (lokal), LanceDB, SQLite-VSS, pgvector

**Agent-Pflicht ab Eintrag 90:**
> *„Der LTM-Index nähert sich dem Schwellenwert (aktuell: N Einträge). Ab 100 Einträgen wird ein Vektorspeicher-Backend benötigt. Empfehlung: ChromaDB unter `./WORKING/AGENT-MEMORY/` einrichten."*

---

## Status

- **Initialisiert:** 2026-02-22
- **Letzter Ingest:** 2026-02-22 (Session-Update)
- **Einträge gesamt:** 19

---

## Index

| # | Datum | Typ | Datei | Inhalt |
|---|---|---|---|---|
| 001 | 2026-02-22 | SPEC | `SPEC.md` | Vollständige AAMS-Spezifikation (englisch). |
| 002 | 2026-02-22 | SPEC | `SPEC-DE.md` | Vollständige AAMS-Spezifikation (deutsch). |
| 003 | 2026-02-22 | MANIFEST | `AGENT.json` | Referenz-Manifest AAMS/1.0. Fix: `whitepapers` auf `./WORKING/WHITEPAPER`. |
| 004 | 2026-02-22 | SCHEMA | `AGENT_SCHEMA.json` | JSON Schema für AGENT.json Validierung. |
| 005 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-bootstrap-session.md` | Bootstrap-Session. Workspace-Struktur angelegt. |
| 006 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-repo-analyse.md` | Repo-Analyse. Inventar, Issues #1-#3 gelöst. |
| 007 | 2026-02-22 | WHITEPAPER | `WORKING/WHITEPAPER/WP-001-aams-overview.md` | Erstes Whitepaper. Projektübersicht, Dreischichtenmodell, Bootstrap-Ablauf. |
| 008 | 2026-02-22 | ENTRY | `READ-AGENT.md` | Agent-Einstiegspunkt mit vollem Agent Contract und LTM-Trigger-Tabelle. |
| 009 | 2026-02-22 | README | `README-DE.md` | Neue README (deutsch). Positionierung, kein technisches Overload. Verweist auf SPEC-DE. |
| 010 | 2026-02-22 | README | `README.md` | Neue README (englisch). Exakte Übersetzung von README-DE. |
| 011 | 2026-02-22 | README | `README-CH.md` | Neue README (Mandarin). Exakte Übersetzung. |
| 012 | 2026-02-22 | TEMPLATE | `templates/read-agent-template.md` | Pfade korrigiert, Agent Contract + LTM-Trigger ergänzt. |
| 013 | 2026-02-22 | BRIDGE | `AGENTS.md` | Tool-Bridge. Single Source of Truth für Copilot, Cursor, Claude Code, Codex, Windsurf, Aider, Continue.dev. Verweist auf READ-AGENT.md + AGENT.json. |
| 014 | 2026-02-22 | CONFIG | `.github/copilot-instructions.md` | Thin redirect zu AGENTS.md. Existiert nur weil Copilot dort sucht. |
| 015 | 2026-02-22 | SKILL | `AGENT.json` (`skills.custom_skills`) | `bootstrap_workspace` Skill eingetragen. Input: `{repo_root, dry_run}`. Output: `{created_dirs, created_files, skipped, warnings}`. Idempotent. |
| 016 | 2026-02-22 | ARCHIVE | `archive/blog-artikel.md` | `blog-artikel.md` archiviert. Inhalt funktional ersetzt durch README-DE.md. Kein aktiver Teil des Standards. |
| 017 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/` | Session-Close: beide Workpaper (bootstrap-session + repo-analyse) nach closed/ verschoben. LTM auf 17 Einträge. |
| 018 | 2026-02-22 | REVIEW | root | Hartes Review: README-CH.md nach archive/ verschoben. 6 Pfadfehler in SPEC.md + SPEC-DE.md korrigiert: `./WORKING/docs`→`WHITEPAPER`, `close`→`closed`, `AGENT-MEMORY`→`MEMORY`. |
| 019 | 2026-02-22 | DECISION | `.gitignore` + `.agent.json` | Gitignore-Architekturentscheidung: `WORKING/MEMORY/` nicht mehr ignoriert (ltm-index.md ist Kollaborationsartefakt). `WORKING/LOGS/` bleibt ignoriert. Vektorspeicher-Patterns auskommentiert vorbereitet. Stale-Einträge entfernt. |

---

## Kernerkenntnis (extrahiert aus allen Quellen)

### Was AAMS ist
- Kein Framework. Kein Tool. Kein Runtime.
- Ein **deklarativer Architekturstandard** der in jedem Repo als Datei existiert.
- Besteht aus zwei Dateien: `AGENT.json` (voll) + `.agent.json` (minimal/portabel).

### Drei-Schichten-Dokumentationsmodell
1. **Workpaper** — sessiongebunden, operativ, wird nach Abschluss archiviert
2. **Whitepaper** — stabile Systemwahrheit, architektonisch, nie gelöscht
3. **Memory (LTM)** — persistenter Kontextspeicher über Sessions hinweg

### Offene Issues (Stand 2026-02-22)
- **Issue #1 — Secret Exclusion:** Im Manifest adressiert (`secrets_policy`, `can_read_secrets=false`). Gilt als gelöst.
- **Issue #2 — Projektanalyse-Struktur:** Durch `workspace.onboarding.steps` + erstes Workpaper adressiert.
- **Issue #3 — Strukturelle Unschärfen:** Durch klare Schichtentrennung (Workpaper/Whitepaper/Memory) + Agent Contract in READ-AGENT.md adressiert.

### Bootstrap-Ablauf (normativ)
1. `.agent.json` lesen
2. Struktur prüfen / anlegen
3. Repository scannen
4. READ-AGENT.md lesen/erstellen
5. Erstes Workpaper mit Analyse erstellen
6. LTM initial befüllen

---

## Backend-Status

| Backend | Status | Pfad |
|---|---|---|
| Markdown-Index | ✅ Aktiv | `WORKING/MEMORY/ltm-index.md` |
| Vektorspeicher | ⬜ Nicht eingerichtet | `WORKING/AGENT-MEMORY/` |

> Vektorspeicher wird ab **100 Einträgen** Pflicht. Aktuell: **12 Einträge**.

---

## Nächster geplanter Ingest

Nach Abschluss der laufenden Session.
