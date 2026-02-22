# 2026-02-22 — Copilot — Issue #3: 8 konkrete Spec-Lücken

**Project:** Autonomous Agent Manifest Specification  
**Module:** SPEC.md / AGENT_SCHEMA.json / AGENT.json / templates/  
**Status:** ✅ COMPLETED  
**Date:** 2026-02-22  
**GitHub Issue:** https://github.com/DEVmatrose/AAMS---Autonomous-Agent-Manifest-Specification/issues/3  
**Label:** `architecture` `invalid` `spec` — *Hinweis: Label "invalid" ist vom Autor selbst gesetzt, beschreibt aber legitime Spec-Lücken.*

---

## 1. Session Scope

### Kontext

Issue #3 wurde von ogerly beim Implementieren von AAMS in einem eigenen Projekt geöffnet. 8 konkrete Fehlstellen die beim praktischen Einsatz aufgefallen sind. Label `invalid` wurde wahrscheinlich als Selbst-Kommentar gesetzt ("das hätte in der Spec stehen sollen"), nicht als "Issue ist ungültig".

### Ziel dieser Session

Alle 8 Lücken analysieren, priorisieren und umsetzen.

---

## 2. Die 8 Lücken — Analyse & Priorisierung

| # | Lücke | Aufwand | Priorität |
|---|---|---|---|
| 1 | `_doc`-Felder: keine Schema-Convention | Klein | Mittel |
| 2 | `onboarding.steps.action` — kein Enum/Registry | Mittel | Hoch |
| 3 | `workpaper_path` Template-Variablen nicht spec'd | Klein | Hoch |
| 4 | `closing_checklist` items — freie Strings, nicht validierbar | Mittel | Mittel |
| 5 | `fallback_providers` — Reihenfolge/Priorität implizit | Klein | Niedrig |
| 6 | `session.workpaper_template` fehlt in Spec + Schema | Klein | Hoch |
| 7 | LTM-Backend-Migration nicht adressiert | Mittel | Mittel |
| 8 | `skills.capabilities`-Registry ist "coming soon" — blockiert Adoption | Groß | Kritisch |

---

## 3. Lücken im Detail

### Lücke 1 — `_doc`-Convention im Schema
**Problem:** `"additionalProperties": true` nötig damit `_doc`-Felder valid bleiben.  
**Fix:** In `AGENT_SCHEMA.json` → `patternProperties: { "^_": {} }` in jedem Object-Type, oder globale Convention dokumentieren.  
**Betroffene Datei:** `AGENT_SCHEMA.json`, `SPEC.md`

### Lücke 2 — `onboarding.steps.action` — kein Enum
**Problem:** Actions wie `"read_entry_point"`, `"validate_structure"`, `"create_workpaper"` sind erfundene Strings. Kein Runtime kann darauf automatisch reagieren.  
**Fix:** Standard Action-Registry definieren. Enum in Schema. SPEC.md dokumentiert alle validen Actions.  
**Betroffene Datei:** `AGENT_SCHEMA.json`, `SPEC.md`

### Lücke 3 — `workpaper_path` Template-Variablen
**Problem:** `{date}` und `{agent}` stehen in `AGENT.json` ohne Definition welche Variablen existieren und welches Format `{date}` hat.  
**Fix:** In SPEC.md dokumentieren: `{date}` = `YYYY-MM-DD`, `{agent}` = Agent-Name aus `identity.name`, `{topic}` = Session-Topic als kebab-case.  
**Betroffene Datei:** `SPEC.md`

### Lücke 4 — `closing_checklist` items als freie Strings
**Problem:** `"no_secrets_in_files"` etc. sind nicht validierbar und nicht automatisierbar.  
**Fix:** Standard-Registry definieren (wie Capabilities). Schema-Enum für bekannte Items.  
**Betroffene Datei:** `AGENT_SCHEMA.json`, `SPEC.md`

### Lücke 5 — `fallback_providers` Reihenfolge implizit
**Problem:** Array ohne explizites `priority`-Feld — unklar ob nach Array-Position priorisiert wird.  
**Fix:** In SPEC.md dokumentieren dass Array-Position = Priorität (Index 0 = höchste Priorität). Optional `priority`-Feld ergänzen.  
**Betroffene Datei:** `SPEC.md`, ggf. `AGENT_SCHEMA.json`

### Lücke 6 — `session.workpaper_template` fehlt
**Problem:** Feld für Verweis auf Template-Datei fehlt in Spec + Schema — aber praktisch gebraucht.  
**Fix:** Feld in `workspace.workpaper_rules` ergänzen (bereits als `template_file` dokumentiert? → prüfen), SPEC.md und Schema synchronisieren.  
**Betroffene Datei:** `AGENT_SCHEMA.json`, `SPEC.md`

### Lücke 7 — LTM-Backend-Migration
**Problem:** Kein Migrationspfad zwischen Backends (z.B. `json-file` → `chroma`) dokumentiert.  
**Fix:** In SPEC.md Migrations-Abschnitt ergänzen. Verweis auf `ltm-rebuild.py` Pattern (bereits in unserem LTM als Entscheidung dokumentiert — Eintrag #30).  
**Betroffene Datei:** `SPEC.md`

### Lücke 8 — `skills.capabilities`-Registry
**Problem:** Capabilities sind bedeutungslose Strings ohne Registry. Blockiert "Explicit over implicit"-Philosophie. Kein Agent-Framework kann darauf bauen.  
**Fix:** Initiale Registry anlegen: `registry/capabilities.md` mit den Standard-Capabilities und ihren semantischen Definitionen. Im Schema `_capability_registry`-Verweis aktivieren.  
**Betroffene Datei:** `registry/capabilities.md` (neu), `SPEC.md`, `AGENT_SCHEMA.json`

---

## 4. Umsetzungsreihenfolge

1. **Lücken 3 + 5 + 6** — Nur SPEC.md, minimaler Aufwand
2. **Lücke 1** — `patternProperties` in Schema
3. **Lücke 2** — Action-Enum/Registry in Schema + SPEC
4. **Lücke 4** — Checklist-Registry in Schema + SPEC
5. **Lücke 7** — LTM-Migration in SPEC
6. **Lücke 8** — `registry/capabilities.md` + Schema-Referenz (größter Aufwand, separat falls nötig)

---

## 5. File Protocol

| Action | File | Details |
|--------|------|---------|
| ✅ Created | `registry/capabilities.md` | Lücke 8: initiales Capability-Registry, 9 Kategorien, 30+ Capabilities |
| ✅ Modified | `SPEC.md` | L1: _doc-Convention-Abschnitt; L2: read_project_analysis + file_exists in Action-Table; L3: Template-Variable-Reference-Tabelle; L4: Standard-Closing-Checklist-Registry; L5: fallback_providers Abschnitt; L7: LTM-Backend-Migration; L8: capabilities-URL auf lokale Datei |
| ✅ Modified | `AGENT_SCHEMA.json` | L2: read_project_analysis in action-Enum, file_exists in condition-Enum, priority-Feld; L5: fallback_providers im runtime-Block |

---

## 6. Ergebnisse

Alle 8 Lücken vollständig geschlossen:

- **L1 _doc-Convention:** `_` Annotation Convention Abschnitt in SPEC.md. Standard-Keys: `_doc`, `_ref`, `_note`, `_todo`, `_migration`, `_restricted_write_doc`. patternProperties war bereits korrekt im Schema.
- **L2 Action-Enum:** `read_project_analysis` in enum, `file_exists` in condition-enum, neues `priority`-Feld (`mandatory_if_present`) im Schema. Onboarding-Tabelle in SPEC.md aktualisiert.
- **L3 Template-Variablen:** Formale Tabelle: `{date}` = YYYY-MM-DD, `{agent}` = identity.name kebab-case, `{topic}` = kebab-case. Mit Regeln und Custom-Placeholder-Hinweis.
- **L4 Closing Checklist:** Standard-Registry in SPEC.md: 7 normative Strings (file_protocol_complete, no_secrets_in_files, workpaper_status_updated, ltm_ingested, next_steps_documented, commit_pushed, open_tasks_in_backlog).
- **L5 fallback_providers:** Runtime-Tabelle in SPEC.md + Subsection. Array-Position = Priorität dokumentiert. Schema: items mit provider/model/endpoint.
- **L6 workpaper_template:** War bereits implementiert (template_file + template_file_quick in Schema + SPEC.md). Keine Änderung nötig.
- **L7 LTM-Migration:** Vollständige Migration-Prozedur in SPEC.md unter `long_term`. 5 Schritte, _migration-Annotation-Beispiel, Verweis auf ltm-rebuild.py.
- **L8 capabilities-Registry:** `registry/capabilities.md` erstellt (9 Kategorien, 30+ Standard-Capabilities). URL in SPEC.md auf lokale Datei aktualisiert.

---

## 7. Next Steps

- [ ] Issue #3 auf GitHub kommentieren + schließen
- [ ] LTM re-ingestieren
- [ ] Workpaper nach closed/ verschieben

---

**Status:** ✅ COMPLETED  
**Date:** 2026-02-22
