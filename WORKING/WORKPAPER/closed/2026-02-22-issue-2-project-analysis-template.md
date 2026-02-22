# 2026-02-22 — Copilot — Issue #2: Project Analysis Template

**Project:** Autonomous Agent Manifest Specification  
**Module:** templates/ / SPEC.md / workspace.onboarding / AGENT_SCHEMA.json  
**Status:** ✅ COMPLETED  
**Date:** 2026-02-22  
**GitHub Issue:** https://github.com/DEVmatrose/AAMS---Autonomous-Agent-Manifest-Specification/issues/2

---

## 1. Session Scope

### Kontext

Issue #2 wurde von ogerly geöffnet. Kernkritik: Es gibt keinen strukturierten Prozess, der *vor* dem Schreiben von `AGENT.json` und `READ-AGENT.md` die Realitäten eines bestehenden Projekts erhebt. Das Manifest wird entweder aus dem Bauch heraus geschrieben oder ist unvollständig.

7 konkrete Fehlstellen identifiziert: Git-Topologie, existierende Tools/Scripts, LTM-Zustand, Workpaper-Naming-Convention, Sicherheits-Enforcement, Projektphase & offene Schulden, Team & Governance.

### Ziel dieser Session

Alle 5 DoD-Punkte aus Issue #2 umsetzen:

1. `templates/project-analysis-template.md` erstellen
2. `SPEC.md` → neue Sektion "Before You Write a Manifest"
3. `workspace.onboarding.steps` → `read_project_analysis` als ersten Step (in `AGENT.json`)
4. `README.md` → Verweis auf das neue Template im Setup-Prozess
5. `AGENT_SCHEMA.json` → optionales Feld `project_analysis_path`

---

## 2. Struktur des Templates

Das Template hat 9 Sektionen (aus Issue #2 übernommen und konkretisiert):

```
1. Project Identity
   — Name, Typ, Stack, Status, Team-Größe, Lizenz

2. Repository Topology
   — Anzahl Repos, Remote ja/nein, Verschachtelung, Branch-Strategie

3. Filesystem Reality
   — Wo liegt WORKING/? Wo liegt Code? Wo liegen Configs?
   — Welche Pfade sind write-sensitiv?

4. Existing Tools & Scripts
   — Name, Pfad, Typ, Permissions, CI-integriert ja/nein

5. LTM State
   — Existiert bereits? Backend? Chunks? Dateien?
   — Onboarding: Erstaufbau oder Inkremental?

6. Session & Workpaper History
   — Naming-Pattern (bestehend)
   — Anzahl archivierter Workpapers
   — Offene Workpapers / aktive Tasks

7. Security Enforcement
   — Existierende Scanner / Hooks
   — Exit-Code-Standards
   — Erlaubte Secret-Speicherorte

8. Governance
   — Wer darf AGENT.json ändern?
   — Review-Intervall
   — Maintainer-Kontakt

9. Open Debt & Current Priorities
   — Was muss der Agent beim Start wissen?
   — Was ist aktiver Fokus, was ist Backlog?
```

---

## 3. Umsetzungsplan

### Schritt 1 — `templates/project-analysis-template.md` erstellen
Vollständiges Template mit allen 9 Sektionen, gut kommentiert, ausfüllbar.

### Schritt 2 — `SPEC.md`: Neue Sektion "Before You Write a Manifest"
Platzierung: vor der `AGENT.json`-Struktur-Dokumentation. Beschreibt `PROJECT-ANALYSIS.md` als optionalen aber empfohlenen Schritt.

### Schritt 3 — `AGENT.json`: `workspace.onboarding.steps`
Neuer erster Step vor `read_entry_point`:
```json
{
  "step": 0,
  "action": "read_project_analysis",
  "description": "Read PROJECT-ANALYSIS.md if present — contains pre-manifest project reality assessment.",
  "target": "./PROJECT-ANALYSIS.md",
  "condition": "file_exists",
  "priority": "mandatory_if_present"
}
```

### Schritt 4 — `README.md`: Verweis auf Template im Setup-Prozess
Im Abschnitt "Which File Do I Need?" oder "Get Started" einen Hinweis auf `templates/project-analysis-template.md`.

### Schritt 5 — `AGENT_SCHEMA.json`: `project_analysis_path`
Optionales Feld im `workspace`-Objekt:
```json
"project_analysis_path": {
  "type": "string",
  "description": "Path to the project analysis document (filled before writing AGENT.json).",
  "default": "./PROJECT-ANALYSIS.md"
}
```

---

## 4. Ergebnisse

Alle 5 DoD-Punkte vollständig implementiert.

- `templates/project-analysis-template.md`: 9 Sektionen, Tabellen-Format, `> Affects:` Hinweise pro Sektion, "How to use" Abschnitt am Ende
- `SPEC.md`: Neue H2-Sektion "Before You Write a Manifest" vor `## Structure Overview` — erklärt Zweck, zeigt alle 9 Sektionen in Tabelle, beschreibt Workflow und greenfield-Ausnahme
- `AGENT.json`: Step 0 `read_project_analysis` (condition: `file_exists`, priority: `mandatory_if_present`) vor `read_entry_point` eingeschoben
- `AGENT_SCHEMA.json`: `project_analysis_path` als optionales String-Feld mit Default `./PROJECT-ANALYSIS.md` im `workspace`-Objekt
- `README.md`: Satz für "Onboarding an existing project?" ergänzt mit Verweis auf Template

**Design-Entscheidung:** Step 0 ist `condition: file_exists` — kein harter Fehler wenn nicht vorhanden. Greenfield-Projekte brauchen es nicht. Für Brownfield ist es explizit als `mandatory_if_present` markiert, damit Agents es nicht überspringen.

---

## 5. File Protocol

| Action | File | Details |
|--------|------|---------|
| ✅ Created | `templates/project-analysis-template.md` | Neues Template, 9 Sektionen |
| ✅ Modified | `SPEC.md` | Neue H2 "Before You Write a Manifest" vor Structure Overview |
| ✅ Modified | `AGENT.json` | `workspace.onboarding.steps` → Step 0 read_project_analysis |
| ✅ Modified | `README.md` | Verweis auf Template für Existing-Project-Onboarding |
| ✅ Modified | `AGENT_SCHEMA.json` | `project_analysis_path` optional field in workspace |

---

## 6. Next Steps

- [x] Schritt 1–5 umsetzen
- [ ] Issue #2 auf GitHub kommentieren + schließen (manuell oder via token)
- [ ] LTM re-ingestieren
- [ ] Workpaper nach closed/ verschieben
- [ ] Issue #3 beginnen

---

**Status:** ✅ COMPLETED
