# LTM — Audit-Log
## Autonomous Agent Manifest Specification

> **Dieses Dokument ist das menschenlesbare Audit-Log des LTM.**  
> Das query-fähige LTM liegt unter `WORKING/AGENT-MEMORY/` (ChromaDB oder kompatibel).  
> Jeder Agent ingested nach jeder Session in beide: den Audit-Log (hier) und den Vektorspeicher.

---

## LTM-Architektur

| Komponente | Pfad | Zweck |
|---|---|---|
| Audit-Log | `WORKING/MEMORY/ltm-index.md` | Menschenlesbar. Was wurde wann ingested. Immer im Git. |
| Vektorspeicher | `WORKING/AGENT-MEMORY/` | Querybar. Semantische Suche. Ab Session 1 aktiv. In `.gitignore`. |

**Warum beides:** Der Audit-Log ist die Wahrheit die Menschen lesen können. Der Vektorspeicher ist die Wahrheit die Agenten effizient abfragen können. Ohne Vektorspeicher degradiert jede LTM-Abfrage ab ~100 Einträgen zur Blindheit.

**Empfohlenes Backend:** ChromaDB (lokal, kein API-Key, Open Source)  
**Setup:** `pip install chromadb` → `WORKING/AGENT-MEMORY/` wird automatisch angelegt beim ersten Ingest.

**Fallback ohne Vektorspeicher:**

| Einträge | Zustand | Was der Agent tut |
|---|---|---|
| < 90 | Normal | Audit-Log vollständig laden |
| ≥ 90 | **Warnung** | Agent meldet: Vektorspeicher fehlt, Kontext wird bald blind |
| ≥ 100 | **Blind** | Agent lädt nur die letzten 20 Einträge — ohne Vektorspeicher gibt es keine andere Option |

**Agent-Pflicht ab Eintrag 90 (wenn kein Vektorspeicher vorhanden):**
> *„Der LTM-Audit-Log hat aktuell N Einträge. Kein Vektorspeicher gefunden unter `WORKING/AGENT-MEMORY/`. Ab 100 Einträgen ist älterer Kontext blind. Bitte `pip install chromadb` ausführen — der Agent ingested beim nächsten Sessionstart automatisch."*

---

## Status

- **Initialisiert:** 2026-02-22
- **Letzter Ingest:** 2026-02-22 (Session-Update)
- **Einträge gesamt:** 34

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
| 020 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-hartes-review-v1.md` | Hartes Review erfasst und bewertet. 8 Kritikpunkte gewichtet, 4 rote Prioritäten identifiziert. |
| 021 | 2026-02-22 | README | `README.md` + `README-DE.md` | 4 rote Prioritäten umgesetzt: Tagline geändert, Cross-Tool-Sektion als Lead, Hierarchie-Tabelle, Proof-Abschnitt ehrlich umformuliert. DE von EN abgeleitet. |
| 022 | 2026-02-22 | DECISION | `ltm-index.md` + `.agent.json` + `AGENT.json` | Dual-Layer-LTM-Architektur: `ltm-index.md` = Audit-Log (Git), `WORKING/AGENT-MEMORY/` = ChromaDB (Sessions 1+). ChromaDB als Disziplin ab Session 1, nicht als Fallback. |
| 023 | 2026-02-22 | SPEC | `SPEC-DE.md` | Alle ~10 fehlenden Abschnitte vs. SPEC.md ergänzt: governance-Hinweis, auto_create false-Modus, Whitepaper-Index/Guidelines-Empfehlungen, Schritt-Reihenfolge, workpaper_rules (template_file_quick, Vollversion/Kurzvorlage, Nesting, Metadata-Header), file_tracking (track_moved, track_archived), _ref-Linting, Schema-Striktheitstabelle, Zukünftige Profile Vorbedingungen. 727→809 Zeilen. |
| 024 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/2026-02-22-hartes-review-v1.md` | Session-Close: hartes-review Workpaper abgeschlossen und nach closed/ verschoben. `AGENT.json` `_spec_url_status: planned` ergänzt. LTM auf 24 Einträge. |
| 025 | 2026-02-22 | TOOL | `WORKING/TOOLS/ltm_chroma.py` | ChromaDB Tool implementiert. Hash-128 Embedding (kein ML, kein Download). Bug gefixt: Endlosschleife in `chunk_by_size`. Bulk-Ingest: 11 Dateien, 114 Chunks. Query-Test erfolgreich. AGENT-MEMORY aktiv. |
| 026 | 2026-02-22 | PAGES | `docs/index.html` | GitHub Pages One-Pager erstellt. Dark theme, zero dependencies, Copy-Button, mobile-ready. 7 Sektionen: Problem, curl, Steps, Tools, Proof, Get started, Footer. GitHub Pages Setup ausstehend (manuell). |
| 027 | 2026-02-22 | SESSION | `WORKING/WORKPAPER/closed/2026-02-22-github-pages-onepager.md` | GitHub Pages Session abgeschlossen. `docs/index.html` fertig, abgenommen. Workpaper nach closed/. |
| 028 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-feldtest-independentes-repo.md` | Feldtest-Workpaper angelegt. Testplan, Hypothesen, Beobachtungs-Tabelle. Ausstehend: echtes externes Repo. |
| 029 | 2026-02-22 | COMMIT | `600f40c` | Repo umbenannt zu `AAMS---Autonomous-Agent-Manifest-Specification`. Git remote aktualisiert. Alle placeholder URLs (`aams-spec/aams`) ersetzt. GitHub Pages Link in README.md + README-DE.md an zentraler Stelle eingefügt. `_spec_url_status` entfernt (URL live). |
| 030 | 2026-02-22 | DECISION | `WORKING/WORKPAPER/closed/2026-02-22-ltm-versionierung-git-chroma-sync.md` | Entscheidung: kein Git-in-Git. Git ist bereits als Versionierung vorhanden (`ltm-index.md` in Git = vollständige History). Echter Gap: ChromaDB-Rebuild nach Datenverlust. Lösung: `ltm-rebuild.py` in `WORKING/TOOLS/` — deterministischer Rebuild aus `ltm-index.md`. Workpaper geschlossen. |
| 031 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-issue-1-security-secret-exclusion-policy.md` | Workpaper für Issue #1 angelegt. 7 DoD-Punkte: gitignore_patterns erweitern, permissions härten, ltm_triggers Pre-Save-Scan, AGENT_SCHEMA.json output_validation, SPEC.md Sektion, Templates-Update, .gitignore prüfen. |
| 032 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-issue-2-project-analysis-template.md` | Workpaper für Issue #2 angelegt. 5 DoD-Punkte: project-analysis-template.md erstellen, SPEC.md "Before You Write a Manifest", onboarding Step 0, README Verweis, AGENT_SCHEMA.json project_analysis_path. |
| 033 | 2026-02-22 | WORKPAPER | `WORKING/WORKPAPER/2026-02-22-issue-3-spec-luecken.md` | Workpaper für Issue #3 angelegt. 8 Lücken analysiert und priorisiert: _doc-Convention, onboarding Action-Enum, workpaper_path Variablen, closing_checklist Registry, fallback_providers Priorität, session.workpaper_template, LTM-Migration, capabilities-Registry. |
| 034 | 2026-02-22 | SECURITY | `AGENT.json` + `AGENT_SCHEMA.json` + `SPEC.md` + `templates/` + `.gitignore` | Issue #1 umgesetzt: 7 DoD gescored. gitignore_patterns (+8 Secret-Muster), restricted_write für .gitignore, ltm_triggers workpaper_pre_save+scan_secrets, AGENT_SCHEMA output_validation+forbidden_patterns, SPEC.md output_validation-Untersektion + H2 "Absolute Secret Exclusion Policy" (3-Layer-Modell, Risk-Matrix, Pre-Commit-Hook-Implementierung), beide Templates aktualisiert. |
| 035 | 2026-02-22 | TEMPLATE | `templates/project-analysis-template.md` + `SPEC.md` + `AGENT.json` + `AGENT_SCHEMA.json` + `README.md` | Issue #2 umgesetzt: 5 DoD. Neues Template (9 Sektionen, Tabellen-Format, Affects-Hinweise). SPEC.md: H2 "Before You Write a Manifest" vor Structure Overview. AGENT.json: onboarding Step 0 read_project_analysis (condition: file_exists, priority: mandatory_if_present). AGENT_SCHEMA.json: project_analysis_path optional field. README.md: Verweis für Existing-Project-Onboarding. |
| 036 | 2026-02-22 | SPEC | `SPEC.md` + `AGENT_SCHEMA.json` + `registry/capabilities.md` | Issue #3 umgesetzt: 8 Lücken. L1: _doc-Convention-Abschnitt. L2: read_project_analysis+file_exists in Enum+Tabelle, priority-Feld. L3: Template-Variable-Tabelle ({date}=YYYY-MM-DD, {agent}=kebab, {topic}=kebab). L4: 7 Standard-Closing-Checklist-Items. L5: fallback_providers (Array-Pos=Priorität) in SPEC+Schema. L6: bereits implementiert (template_file). L7: LTM-Migration-Prozedur (5 Schritte, _migration-Annotation, ltm-rebuild.py-Verweis). L8: registry/capabilities.md erstellt (9 Kategorien, 30+ Capabilities, URL in SPEC aktualisiert). |

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
| Vektorspeicher | ✅ Aktiv | `WORKING/AGENT-MEMORY/` — 114 Chunks, Hash-128 Embedding |

> Hash-128 Embedding (pure Python, kein ML). Wechsel zu semantischem Embedding: `reset` + `bulk-ingest`.

---

## Nächster geplanter Ingest

Nach Abschluss der laufenden Session.
