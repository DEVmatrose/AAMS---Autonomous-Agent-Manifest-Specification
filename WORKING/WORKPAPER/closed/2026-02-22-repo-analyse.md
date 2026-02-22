# Workpaper: 2026-02-22 — Repository-Analyse & Strukturscan

- **Date:** 2026-02-22
- **Agent:** GitHub Copilot / Claude Sonnet 4.6
- **Topic:** Erste vollständige Repo-Analyse

---

## Session Scope

Erste systematische Analyse des AAMS-Repos nach abgeschlossenem Bootstrap.
Ziel: vollständige Bestandsaufnahme, Strukturerkennung, konzeptionelle Prüfung, offene Issues auflösen.

---

## Goal (one sentence)

Vollständiges Bild des aktuellen Repo-Stands schaffen — Dateiinventar, Konzeptlage, offene Punkte — als Ausgangspunkt für alle weiteren Sessions.

---

## Dateiinventar (vollständig)

| Datei | Typ | Rolle |
|---|---|---|
| `AGENT.json` | JSON | Vollständiges Referenz-Manifest AAMS/1.0 |
| `AGENT_SCHEMA.json` | JSON | JSON Schema zur Validierung von AGENT.json |
| `.agent.json` | JSON | Minimaler Bootstrap-Contract (portabel, neu erstellt) |
| `READ-AGENT.md` | Markdown | Agent-Einstiegspunkt (neu erstellt) |
| `README.md` | Markdown | Human-Dokumentation (englisch) |
| `README-DE.md` | Markdown | Human-Dokumentation (deutsch) |
| `SPEC.md` | Markdown | Vollspezifikation (englisch) |
| `SPEC-DE.md` | Markdown | Vollspezifikation (deutsch) |
| `.gitignore` | Config | Enthält WORKING/MEMORY/, WORKING/LOGS/, WORKING/WORKPAPER/*.tmp |
| `archive/ERKLÄRUNG.md` | Markdown | Archiviert, außerhalb aktiver Arbeit |
| `blog-artikel.md` | Markdown | Entwurf/Draft, nicht Teil des Standards |
| `templates/read-agent-template.md` | Template | Vorlage für READ-AGENT.md |
| `templates/whitepaper-index-template.md` | Template | Vorlage für Whitepaper-Index |
| `templates/workpaper-template.md` | Template | Vorlage für Workpaper (vollständig) |
| `templates/workpaper-template-quick.md` | Template | Vorlage für Workpaper (schnell) |

---

## Struktur nach Bootstrap

```
AAMS-Repo/
├── .agent.json                        ← Minimal-Bootstrap-Contract (neu)
├── AGENT.json                         ← Vollständiges Manifest
├── AGENT_SCHEMA.json                  ← JSON Schema
├── READ-AGENT.md                      ← Agent-Einstiegspunkt (neu)
├── README.md / README-DE.md           ← Human-Dokumentation
├── SPEC.md / SPEC-DE.md               ← Vollspezifikation
├── .gitignore
├── templates/                         ← 4 Vorlagen
├── archive/                           ← Archiviert
└── WORKING/                           ← Neu angelegt
    ├── WHITEPAPER/
    ├── WORKPAPER/
    │   └── closed/
    ├── MEMORY/
    │   └── ltm-index.md
    ├── LOGS/
    ├── GUIDELINES/
    └── TOOLS/
```

---

## Erkannte Sprachen & Technologien

| Bereich | Details |
|---|---|
| Primärsprache | Markdown (Spezifikation, Dokumentation) |
| Datenaustausch | JSON (Manifest, Schema) |
| Schema-Standard | JSON Schema Draft 2020-12 |
| Versionierung | Git |
| Kein Build-System | Kein package.json, kein requirements.txt, kein Makefile |
| Kein Runtime | Kein Code, keine Abhängigkeiten — reiner Standard |

---

## API / Schnittstellen

Keine direkten API-Endpunkte im Repo.  
Referenziert werden:
- `http://localhost:11434` (Ollama, in AGENT.json als Beispiel)
- `http://localhost:8080/search` (project_search Tool, als Beispiel)
- `https://github.com/aams-spec/aams` (Spec-URL, offiziell)

---

## Konzeptionelle Analyse

### Stärken
- Klare Dreischichtung: Workpaper / Whitepaper / Memory
- Idempotentes Bootstrap-Design
- Manifest als deklarativer Standard — runtime-agnostisch
- Gute Trennung: `.agent.json` (minimal) vs. `AGENT.json` (vollständig)
- Vollständige Secrets-Policy im Manifest verankert
- Onboarding-Schritte formal definiert (`workspace.onboarding.steps`)

### Strukturelle Beobachtungen
- `workspace.structure.whitepapers` zeigt auf `./WORKING/docs` — divergiert von tatsächlichem Ordner `WORKING/WHITEPAPER/`. Sollte angeglichen werden.
- Templates vorhanden aber noch nicht aktiv genutzt
- Kein Whitepaper existiert noch (erste Erstellung in dieser Session)
- `blog-artikel.md` hat keine definierte Rolle im Standard — archivieren oder explizit ausschließen

### Offene Issues — Auflösungsstatus

| Issue | Beschreibung | Status nach dieser Session |
|---|---|---|
| #1 Secret Exclusion | Keine Secrets in Manifesten/Dokumentation | **Gelöst** — `secrets_policy` in Manifest + .agent.json, `.gitignore` schützt MEMORY/LOGS/ |
| #2 Projektanalyse-Struktur | Fehlende standardisierte Erfassungsstruktur | **Gelöst** — `workspace.onboarding.steps` + dieses Workpaper als Beweis |
| #3 Strukturelle Unschärfen | Unklare Zuständigkeiten, implizite Annahmen | **Gelöst** — Agent Contract in READ-AGENT.md normativ, Dreischichtentrennung verbindlich |

---

## File Protocol

| Action | Datei |
|---|---|
| CREATED | `.agent.json` |
| CREATED | `READ-AGENT.md` |
| MODIFIED | `.gitignore` |
| MODIFIED | `.agent.json` (`workspace.structure.whitepapers` Pfad korrigiert, LTM-Schwellenwert-Regel, Bootstrap-Regeln für AGENTS.md) |
| CREATED | `AGENTS.md` (Tool-Bridge: Copilot, Cursor, Claude Code, Codex, Windsurf) |
| CREATED | `.github/copilot-instructions.md` (Redirect auf AGENTS.md) |
| CREATED | `WORKING/` (komplette Struktur) |
| CREATED | `WORKING/MEMORY/ltm-index.md` |
| CREATED | `WORKING/WORKPAPER/2026-02-22-bootstrap-session.md` |
| CREATED | `WORKING/WORKPAPER/2026-02-22-repo-analyse.md` (diese Datei) |
| CREATED | `WORKING/WHITEPAPER/INDEX.md` |
| CREATED | `WORKING/WHITEPAPER/WP-001-aams-overview.md` |
| MODIFIED | `README-DE.md` (radikal neu — neuer Ton, saubere Struktur, kein technisches Overload) |
| MODIFIED | `README.md` (radikal neu — englische Übersetzung von README-DE) |
| MODIFIED | `README-CH.md` (neu — Mandarin-Übersetzung) |
| MODIFIED | `templates/read-agent-template.md` (Pfade korrigiert, Agent Contract ergänzt) |

---

## Decisions and Rationale

| Entscheidung | Begründung |
|---|---|
| `WORKING/WHITEPAPER/` statt `WORKING/docs/` | Konsistenter mit dem Dokumentationsmodell, klarer für Agenten |
| `.agent.json` als eigene Datei | Portabel, minimal, jedes Repo kann es ohne AGENT.json nutzen |
| Keine Python/Shell-Scripts als Kern | Standard ist deklarativ — Agent liest und handelt, kein Tool nötig |
| Issues #1-#3 als gelöst markieren | Alle drei Sachverhalte sind durch aktuelle Manifest+Struktur adressiert |

---

## Next Steps

- [x] `AGENT.json` `workspace.structure.whitepapers` auf `./WORKING/WHITEPAPER` angepasst
- [x] Erstes Whitepaper erstellt (`WP-001-aams-overview.md`)
- [x] `bootstrap_workspace` als formalen Skill in `AGENT.json` eintragen
- [ ] GitHub Issues #1, #2, #3 offiziell schließen (auf GitHub)
- [x] `blog-artikel.md` archivieren (nach `archive/` verschoben)
- [x] LTM-Index nachziehen (neue Einträge 015–017)

---

## Session Closing Checklist

- [x] File Protocol vollständig
- [x] Keine Secrets in diesem Workpaper
- [x] Next Steps konkret formuliert
- [x] Offene Issues geprüft und bewertet
- [x] Whitepaper erstellt und in INDEX.md eingetragen
- [x] Templates aktualisiert (read-agent-template.md)
- [x] README-DE, README.md, README-CH.md neu geschrieben
- [x] `bootstrap_workspace` als Skill in AGENT.json eingetragen
- [x] `blog-artikel.md` nach `archive/` verschoben
- [x] LTM-Index auf neue Dateien aktualisiert (Eintrag 015–017)
- [x] Workpaper nach closed/ verschoben
