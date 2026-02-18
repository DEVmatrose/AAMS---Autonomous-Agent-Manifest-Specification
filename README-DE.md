---

# AAMS — Autonomous Agent Manifest Specification

> **Der fehlende Standard für KI-Agenten die in Repositories arbeiten.**
> `README.md` ist für Menschen. `AGENT.json` ist für Maschinen.

---

## Das Problem

Jedes Repository hat eine `README.md`. Sie erklärt Menschen, worum es geht, wie man installiert und wie man beiträgt.

Aber wenn ein KI-Agent dieses Repo klont, hat er keine Ahnung: Wo soll ich meine Arbeit ablegen? Wie behalte ich Kontext zwischen Sessions? Was darf ich anfassen? Wo dokumentiere ich Entscheidungen? Wie baue ich ein Langzeitgedächtnis für dieses Projekt auf?

Jede neue Chat-Session startet bei Null. Kontext geht verloren. Entscheidungen werden doppelt getroffen. Dateien verwaisen. Was in Session 47 entschieden wurde, weiß Session 48 nicht.

Das ändern wir.

---

## Was ist AAMS?

AAMS ist ein offener Standard für eine maschinenlesbare Manifest-Datei — `AGENT.json` — die in jedem Repository liegt, direkt neben der `README.md`, und einem KI-Agenten sagt: **So arbeitest du in diesem Projekt.**

Sie definiert:
- **Workspace-Struktur** — wo Whitepapers, Workpapers, Guidelines und Tools liegen
- **Memory** — wie Langzeitgedächtnis (LTM) für das Projekt aufgebaut und gepflegt wird
- **Session-Hygiene** — wie Arbeit protokolliert, Audit-Trails erstellt und Sessions sauber abgeschlossen werden
- **Permissions** — was der Agent lesen, schreiben, ausführen darf und was verboten ist
- **Tools** — welche externen Tools und APIs der Agent nutzen darf

```
beliebiges-projekt/
├── README.md        ← für Menschen    (Überblick, Setup, Contribution)
├── AGENT.json       ← für Maschinen   (Workspace, Permissions, Memory, Sessions, Tools)
└── WORKING/         ← Agent-Workspace (angelegt nach AGENT.json)
    ├── docs/        ← Whitepapers (Langzeit-Projektwissen)
    ├── WORKPAPER/   ← Aktive Arbeitssessions
    │   └── close/   ← Archivierte Sessions
    ├── GUIDELINES/  ← Coding-Standards, Architektur-Regeln
    └── TOOLS/       ← Projekt-spezifische Skripte
```

Eine Datei. Ein Standard. Liegt neben deiner README. Funktioniert mit jedem Modell, jeder Runtime, jedem Stack.

---

## So funktioniert es

### Erstkontakt (Onboarding)

1. **Agent klont ein Repo** und findet `AGENT.json`
2. **Liest den Entry-Point** (`READ-AGENT.md`) — hat in 30 Sekunden Projektkontext
3. **Legt die Workspace-Struktur an** — den `WORKING/`-Ordner mit allen Unterverzeichnissen
4. **Scannt das Repository** — Dateien, Sprachen, Abhängigkeiten, bestehende Dokumentation
5. **Erstellt Guidelines** — leitet Coding-Standards und Architektur-Regeln aus dem Projekt ab
6. **Indexiert alles ins LTM** — alle Doku in den Vektorspeicher (z.B. ChromaDB)
7. **Erstellt erstes Workpaper** — Onboarding-Protokoll das dokumentiert was gefunden wurde

Alle Schritte stehen in `workspace.onboarding` — nicht hartcodiert, pro Projekt konfigurierbar.

### Jede Session

1. **LTM abfragen** — Kontext für das Session-Thema laden (Pflicht-Trigger)
2. **Offene Workpapers lesen** — weitermachen wo die letzte Session aufgehört hat
3. **Arbeiten** — nach Permissions, Tool-Bindings, Coding-Guidelines und Code-Hygiene-Regeln
4. **Dokumentieren** — jede erstellte/geänderte/gelöschte Datei ins Workpaper (fortlaufend, nicht erst am Ende)
5. **Session abschließen** — Closing-Checkliste (keine Secrets? keine Temp-Dateien? kein verlassener Code?), LTM Re-Ingest, Workpaper archivieren

### Das Ergebnis

Kein Kontextverlust. Keine Doppelarbeit. Keine verwaisten Dateien. Session N+1 weiß was Session N entschieden hat.

---

## Dein Manifest validieren

```bash
# Node.js
npm install -g ajv-cli
ajv validate -s AGENT_SCHEMA.json -d AGENT.json

# Python
pip install check-jsonschema
check-jsonschema --schemafile AGENT_SCHEMA.json AGENT.json
```

✅ Valide. Fertig.

---

## Spezifikation

Die vollständige Spezifikation liegt in `SPEC.md`.

### Sektionen auf einen Blick

| Sektion       | Pflicht | Zweck |
|---------------|---------|-------|
| `identity`    | ✅      | Name, Version, Agententyp |
| `runtime`     | ✅      | Modell, Provider, Endpoint |
| `skills`      | ✅      | Deklarierte Fähigkeiten |
| `permissions` | ✅      | Explizite Erlaubnisse und Verbote |
| `memory`      | ✅      | Kurzzeit-, Langzeit-, Session-Persistenz |
| `session`     | ✅      | Logging, Workpaper, Audit-Trail |
| `tools`       | ✅      | Externe Tool- und API-Bindings |
| `workspace`   | ✅      | Arbeitsverzeichnis, Onboarding, Session-Hygiene, Code-Hygiene, Secrets-Policy |
| `governance`  | ⬜      | Compliance- und Review-Metadaten |
| `metadata`    | ⬜      | Freiformfeld für Provider-Erweiterungen und projekt-spezifische Daten |

**Grundprinzip: Default-Deny.** Alles was nicht explizit erlaubt ist, ist verboten.

---

## Designprinzipien

**Local-first.** Version 1.0 ist für selbst gehostete Agenten mit lokalen Modellen gebaut. Cloud- und Multi-Agent-Mesh-Profile sind geplant — Beiträge willkommen.

**Workspace-getrieben.** Ein Agent der ein Repo klont bekommt eine definierte Arbeitsstruktur — Whitepapers für Langzeitwissen, Workpapers für Sessions, Guidelines für Standards. Kein Raten mehr, wo was hinkommt.

**Explizit statt implizit.** Permissions werden deklariert, nicht angenommen. Ein Agent der eine Fähigkeit nicht deklariert, hat sie nicht.

**Kontinuität über Sessions.** Langzeitgedächtnis, Session-Logs und Workpaper-Archive stellen sicher, dass Session N+1 weiß was Session N entschieden hat.

**Maschinenlesbar, menschlich prüfbar.** JSON für Maschinen, `_doc`-Felder für die Menschen die es reviewen.

**Stack-agnostisch.** Funktioniert mit Ollama, LM Studio, llama.cpp, OpenAI, Anthropic oder jedem eigenen Endpoint.

---

## Roadmap

| Profil     | Status        | Beschreibung |
|------------|---------------|--------------|
| `local-v1` | ✅ Aktuell    | Self-hosted, lokale Modelle |
| `cloud-v1` | 🔜 Geplant   | Cloud-Provider, API-Keys, Rate-Limits |
| `mesh-v1`  | 🔜 Geplant   | Multi-Agent-Koordination, Trust-Level |
| `edge-v1`  | 💡 Idee      | IoT und Edge-Deployment |

---

## Repository-Struktur

```
aams/
├── README.md              ← du bist hier
├── SPEC.md                ← vollständige Spezifikation
├── AGENT.json             ← annotiertes Template
├── AGENT_SCHEMA.json      ← JSON Schema zur Validierung
└── registry/
    └── capabilities.md    ← Standard-Capability-Registry (folgt)
```

**In deinem Projekt (nach Agent-Setup):**

```
dein-projekt/
├── README.md              ← für Menschen
├── AGENT.json             ← für Agenten
├── READ-AGENT.md          ← Agent-Einstiegspunkt
└── WORKING/               ← vom Agent angelegt
    ├── docs/              ← Whitepapers (Architektur, Entscheidungen)
    ├── WORKPAPER/         ← Aktive Sessions
    │   └── close/         ← Archivierte Sessions
    ├── GUIDELINES/        ← Coding-Standards, Regeln
    ├── TOOLS/             ← Projekt-spezifische Skripte
    └── AGENT-MEMORY/      ← LTM-Vektorspeicher (z.B. ChromaDB)
```

---

## Mitmachen

AAMS ist ein offener Standard. Das Feld ist leer und es gibt viel zu bauen.

**Möglichkeiten beizutragen:**
- Neue Standard-Capabilities vorschlagen → `registry/capabilities.md`
- Die Profile `cloud-v1` oder `mesh-v1` mitgestalten
- Validator-Tooling oder GitHub Actions bauen
- Eigene `AGENT.json` als Referenz-Implementierung einreichen
- Issues öffnen für Fälle die der Standard noch nicht abdeckt

Issue oder Pull Request öffnen. Alle Hintergründe willkommen — Agent-Entwickler, Security-Forscher, Plattform-Ingenieure und alle die finden, dass KI-Infrastruktur ordentliche Standards verdient.

---

## Lizenz

AAMS Specification 1.0 steht unter [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

Die Spezifikation ist gemeinfrei. Nutzen, forken, drauf aufbauen. Keine Erlaubnis nötig.

---

*Ja, dieses Projekt hat eine `README.md`. Die Ironie ist Absicht.*