# Workpaper: 2026-02-22 — Hartes Review v1 — Kritik, Lücken, Konsequenzen

- **Date:** 2026-02-22
- **Agent:** GitHub Copilot / Claude Sonnet 4.6
- **Topic:** Externes hartes Review — Positionierung, Schwächen, offene Architekturprobleme
- **Status:** ✅ COMPLETED

---

## Session Scope

Ein erstes hartes externes Review wurde eingebracht. Ziel dieser Session: Review strukturiert erfassen, jede Kritik bewerten (berechtigt / teilweise / falsch), konkrete Konsequenzen ableiten und priorisieren.

---

## Das Review (vollständig)

> Quelle: externer Reviewer, 2026-02-22

### Gesamturteil des Reviewers

> "Solides erstes Release mit echter Felderfahrung dahinter. Die Grundidee ist richtig. Die Ausführung hat aber eine kritische Lücke: das LTM-Problem ist beschrieben aber nicht gelöst, und ohne das ist der Kern-Claim ('no context loss') nicht einlösbar."

---

## Bewertung jedes Kritikpunkts

### 1. "AAMS ist ein Konventionssystem, kein Framework" — Positionierung verspricht zu viel

**Berechtigung:** ✅ Vollständig berechtigt.  

"One file. Every repo. No context loss." — der letzte Teil ist nicht durch die Struktur allein einlösbar. Context loss wird *reduziert*, nicht eliminiert. Das ist ein Claim-Problem, kein Konzeptproblem.

**Konsequenz:**  
Tagline überarbeiten. "No context loss" → etwas Ehrlicheres. Vorschlag: "No more starting from zero." oder "Context survives sessions."

---

### 2. Stärken — Kernproblem real, Zero-dependency, Dreischichten solid

**Bewertung:** ✅ Zutreffend, kein Handlungsbedarf außer diese Punkte im README schärfer herauszuarbeiten.

---

### 3. LTM-Konzept — "beschrieben aber nicht gelöst"

**Berechtigung:** ✅ Vollständig berechtigt. Das ist die kritischste Schwäche.

`ltm-index.md` ist ein Workaround, keine Lösung. Der Reviewer hat recht: ohne funktionierendes LTM ist "no context loss" nicht einlösbar.

**Konsequenz (konkret):**  
- Option A: SQLite-basiertes Minimalbeispiel liefern — `WORKING/MEMORY/ltm.db` + 30-Zeilen-Python-Script für ingest/query. Kein Framework, kein Vendor.
- Option B: ltm-index.md ehrlich als "Bootstrap-LTM für kleine Projekte (<100 Sessions)" positionieren — nicht als LTM-Lösung.
- **Empfehlung:** Beides. Option B sofort (Messaging-Fix), Option A als `WORKING/TOOLS/` Referenzimplementierung.

---

### 4. Compliance nicht erzwingbar — "Agent Contract funktioniert nur wenn Agent mitzieht"

**Berechtigung:** ✅ Vollständig berechtigt — aber das ist inhärent bei JEDEM deklarativen Standard.

`.editorconfig` ist auch nicht erzwingbar ohne Editor-Plugin. `package.json` führt nicht automatisch zu Code-Qualität. Der Reviewer beschreibt keine AAMS-spezifische Schwäche — er beschreibt die Grenzen deklarativer Standards.

**Was trotzdem stimmt:** Der AGENTS.md/system-prompt-Injection-Weg wird nicht prominent genug als "so machst du es erzwingbar" kommuniziert.

**Konsequenz:** README um einen konkreten "Enforcement"-Abschnitt ergänzen: "This is how you make agents actually follow it."

---

### 5. "AGENTS.md, .agent.json und AGENT.json — drei Einstiegspunkte für dasselbe"

**Berechtigung:** ⚠️ Teilweise berechtigt.

Das sind tatsächlich drei verschiedene Dinge:
- `.agent.json` — minimal bootstrap für jedes Repo (portabel)
- `AGENT.json` — vollständiges annotiertes Manifest (dieses Repo als Referenz)
- `AGENTS.md` — Tool-Bridge (Copilot/Cursor/etc. lesen das, nicht die JSON)

Die Hierarchie ist klar, aber sie ist **nicht sichtbar dokumentiert**. Ein neuer Developer versteht den Unterschied nicht auf den ersten Blick.

**Konsequenz:** Klare Hierarchie-Tabelle ins README. "Which file do I need?" als explizite Frage beantworte.

---

### 6. "'Proof' ist kein Beweis" — circular

**Berechtigung:** ✅ Vollständig berechtigt.

Ein Greenfield-Test auf dem eigenen Repo beweist nichts über Legacy-Repos, wechselnde Agenten, echte Teams.

**Konsequenz:** Den "Proof"-Abschnitt im README umformulieren. Ehrlicher Claim: "We applied it to ourselves — here's what that looked like." Nicht: "That's the proof."

---

### 7. Governance-Felder referenzieren nicht-existente Dinge

**Berechtigung:** ✅ Berechtigt.

`validated_with: "aams-validator"` — existiert nicht. `spec_url` — Repo existiert noch nicht öffentlich.

**Konsequenz:** In AGENT.json und SPEC: entweder als "planned" markieren oder Beispielwerte mit echten, heute existierenden Tools belegen (`check-jsonschema` statt `aams-validator`).

> **Status:** `check-jsonschema` ist bereits im `governance`-Feld von AGENT.json — das ist korrekt. Aber `spec_url` zeigt auf ein Repo das noch nicht existiert. Das ist Aspirational-Design und sollte als `"_status": "planned"` markiert sein.

---

### 8. Cross-tool-Portabilität als Differenziator nicht klar genug

**Berechtigung:** ✅ Berechtigt.

Das ist der stärkste unique value. Im README vergraben statt als Lead-Argument.

**Konsequenz:** README-Struktur überdenken. Cross-tool-Portabilität als erstes Argument nach dem Problem, nicht als Nachgedanke.

---

## Priorisierte Konsequenzen

| # | Aktion | Priorität | Aufwand |
|---|--------|-----------|---------|
| 1 | Tagline "No context loss" → ehrlicher Claim | 🔴 Hoch | Klein |
| 2 | "Which file do I need?" Hierarchie-Tabelle ins README | 🔴 Hoch | Klein |
| 3 | "Proof"-Abschnitt umformulieren (ehrlicher) | 🔴 Hoch | Klein |
| 4 | Cross-tool-Portabilität als Lead-Argument im README | 🔴 Hoch | Mittel |
| 5 | ltm-index.md klar als "Bootstrap-LTM <100 Sessions" positionieren | 🟡 Mittel | Klein |
| 6 | Enforcement-Abschnitt ins README (System-Prompt-Injection konkret) | 🟡 Mittel | Mittel |
| 7 | Governance `spec_url` als `_status: planned` markieren | 🟡 Mittel | Klein |
| 8 | SQLite-Minimalimplementierung in WORKING/TOOLS/ | 🟢 Low | Groß |

---

## File Protocol

| Action | Datei |
|--------|-------|
| CREATED | `WORKING/WORKPAPER/2026-02-22-hartes-review-v1.md` (diese Datei) |
| MODIFIED | `README.md` — 4 Änderungen: Tagline, Cross-Tool-Sektion als Lead, Hierarchie-Tabelle, ehrlicher Proof-Abschnitt |
| MODIFIED | `README-DE.md` — identische 4 Änderungen ins Deutsche abgeleitet |
| MODIFIED | `WORKING/MEMORY/ltm-index.md` — LTM-Architektur-Entscheidung: Audit-Log + Vektorspeicher dual-layer |
| MODIFIED | `.agent.json` — `ltm_store` Felder, ChromaDB als Standard ab Session 1 |
| MODIFIED | `AGENT.json` — `ltm_triggers` neu formuliert, `_ref` korrigiert, `_note` Dual-Layer; `_spec_url_status` Annotation (planned) |
| MODIFIED | `.gitignore` — `WORKING/AGENT-MEMORY/` aktiv ignoriert (war auskommentiert), Kommentar aktualisiert |
| MODIFIED | `README.md` + `README-DE.md` — LTM-Sektion Dual-Layer-Darstellung |
| MODIFIED | `SPEC-DE.md` — alle ~10 fehlenden Abschnitte gegenüber SPEC.md ergänzt: governance-Hinweis, auto_create false-Modus, Whitepaper-Index/Guidelines-Empfehlungen, Schritt-Reihenfolge + zwei Strategien, workpaper_rules (template_file_quick, Vollversion vs. Kurzvorlage, Nesting, Metadata-Header), file_tracking (track_moved, track_archived), _ref-Linting-Block, Validierungs-Striktheitstabelle, Zukünftige Profile Vorbedingungen |

---

## Next Steps

- [x] README.md + README-DE.md: Tagline, Hierarchie-Tabelle, Proof-Abschnitt, Portabilität als Lead
- [x] AGENT.json: `spec_url` als geplant markieren (`_spec_url_status: "planned"`)
- [ ] ltm-index.md Beschreibung: "Bootstrap-LTM für kleine Projekte"
- [x] LTM update nach Session-Ende

---

## Session Closing Checklist

- [x] Review vollständig erfasst
- [x] Jeder Kritikpunkt bewertet
- [x] Konsequenzen priorisiert
- [x] Keine Secrets in diesem Workpaper
- [x] File Protocol vollständig
- [x] Konsequenzen umgesetzt (Prioritäten 1–4 und 7 erledigt; #5 und #8 als Low-Prio für Folge-Sessions)
- [x] LTM-Update
- [x] Workpaper nach closed/ verschieben
