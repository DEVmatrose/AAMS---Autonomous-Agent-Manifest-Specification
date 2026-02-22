# 2026-02-22 — Copilot — Issue #1: Absolute Secret Exclusion Policy

**Project:** Autonomous Agent Manifest Specification  
**Module:** Security / AGENT.json / AGENT_SCHEMA.json / SPEC.md  
**Status:** ✅ COMPLETED  
**Date:** 2026-02-22  
**GitHub Issue:** https://github.com/DEVmatrose/AAMS---Autonomous-Agent-Manifest-Specification/issues/1

---

## 1. Session Scope

### Kontext

Issue #1 wurde von ogerly geöffnet. Kernkritik: Die `secrets_policy` in AAMS ist deklarativ dokumentiert, aber nicht auf Infrastrukturebene erzwungen. LLMs haben keine persistente Regelbindung — ein langes Kontextfenster kann dazu führen, dass Checklist-Items übersprungen werden.

### Ziel dieser Session

Alle 7 DoD-Punkte aus Issue #1 umsetzen:

1. `AGENT_SCHEMA.json` → `output_validation` mit `forbidden_patterns`
2. `AGENT.json` → `gitignore_patterns` erweitern (`.env`, `*.pem`, `*.key`, etc.)
3. `AGENT.json` → `permissions.filesystem.write` → `.gitignore` einschränken
4. `AGENT.json` → `ltm_triggers` → `workpaper_pre_save` Pflicht-Scan
5. `SPEC.md` → neue Sektion "Absolute Secret Exclusion Policy"
6. Workpaper-Templates → Pre-Save-Scan als expliziter Hinweis
7. `.gitignore` im Repo selbst prüfen und ggf. ergänzen

---

## 2. Bestandsaufnahme (aktueller Stand)

### `AGENT.json` — `gitignore_patterns`
```json
"gitignore_patterns": [
  "WORKING/LOGS/",
  "WORKING/WORKPAPER/*.tmp"
]
```
**Fehlt:** `.env`, `.env.*`, `.env.local`, `.point-mf`, `*.pem`, `*.key`, `secrets.*`

### `AGENT.json` — `permissions.filesystem.write`
Enthält `./.gitignore` ohne Einschränkung → theoretisch kann ein Agent Schutzregeln überschreiben.

### `AGENT_SCHEMA.json`
Kein `output_validation`-Block. Kein Pattern-Matching auf Secret-Strings.

### `SPEC.md`
Keine Sektion zum Thema Secret Exclusion Policy.

### Workpaper-Templates
`closing_checklist` enthält `"No secrets/passwords/tokens in plain text in workpaper?"` als manuelles Checkbox-Item — kein automatischer Scan-Step.

### `.gitignore`
Nicht geprüft. Muss verifiziert werden.

---

## 3. Umsetzungsplan

### Schritt 1 — `AGENT.json`: `gitignore_patterns` erweitern
```json
"gitignore_patterns": [
  "WORKING/LOGS/",
  "WORKING/WORKPAPER/*.tmp",
  "WORKING/AGENT-MEMORY/",
  ".env",
  ".env.*",
  ".env.local",
  ".point-mf",
  "*.pem",
  "*.key",
  "secrets.*"
]
```

### Schritt 2 — `AGENT.json`: `permissions.filesystem.write` härten
`.gitignore` aus freiem Write herausnehmen → in `restricted_write` verschieben:
```json
"write": ["./WORKING", "./READ-AGENT.md"],
"restricted_write": ["./.gitignore"]
```

### Schritt 3 — `AGENT.json`: `ltm_triggers` → `workpaper_pre_save`
Neuer Trigger vor dem Schreiben jedes Workpapers:
```json
{
  "event": "workpaper_pre_save",
  "action": "scan_secrets",
  "priority": "mandatory",
  "on_match": "block_and_alert",
  "description": "Before saving any workpaper: scan for secret patterns. Block if match found."
}
```

### Schritt 4 — `AGENT_SCHEMA.json`: `output_validation`
```json
"output_validation": {
  "scan_before_write": true,
  "forbidden_patterns": [
    "AKIA[0-9A-Z]{16}",
    "eyJ[a-zA-Z0-9_-]+\\.[a-zA-Z0-9_-]+\\.[a-zA-Z0-9_-]+",
    "-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "[a-zA-Z0-9_\\-]{20,}:[a-zA-Z0-9_\\-]{20,}@",
    "password\\s*[:=]\\s*['\"][^'\"]{6,}['\"]",
    "api[_-]?key\\s*[:=]\\s*['\"][^'\"]{8,}['\"]"
  ],
  "on_match": "block_and_log"
}
```

### Schritt 5 — `SPEC.md`: Neue Sektion
Neue Sektion "Absolute Secret Exclusion Policy" mit vollständiger Policy-Dokumentation (aus Issue #1 übernommen, ggf. angepasst).

### Schritt 6 — Workpaper-Templates
In `closing_checklist` und `workpaper_rules` expliziten Pre-Save-Scan-Hinweis ergänzen — kein manuelles Checkbox-Item, sondern als Pflicht-Step beschrieben.

### Schritt 7 — `.gitignore` prüfen
Aktuellen `.gitignore` lesen → `.env`, `.env.*`, `.point-mf`, `*.pem`, `*.key` prüfen.

---

## 4. Ergebnisse

Alle 7 DoD-Punkte umgesetzt:

| Punkt | Aktion | Status |
|---|---|---|
| 1 | `AGENT.json` `gitignore_patterns` + 8 neue Muster (`.env`, `*.pem`, `*.key`, etc.) | ✅ |
| 2 | `permissions.filesystem.write`: `.gitignore` nach `restricted_write` verschoben | ✅ |
| 3 | `AGENT.json` `ltm_triggers`: `workpaper_pre_save` + `scan_secrets` + `on_match: block_and_alert` | ✅ |
| 4 | `AGENT_SCHEMA.json`: `output_validation` Block mit `forbidden_patterns`, `scan_before_write`, `on_match` Enum. `scan_secrets` zum Action-Enum hinzugefügt | ✅ |
| 5 | `SPEC.md`: `output_validation` Untersektion + H2-Sektion "Absolute Secret Exclusion Policy" (3-Layer-Enforcement-Modell, Risk Matrix, Pre-Commit Hook Referenzimplementierung) | ✅ |
| 6 | Beide Templates: Checklist-Item als **⚠️** markiert + Verweis auf `output_validation` + Policy | ✅ |
| 7 | `.gitignore`: Secret-Block ergänzt (`.env`, `.env.*`, `.env.local`, `.point-mf`, `*.pem`, `*.key`, `secrets.*`) | ✅ |

**Kritische Designentscheidung:** AAMS kann keine Runtime-Enforcement erzwingen (framework-unabhängig). Die Spec benennt das ehrlich. Lösung: 3-Layer-Modell (Agent + Pre-Commit Hook + CI). Der Pre-Commit Hook liest `forbidden_patterns` direkt aus `AGENT.json` — Single Source of Truth, kein separates Hook-Config-File.

---

## 5. File Protocol

| Action | File | Details |
|--------|------|---------|
| ✏️ Modified | `AGENT.json` | gitignore_patterns, permissions, ltm_triggers |
| ✏️ Modified | `AGENT_SCHEMA.json` | output_validation block |
| ✏️ Modified | `SPEC.md` | Neue Sektion "Absolute Secret Exclusion Policy" |
| ✏️ Modified | `templates/workpaper-template.md` | Pre-Save-Scan Hinweis |
| ✏️ Modified | `templates/workpaper-template-quick.md` | Pre-Save-Scan Hinweis |
| ✏️ Modified | `.gitignore` | ggf. ergänzt |

---

## 6. Next Steps

- [ ] Schritt 1–7 umsetzen (siehe oben)
- [ ] Issue #1 auf GitHub kommentieren + schließen
- [ ] LTM ingestieren
- [x] Schritt 1–7 umgesetzt ✅
- [ ] Issue #1 auf GitHub schließen
- [x] LTM ingestieren ✅
- [ ] Workpaper nach closed/ verschieben

---

**Status:** ✅ COMPLETED — Alle 7 DoD-Punkte umgesetzt. Issue #1 kann geschlossen werden.
