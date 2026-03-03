# WORKPAPER — Session Check & Issues Review

**Session:** 2026-03-03
**Status:** OPEN
**Agent:** GitHub Copilot / Claude Sonnet 4.6
**Typ:** Session Start / Repository Sync / Issue Review

---

## Session Scope

Selbstcheck des AAMS-Repos. Git Pull + aktuelle Open Issues vom GitHub-Profil (DEVmatrose/AAMS) reviewen.

---

## Git Status

- Remote: `https://github.com/DEVmatrose/AAMS.git`
- HEAD: `559fe85` — `fix(#12): AAMS-MINI vs full — explicit ltm_mode + two-track LTM in READ-AGENT.md`
- Status: **Already up to date** — kein Pull nötig

### Letzte Commits (Zusammenfassung)

| Hash | Message |
|------|---------|
| `559fe85` | fix(#12): AAMS-MINI vs full — explicit ltm_mode + two-track LTM in READ-AGENT.md |
| `dd6b10a` | fix+ux: issues #10 #11 #13 from field report ImprintGuard |
| `15c4313` | fix+feat: repo issue review 2026-02-28 |
| `4043b31` | session close: 2026-02-26-entry-point-klarheit workpaper archived |
| `42df943` | Signal-Redesign: imperative agent entry points + Diary Layer mandatory |

---

## Offene GitHub Issues (Stand: 2026-03-03)

### #18 — Report: GEMINI.md / airules.md (NEU — 2026-03-03)
**Author:** ogerly | **Datum:** 2026-03-03 (heute, 14:45)

**Inhalt:** Deep-Dive in Firebase Studio's `GEMINI.md` (alternativ: `.idx/airules.md`) — das Herzstück für "Vibe Coding" mit Gemini.

**Was macht GEMINI.md laut Report:**
- Fungiert als **System-Prompt auf Projektebene** (Persona, Tech Stack, Coding Standards, Workflow-Modi)
- Wird bei *jedem* Prompt mitgeschickt → Token-Kosten bei langen Dateien
- Firebase Studio priorisiert `.idx/airules.md` vor `GEMINI.md`
- Supports JIT-Kontext via Unterordner-GEMINI.md

**Limits:** Zu lang → Token-Bloat, Halluzinationen — gleiche Problematik wie CLAUDE.md (#14)

**Bedeutung für AAMS:** Direkt verknüpft mit #14 (CLAUDE.md-Trend) und #15/#16 (Gemini-Workflow). Zeigt, dass jedes Agent-Ökosystem seine eigene Config-Datei hat (`CLAUDE.md`, `GEMINI.md`, `airules.md`, `AGENTS.md`). AAMS muss sich davon explizit abgrenzen.

---

### #17 — Field Report: AAMS in a Real Production Project
**Author:** ogerly | **Label:** field-report | **Datum:** 2026-03-02

**Projekt:** Luna-1 (Vue 3 + Node.js + Supabase + LM Studio) — Nov 2025 bis März 2026 (~4 Monate)

**Key Findings aus dem Report:**
- 3-Layer Model (Workpaper → Whitepaper → LTM) funktioniert in der Praxis ✅
- Vector LTM (ChromaDB, 2120 Chunks) ist der Component mit dem höchsten Wert
- Workpaper-Disziplin verhindert "Where Were We"-Syndrom
- **Kritik (Friction Points):**
  1. Chat Agents bootstrappen sich nicht selbst — User muss explizit prompten
  2. Naming Drift: `close/` vs `closed/` — 50+ Dateien, Deviation dokumentiert in `.agent.json`
  3. `ltm-index.md` Track fehlte bis heute — nachträglich mit ~8 Einträgen bootstrapped
  4. `AGENTS.md` Bridge fehlte (war erst heute erstellt worden)
  5. Folder Naming vs Spec — 40+ interne Cross-References verhindern Umbenennung

**Empfehlungen zurück an AAMS Spec:**
1. `ltm-index.md` als Hero Artifact etablieren (survives fresh clone, GitHub-lesbar)
2. `_deviations` als offizielles Schema-Feld hinzufügen
3. `AGENTS.md` vor `.agent.json` im Onboarding
4. Session-Start Prompts / VS Code Snippets für Copilot Chat
5. `workpapers_closed_aliases` Feld erwägen

**Quantitative Daten:**
- 30+ Sessions | 25+ archivierte Workpapers | 40+ Whitepapers
- 2120 LTM Chunks | 187 indexed Dokumente | 0 Secret Leaks
- ~70% Compliance bei Workpaper-vor-Arbeit & LTM-Query

---

### #16 — Report & Guideline: Gemini/Firebase Studio Workflow Integration into AAMS
**Author:** ogerly | **Label:** field-report | **Datum:** 2026-03-02

**Inhalt:** Zwei-Phasen-Workflow für Agenten-native Planungs-Artefakte (z.B. Gemini's `blueprint.md`):
- Phase 1: `blueprint.md` als ephemeres Live-Planungsdokument (im Root, nur während der Task)
- Phase 2: AAMS Formalisierung → Inhalte in Workpaper/Whitepaper → `blueprint.md` löschen

Dieser konkrete Workflow-Guide wurde als Annotation für `READ-AGENT.md` vorgeschlagen (Abschnitt "Agent-Specific Workflows").

---

### #15 — Proposal: Integrate Agent-Specific Planning Artifacts into AAMS Workflow
**Author:** ogerly (submitted by Gemini) | **Labels:** documentation, enhancement | **Datum:** 2026-03-02

**Inhalt:** Formaler Proposal (von Gemini eingereicht) für denselben Zwei-Phasen-Ansatz wie #16.
- Blueprint.md = temporäres ephemeres Planungsartefakt
- AAMS = dauerhaftes Archiv

**Verhältnis zu #16:** #15 ist der Proposal, #16 ist das konkrete Guideline. Inhaltlich zusammengehörig — evtl. zusammenführen oder #15 als geschlossen markieren wenn #16 implementiert wird.

---

### #14 — CLAUDE.md in Claude-Code-Projekten: Hintergrund & aktueller Trend (März 2026)
**Author:** ogerly | **Datum:** 2026-03-01

**Community-Trend:** Lange CLAUDE.md-Dateien (>150 Zeilen) schaden der Antwortqualität.
Empfehlung: Kürzen auf 20–60 Zeilen oder `/init` für Neubau.

**AAMS-Status:** Kein CLAUDE.md vorhanden. Stattdessen: `AGENTS.md` + `.agent.json` + `READ-AGENT.md`.

**Diskussionsfrage:**
1. Explizit dokumentieren dass AAMS kein CLAUDE.md braucht/empfiehlt?
2. Best-Practice-Abschnitt für Claude Code: nutze `AGENTS.md` statt `CLAUDE.md`
3. Optional: Template-Link für den seltenen Fall

---

### #8 — Feature: Security Signals in AGENT.json
**Author:** AgentGurke | **Datum:** 2026-02-27 (Updated: 2026-02-28)

**Vorschlag:** `security`-Sektion in AGENT.json:
- `last_scan`, `scan_type`, `findings` (critical/high/medium/low)
- `deployed_services` Array
- `behavioral_signals` (sessions_without_incident, trust_score)

---

### #7 — Feature: Security Audit Fields in AGENT.json (from AutoPilotAI feedback)
**Author:** AgentGurke | **Datum:** 2026-02-27 (Updated: 2026-02-28)

**Vorschlag:** `security_audit`-Sektion in AGENT.json:
- `last_scan`, `scanner`, `findings`, `trust_score`, `attestations`
- Behavioral log als Dateipfad

**Verhältnis zu #8:** Beide kommen aus der Moltbook-Diskussion / AutoPilotAI-Feedback. Inhaltlich nahezu identisch — #7 und #8 sollten zusammengeführt werden.

---

## Issue-Kategorisierung

| # | Typ | Priorität | Aktion |
|---|-----|-----------|--------|
| #17 | Field Report — Produktionspraxis | HIGH | Empfehlungen reviewen → Issues anlegen / Spec updaten |
| #18 | Report — GEMINI.md / airules.md | HIGH | Mit #14 zusammenführen → AAMS-Positionierung schärfen |
| #16 | Guideline — Blueprint.md Workflow | MEDIUM | Als Abschnitt in READ-AGENT.md integrieren |
| #15 | Proposal — Agent-native Artifacts | MEDIUM | Mit #16 zusammenführen oder #15 schließen nach #16-Impl. |
| #14 | Diskussion — CLAUDE.md Trend | MEDIUM | Klärung in README/SPEC: AAMS als agent-agnostischer Standard |
| #8 | Feature — Security Signals | LOW | Duplicate mit #7 — zusammenführen, dann AGENT.json + Schema erweitern |
| #7 | Feature — Security Audit | LOW | Duplicate mit #8 — Basis für Feature-Implementierung |

---

## Selbstcheck: README + Index + Repo-Struktur

### Befunde

| Datei | Status | Aktion |
|-------|--------|--------|
| `README.md` | ✅ Aktuell | Agent-Block oben, human content darunter. Inhalt korrekt. |
| `AGENTS.md` | ✅ Aktuell | Imperative, korrekt, agent-agnostisch. |
| `READ-AGENT.md` | ✅ Aktuell | Dual-track LTM, Diary Layer, AAMS-MINI vs. full. |
| `WORKING/WHITEPAPER/INDEX.md` | ~~VERALTET~~ → ✅ Fixed | Stand 2026-02-22, Diary Layer fehlte → aktualisiert |
| `WORKING/WHITEPAPER/WP-001` | ~~VERALTET~~ → ✅ Fixed | "3-Schichten" korrigiert zu "4-Schichten", Status aktualisiert |

### Root-Struktur: zu viel

Aktuell landen auf Root-Level:
```
.agent.json          ← THE ONE FILE — keep
AGENTS.md            ← auto-read bridge — keep (muss in Root bleiben)
READ-AGENT.md        ← agent contract — keep (muss in Root bleiben)
README.md            ← humans — keep
README-DE.md         ← German README — kandidat für reference/
AGENT.json           ← reference manifest — kandidat für reference/
AGENT_SCHEMA.json    ← JSON Schema — kandidat für reference/
SPEC.md              ← full spec — kandidat für reference/
SPEC-DE.md           ← German spec — kandidat für reference/
archive/             ← 2 alte Dateien — entfernen
docs/                ← GitHub Pages — keep (extern verlinkt)
prompts/             ← 2 Dateien — kandidat für reference/
registry/            ← 1 Datei — kandidat für reference/
templates/           ← 5 Dateien — kandidat für reference/
WORKING/             ← Workspace — keep
```

### Vorschlag: Konsolidierung in `reference/`

**Root nach Umbau:**
```
.agent.json          ← THE ONE FILE
AGENTS.md            ← auto-read bridge
READ-AGENT.md        ← agent contract
README.md            ← humans
docs/                ← GitHub Pages
reference/           ← alles Spec-Material
WORKING/             ← Workspace
```

**`reference/` Inhalt:**
```
reference/
├── AGENT.json             ← full annotated manifest
├── AGENT_SCHEMA.json      ← JSON Schema
├── SPEC.md                ← full spec (EN)
├── SPEC-DE.md             ← full spec (DE)
├── README-DE.md           ← German README
├── prompts/               ← bootstrap.md, system.md
├── registry/              ← capabilities.md
└── templates/             ← alle 5 Templates
```

**archive/** → entfernen (nur 2 alte Dateien, kein Mehrwert)

### Impact-Check: Was würde sich ändern?
- `README.md` Links auf `SPEC.md`, `AGENT.json`, `AGENT_SCHEMA.json` müssen aktualisiert werden
- `.agent.json` und `AGENTS.md` haben keine Abhängigkeiten zu den moved files ✅
- `READ-AGENT.md` hat keine Abhängigkeiten zu den moved files ✅
- GitHub Pages (`docs/`) bleibt unverändert ✅
- `curl` Bootstrap-Befehl (`.agent.json`) bleibt identisch ✅

---

1. #15 und #16 zusammenführen oder separat abarbeiten?
2. #7 und #8 zusammenführen — welcher als Basis?
3. Für #14: Soll CLAUDE.md aktiv im README erwähnt werden, oder nur als FAQ?
4. Für #17 Empfehlung 2 (`_deviations`): AGENT_SCHEMA.json erweitern — Scope dieser Session?

---

## File Protocol

| Action | File | Detail |
|--------|------|--------|
| CREATED | `WORKING/WORKPAPER/2026-03-03-session-check-issues-review.md` | Diese Session |
| CREATED | `WORKING/DIARY/2026-03.md` | März-Diary angelegt |
| CREATED | `reference/` | Neues Verzeichnis für alle Spec-Referenzmaterialien |
| MOVED | `AGENT.json` → `reference/AGENT.json` | Repo-Bereinigung |
| MOVED | `AGENT_SCHEMA.json` → `reference/AGENT_SCHEMA.json` | Repo-Bereinigung |
| MOVED | `SPEC.md` → `reference/SPEC.md` | Repo-Bereinigung |
| MOVED | `SPEC-DE.md` → `reference/SPEC-DE.md` | Repo-Bereinigung |
| MOVED | `README-DE.md` → `reference/README-DE.md` | Repo-Bereinigung |
| MOVED | `prompts/` → `reference/prompts/` | Repo-Bereinigung |
| MOVED | `registry/` → `reference/registry/` | Repo-Bereinigung |
| MOVED | `templates/` → `reference/templates/` | Repo-Bereinigung |
| EDITED | `README.md` | Links auf reference/ aktualisiert, Three-Layer → Four-Layer, DIARY/ in Struktur |
| EDITED | `AGENTS.md` | Links auf reference/SPEC.md, reference/AGENT.json, reference/AGENT_SCHEMA.json |
| EDITED | `READ-AGENT.md` | Key Files Tabelle Pfade auf reference/ aktualisiert |
| EDITED | `WORKING/WHITEPAPER/INDEX.md` | Aktualisiert auf 2026-03-03, Diary Layer, AAMS-MINI |
| EDITED | `WORKING/WHITEPAPER/WP-001-aams-overview.md` | 4-Schichten-Modell, Diary Layer, Status Stand März 2026 |

---

## Tasks dieser Session

### T1 — #17 Empfehlung 2: `_deviations` als offizielles Schema-Feld
- [ ] `AGENT_SCHEMA.json` um `_deviations`-Feld erweitern
- [ ] `AGENT.json` mit Beispiel-Deviation dokumentieren
- [ ] `SPEC.md` Abschnitt ergänzen

### T2 — #17 Empfehlung 1: `ltm-index.md` prominenter machen
- [ ] `README.md` — `ltm-index.md` als primäres LTM-Artefakt herausstellen
- [ ] Setup-Reihenfolge in Docs prüfen: ltm-index.md vor ChromaDB erwähnen

### T3 — #14 + #18: AAMS vs CLAUDE.md / GEMINI.md / airules.md — Positionierung
- [ ] Kurzen Abschnitt für `README.md` oder `SPEC.md` schreiben
- [ ] Klarstellen: AAMS ist agent-agnostisch, die tool-spezifischen Dateien sind nicht nötig
- [ ] Mapping dokumentieren: `CLAUDE.md` / `GEMINI.md` / `airules.md` → werden durch `AGENTS.md` + `.agent.json` ersetzt

### T4 — #15/#16: Agent-Specific Workflows in READ-AGENT.md
- [ ] Neuer Abschnitt "Agent-Specific Workflow Integration" in `READ-AGENT.md`
- [ ] blueprint.md Zwei-Phasen-Workflow dokumentieren
- [ ] #15 nach Integration schließen

### T5 — #7/#8: Security Signals zusammenführen + AGENT.json erweitern
- [ ] Entscheidung: welches Issue als Basis
- [ ] `security_audit`-Feld in `AGENT.json` hinzufügen
- [ ] `AGENT_SCHEMA.json` um security_audit erweitern

---

## Next Steps

- Diary-Eintrag für 2026-03 angelegt ✅
- T1 beginnen (höchste Spec-Relevanz aus #17)

