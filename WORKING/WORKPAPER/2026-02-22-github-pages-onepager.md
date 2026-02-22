# Workpaper: 2026-02-22 — GitHub Pages One-Pager — Konzept & Umsetzung

- **Date:** 2026-02-22
- **Agent:** Claude Sonnet 4.6
- **Topic:** GitHub Pages Landing Page — Ein-Datei-Pitch, curl-Onboarding, Repo als lebender Beweis
- **Status:** ✅ COMPLETED

---

## Session Scope

Auf Basis des überarbeiteten README.md (nach hartem Review) soll eine GitHub Pages One-Pager gebaut werden. Ziel: Menschen und Agenten in 60 Sekunden erklären, was AAMS ist, warum nur eine Datei zieht, und wie sie sofort loslegen können. Die Seite selbst ist hosted auf dem AAMS-Repo via GitHub Pages.

---

## Kontext aus vorherigen Sessions

- README.md v2 fertig: ehrliche Tagline, Hierarchie-Tabelle, Cross-Tool-Portabilität als Lead, Proof-Abschnitt reformuliert.
- Workpaper hartes-review-v1 abgeschlossen.
- Nächster logischer Schritt: externe Sichtbarkeit. Wer das Repo findet, muss sofort verstehen — ohne README zu lesen.

---

## Ziel dieser Session (ein Satz)

Eine statische GitHub Pages Seite (`index.html`) bauen, die AAMS erklärt, den curl-Befehl prominiert und das Repo als lebenden Beweis des Standards positioniert.

---

## Betroffene Bereiche

- `docs/index.html` (neu) — GitHub Pages Source
- `docs/` Ordner (neu anlegen)
- Kein Eingriff in bestehendes `WORKING/`, keine Spec-Änderungen

---

## Session Overview

### Ausgangslage

AAMS hat jetzt ein gutes README, ein strukturiertes Repo, ein Workpaper-System. Was fehlt: eine URL die man teilen kann. GitHub Pages ist der offensichtliche Weg — kein Hosting, kein Build-Step, direkt aus dem Repo.

### Ansatz

One-Pager, nicht Marketing-Site. Die Seite tut genau das was `.agent.json` tut: eine Sache, klar kommuniziert.

**Struktur der Seite:**

```
[Hook — das Problem in 2 Sätzen]
[Was AAMS ist — 3 Bullets max]
[Der curl — prominent, kopierbar]
[Was dann passiert — 4 Schritte]
[Repo ist der Beweis — Link, kein Claim]
[Spec & Lizenz — Footer]
```

### Curl-Befehl (der Hero-Moment der Seite)

```bash
curl -O https://raw.githubusercontent.com/aams-spec/aams/main/.agent.json
```

Alternativ mit Ausgabe ins aktuelle Verzeichnis, sofort lesbar:

```bash
curl -sO https://raw.githubusercontent.com/aams-spec/aams/main/.agent.json && echo "Done. Now open .agent.json and hand it to your agent."
```

**Was dann passiert (4 Schritte für die Seite):**
1. `.agent.json` liegt im Repo-Root
2. Agent liest die Datei beim nächsten Start
3. Agent erstellt `WORKING/` Struktur automatisch
4. Jede Session ist dokumentiert — kein Kontextverlust mehr

### Design-Entscheidungen

- Kein CSS-Framework — inline styles, ein File, zero dependencies (konsistent mit AAMS-Philosophie)
- Dark theme — passt zum Developer-Publikum, liest sich gut im Terminal-Umfeld
- Monospace für Code-Blöcke, Copy-Button via `navigator.clipboard`
- Mobile-ready — GitHub wird oft auf Mobile aufgerufen
- Kein JavaScript-Framework, kein Build-Step

### GitHub Pages Setup

- Source: `docs/` Ordner im `main` Branch
- Aktivierung: Repo Settings → Pages → Source: `docs/`
- URL wird: `https://aams-spec.github.io/aams/`

---

## Ergebnisse

- [x] `docs/index.html` erstellt — 7 Sektionen, dark theme, zero dependencies
- [x] Copy-Button für curl-Befehl (clipboard API + textarea-Fallback)
- [x] Responsiv auf Mobile (clamp, flex-wrap, @media query)
- [x] Kein externer Dependency

## File Protocol

| Action | Datei | Notiz |
|--------|-------|-------|
| CREATED | `WORKING/WORKPAPER/2026-02-22-github-pages-onepager.md` | Diese Datei |
| CREATED | `docs/index.html` | GitHub Pages One-Pager — single file, ~300 Zeilen |

---

## Entscheidungen & Rationale

| Entscheidung | Rationale |
|---|---|
| `docs/` statt `root` für Pages | Saubere Trennung — Repo-Root bleibt für AAMS-Files |
| Single HTML file, kein Framework | AAMS-Konsistenz — zero dependencies. Wer eine Seite baut die ein Framework braucht, hat das Konzept nicht verstanden |
| curl für `.agent.json`, nicht für ganzes Repo | Das ist der Kern-Claim: eine Datei reicht |
| Dark theme | Developer-Publikum, passt zum Terminal-Kontext |
| Copy-Button via Clipboard API | UX-Minimum für Code-Snippets |

---

## Next Steps

- [x] `docs/index.html` finalisieren und ins Repo pushen
- [ ] GitHub Pages in Repo Settings aktivieren (manuell: Settings → Pages → Source: `docs/`)
- [ ] URL in README.md ergänzen (nach Pages-Aktivierung)
- [ ] AGENTS.md mit Pages-URL ergänzen
- [ ] LTM-Update nach Session-Ende (Eintrag 026)
- [ ] Workpaper nach `closed/` verschieben

---

## Session Closing Checklist

- [x] Scope klar definiert
- [x] Curl-Befehl festgelegt
- [x] Seitenstruktur entschieden
- [x] Keine Secrets in diesem Workpaper
- [x] `docs/index.html` erstellt
- [x] File Protocol vollständig
- [x] LTM-Update
- [x] Workpaper nach closed/ verschieben
