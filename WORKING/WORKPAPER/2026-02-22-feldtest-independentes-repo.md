# Workpaper: 2026-02-22 — Feldtest AAMS in unabhängigem Repo

- **Date:** 2026-02-22
- **Agent:** GitHub Copilot / Claude Sonnet 4.6
- **Topic:** Live-Test von AAMS/1.0 in einem bestehenden, unabhängigen Repository
- **Status:** 🚧 IN PROGRESS

---

## Session Scope

AAMS wurde bisher nur auf dem eigenen Repo getestet — dem Repo das den Standard selbst beschreibt. Das ist kein unabhängiger Beweis. Ziel dieser Session: AAMS in einem echten, bereits bestehenden Projekt einsetzen. Nichts Setup-Greenfield, sondern Legacy: ein Repo mit bestehendem Code, bestehendem Chaos, ohne AAMS-Vorkenntnis.

**Kontext aus vorherigen Sessions:**
- AAMS/1.0 vollständig: Spec, Schema, README, GitHub Pages, ChromaDB, alle Workpapers geschlossen
- GitHub Pages live (nach Setup durch User)
- `curl -sO https://raw.githubusercontent.com/aams-spec/aams/main/.agent.json` → ein Befehl, bootstrappable

---

## Ziel dieser Session (ein Satz)

AAMS in ein unabhängiges, bestehendes Repo einsetzen und dokumentieren was funktioniert, was fehlt, und was wir für v1.1 brauchen.

---

## Betroffene Bereiche

- Externes Repo (User wählt) — kein Eingriff in dieses Repo
- Erkenntnisse fließen zurück in AAMS-Repo als Feedback
- Eventuell: SPEC.md / AGENT.json Korrekturen basierend auf Felderfahrung

---

## Testplan

### Schritt 1 — Repo auswählen

Kriterien für den Test-Repo:
- Bestehendes, echtes Projekt (kein Greenfield)
- Kein AAMS, kein `WORKING/`, kein `.agent.json`
- Möglichst unterschiedlich von diesem Repo (andere Sprache, anderes Ziel)

### Schritt 2 — Bootstrap ausführen

```bash
# Im Root des Test-Repos
curl -sO https://raw.githubusercontent.com/aams-spec/aams/main/.agent.json
```

Dann Agent (Copilot / Claude / Cursor) auf das Repo loslassen mit Anweisung:
> "Lies `.agent.json` und bootstrappe den Workspace."

### Schritt 3 — Beobachten & dokumentieren

Was wird korrekt angelegt? Was fehlt? Wo ist die Spec unklar?

| Erwartung | Beobachtung | Bewertung |
|-----------|-------------|-----------|
| Agent liest `.agent.json` | ? | ? |
| `WORKING/` Struktur wird angelegt | ? | ? |
| Erstes Workpaper wird erstellt | ? | ? |
| LTM wird befüllt | ? | ? |
| Agent macht READ-AGENT.md | ? | ? |

### Schritt 4 — Eine echte Aufgabe

Der Agent soll eine echte, kleine Aufgabe erledigen — nicht nur bootstrappen. Ziel: prüfen ob das Workpaper-System im Alltag hält.

### Schritt 5 — Feedback zurückschreiben

Was muss in AAMS verbessert werden?

---

## Hypothesen (vor dem Test)

1. **Bootstrap funktioniert** — `.agent.json` ist klar genug, Agent legt `WORKING/` an
2. **LTM-Trigger werden vergessen** — Agenten ingestieren nicht automatisch ohne expliziten Hinweis
3. **code_hygiene wird ignoriert** — Agenten lesen es, folgen aber nicht konsequent
4. **Workpaper-Qualität sinkt** — Ohne Feedback schreibt der Agent kürzere, weniger nützliche Workpapers

---

## Ergebnisse

*(nach Feldtest auszufüllen)*

---

## File Protocol

| Action | Datei | Notiz |
|--------|-------|-------|
| CREATED | `WORKING/WORKPAPER/2026-02-22-feldtest-independentes-repo.md` | Diese Datei |

---

## Entscheidungen & Rationale

| Entscheidung | Rationale |
|---|---|
| Test vor v1.1 planen | Kein Standard ohne Feldbeweis außerhalb des eigenen Repos |
| Bestehender Repo, kein Greenfield | Greenfield-Test wäre zu einfach — echte Projekte haben Kontext, Altlasten, Struktur |
| Erkenntnisse → SPEC.md-Korrekturen | Feedback-Loop ist Teil der AAMS-Disziplin |

---

## Offene Fragen

1. **Welches Repo?** — User entscheidet. Empfehlung: ein kleineres Projekt mit 50–500 Dateien.
2. **Welcher Agent?** — Copilot empfohlen (bereits konfiguriert via AGENTS.md). Claude/Cursor auch möglich.
3. **Was ist "erfolgreich"?** — Mindest-Definition: `WORKING/` angelegt, erstes Workpaper mit Datei-Protokoll erstellt, LTM initiales Ingest.

---

## Next Steps

- [ ] Externes Test-Repo auswählen (User)
- [ ] Bootstrap ausführen: `.agent.json` reinlegen, Agent loslassen
- [ ] Testplan Schritt 3 ausfüllen (Beobachtungen)
- [ ] Echte Aufgabe durchführen
- [ ] Feedback dokumentieren und in AAMS-Repo aufnehmen
- [ ] LTM-Update nach Session-Ende
- [ ] Workpaper nach `closed/` verschieben

---

## Session Closing Checklist

- [x] Scope klar definiert
- [x] Testplan dokumentiert
- [x] Hypothesen formuliert
- [x] Keine Secrets in diesem Workpaper
- [ ] Feldtest durchgeführt
- [ ] Beobachtungen dokumentiert
- [ ] Feedback in AAMS eingearbeitet
- [ ] LTM-Update
- [ ] Workpaper nach closed/ verschieben
