# 2026-02-22 — Copilot — Review-Analyse + Forschungsebene

**Project:** Autonomous Agent Manifest Specification  
**Module:** docs/ · .agent.json · Positionierung · Forschungsebene  
**Status:** 🚧 IN PROGRESS  
**Date:** 2026-02-22

---

## 1. Session Scope

Externes Review auf Entwickler- und Forschungsebene erhalten. Zwei Aufgaben:
1. Review analysieren — was ist valide, was ist veraltet, was fehlt im Review?
2. Forschungsebene als aktiven Projektbereich verankern.

---

## 2. Review-Analyse — Was hat der Reviewer richtig verstanden?

**Kurzes Urteil: Reviewer hat das Projekt gut verstanden. Die Entwicklerebene ist präzise und ehrlich. Die Forschungsebene ist kompetent, aber etwas zu distanziert formuliert für ein Projekt das sich selbst als potentiellen Forschungsbeitrag versteht.**

### Entwicklerebene — Befund per Problem

| # | Reviewer-Befund | Status heute | Bewertung |
|---|---|---|---|
| P1 | curl-Befehl zeigt auf `aams-spec/aams` → 404 | ✅ **SOFORT BEHOBEN** (diese Session) | Kritisch und korrekt |
| P2 | `ltm_store_backend: "chroma"` in `.agent.json` — widerspricht Zero-dependency-Claim | ⚠️ Vorhanden, aber mit Note. Noch nicht bereinigt. | Valide Kritik |
| P3 | `AGENT_SCHEMA.json` nicht mit `AGENT.json` synchronisiert | ❌ **VERALTET** — 0 Validation-Errors bewiesen (diese Session, `_selfcheck.py`) | Reviewer hatte ältere Version |
| P4 | `templates/project-analysis-template.md` existiert nicht | ❌ **VERALTET** — in Issue #2 erstellt (`2c4126a`) | Reviewer hatte ältere Version |
| P5 | Repo-Name SEO/UX-Problem — drei Bindestriche | ⚠️ Offen, aber niedrige Priorität | Valide, mittel-langfristig |

**Wichtig für die Dokument-Pflege:** Der Reviewer hat offensichtlich nicht den aktuellen Git-Stand gesehen (fehlte Issue #2 + Issue #3 Commits). Das bedeutet: wenn AAMS als Standard kommuniziert wird, braucht es ein "What's New" / Changelog der deutlich macht was aktuell ist. Der SPEC-Header hat noch `Status: Draft` — das ist korrekt, aber ein Reviewer der einen Draft bekommt ohne Commit-History hat keinen Bezug zum aktuellen Stand.

### Was der Reviewer **nicht** gesieht hat

- `_selfcheck.py` als Werkzeug — das zeigt, dass wir bereits automated compliance tracking haben
- Die Closing Checklist Registry (L4 fix) — das adressiert genau den "not automatable" Einwand
- `restricted_write` — der Reviewer erwähnt `.gitignore` als Sicherheitsrisiko implizit, das ist bereits adressiert

---

## 3. Offene Entwickler-Aufgaben aus dem Review

### P1 — curl fix (ERLEDIGT)
`docs/index.html` URL geändert auf aktuelles Repo. Commit pending.

### P2 — `.agent.json` ltm_store_backend bereinigen
Das Feld ist in `bootstrap_rules` mit einer Opt-in-Note. Problem: ein Leser der die Datei schnell scannt, sieht `"ltm_store_backend": "chroma"` und denkt: Pflicht.

**Empfohlene Änderung:** Das Feld umbenennen in `ltm_store_backend_recommended` und die Note klarer machen. Oder: in einen optionalen `advanced` Block verschieben.

Status: **TODO — nächste Session oder nach diesem Commit**

### P5 — Repo-Name
Langfristig: org `aams-spec` + Repo `aams` anlegen. Kein kurzfristiger Fix nötig solange alle Links korrekt sind (P1 war der einzige broken link).

---

## 4. Forschungsebene — Verortung und Ambition

### 4.1 Was der Reviewer richtig identifiziert hat

Der Reviewer nennt drei legitime Forschungsfragen die AAMS berührt:

1. **Episodic Memory für LLM-Agenten** (MemGPT-Linie, Cognitive Architectures)
2. **Agent Coordination Protocols** (Multi-Agent, FIPA-Verwandtschaft, Filesystem-Konvention vs. Messaging)
3. **Reproducibility:** Workpaper ≈ Lab-Notebook für Software-Agenten

Alle drei sind korrekt erkannt. Der Reviewer hält AAMS jedoch für "nicht Forschungsbeitrag — Engineering-Konvention mit realem Problem." Das ist die momentane Wahrnehmung. Die Frage ist ob wir das ändern wollen — und falls ja, wie.

### 4.2 Eigene Einschätzung (ogerly)

Die Intention ist: AAMS könnte Teil der Forschung auf diesem Gebiet werden — nicht als primäres Ziel, aber als Möglichkeit, wenn die Bedingungen erfüllt sind. Das ist ehrlich und realistisch. Es bedeutet:

- **Primär:** Engineering-Standard, Adoption in der Entwickler-Community
- **Sekundär / offen:** Akademische Anschlussfähigkeit, wenn das Projekt die nötigen Qualitätsstufen erreicht

Das ist ein legitimer Weg. Viele Forschungsartefakte (Git, Docker, Kubernetes) begannen als Engineering-Lösungen und wurden erst nachträglich akademisch relevant.

### 4.3 Was fehlt für akademische Anschlussfähigkeit

Der Reviewer trifft mit dieser Liste den Kern:

| Lücke | Aufwand | Priorität |
|---|---|---|
| Kein Related Work / Positionierung gegen existierende Ansätze | Mittel | Wenn Forschungsambitionen ernst | 
| LTM-Qualität nicht messbar (keine Metriken) | Groß | Forschungsebene |
| Dreischichten-Modell nicht empirisch begründet | Mittel | Forschungsebene |
| Kein Falsifizierbarkeits-Claim ("no more starting from zero" ist nicht messbar) | Klein | Wenn Peer-Review angestrebt |

### 4.4 Stärkste akademisch anschlussfähige Formulierung (aus dem Review übernommen)

> *"We are not solving the LTM problem — we are creating the scaffolding that makes LTM solutions pluggable."*

Diese Formulierung ist besser als der aktuelle SPEC-Claim. Sie ist:
- ehrlicher (kein Over-Engineering-Claim)
- anschlussreich für Framework-Designer und Forscher
- klar abgegrenzt gegenüber MemGPT, LangChain Memory etc.

**Aktion:** Diese Formulierung (oder eine Variante) in SPEC.md und README.md verankern — als explizite Positionierung.

### 4.5 Forschungsebene als Projektbereich — Entscheidung

Ab sofort: Die Forschungsebene ist ein aktiver Projektbereich, aber sekundär. Konkret:

- SPEC.md erhält einen `Related Work`-Abschnitt (mittel-langfristig)
- SPEC.md erhält eine explizite Positions-Formulierung (kurzfristig, nächste Session)
- Vergleichstabelle: AAMS vs. MemGPT vs. LangChain Memory vs. DVC — als eigenständiges Whitepaper `WP-002-related-work.md`
- Metriken für LTM-Qualität: offene Forschungsfrage, wird als Issue formuliert

---

## 5. Offene Punkte / Nächste Schritte

- [ ] `.agent.json` P2-Fix: `ltm_store_backend` als optional/advanced markieren
- [ ] `SPEC.md` Positionierungs-Formulierung ergänzen ("scaffolding that makes LTM solutions pluggable")
- [ ] `WP-002-related-work.md` erstellen: Vergleich AAMS vs. verwandte Ansätze
- [ ] GitHub Issue für Related Work / Research Positioning anlegen
- [ ] Commit diese Session: curl-Fix + Schema-Fixes + _selfcheck.py + prompts/system.md + AGENT.json typo
- [ ] LTM re-ingest

---

## 6. File Protocol

| Action | File | Details |
|--------|------|---------|
| ✅ Fixed | `docs/index.html` | curl-URL von `aams-spec/aams` auf aktuelles Repo |
| ✅ Created | `WORKING/TOOLS/_selfcheck.py` | Automatisierter Self-Check (34 Checks) |
| ✅ Modified | `AGENT_SCHEMA.json` | restricted_write in filesystem, ltm_triggers neue Actions + Felder |
| ✅ Modified | `SPEC.md` | restricted_write doku, ltm_triggers Tabelle erweitert |
| ✅ Modified | `AGENT.json` | workpapers_closed Typo: ./WORKING/WORKPAPER/close → closed |
| ✅ Created | `prompts/system.md` | Referenz-Vorlage für runtime.system_prompt_file |
| ✅ Created | `WORKING/DATABASE/` | Fehlendes Verzeichnis aus workspace.structure |

---

**Status:** 🚧 IN PROGRESS
