# WP-001 — AAMS Projektübersicht
## Was haben wir vor uns?

- **ID:** WP-001
- **Erstellt:** 2026-02-22
- **Letztes Update:** 2026-02-22
- **Status:** Aktiv
- **Typ:** Architektur / Projektverständnis

---

## 1. Was ist dieses Projekt?

**Autonomous Agent Manifest Specification (AAMS)** ist ein offener Standard — keine Software, keine Runtime, kein Framework.

Es ist eine **deklarative Spezifikation** in Form einer JSON-Datei, die in jedes Repository gelegt werden kann und definiert, wie ein KI-Agent in diesem Projekt arbeitet.

Kerngedanke:
> `README.md` ist für Menschen. `AGENT.json` ist für Maschinen.

---

## 2. Das Problem das AAMS löst

Klassische Softwareentwicklung: Entwickler → Git → Issues → PR → Merge.  
Jeder Entwickler hat Kontext im Kopf. Der nächste liest die Commit-History.

Agentisches Arbeiten: Agent → Session → Ergebnis → Context lost.  
Session N+1 weiß nicht was Session N entschieden hat.

Ohne AAMS:
- Kein Gedächtnis über Sessions hinweg
- Keine definierte Struktur wo Dokumentation liegt
- Keine Regeln was der Agent anfassen darf
- Kein Einstiegspunkt für einen neuen Agenten
- Kontextverlust is unvermeidlich

Mit AAMS:
- Jede Session beginnt mit Kontext (LTM-Abfrage)
- Jede Entscheidung ist dokumentiert (Workpaper)
- Stabile Architekturwissen ist persistent (Whitepaper)
- Neue Agenten finden sofort Orientierung (READ-AGENT.md + WORKING/)

---

## 3. Zwei Formen des Standards

### Vollständig: `AGENT.json`
Komplettes Manifest mit allen Sektionen:
- `identity` — Agent-Identität und Versioning
- `runtime` — Modell, Provider, Endpoint
- `skills` — Fähigkeiten und Custom Skills
- `permissions` — was darf der Agent (Filesystem, Network, Process, Data)
- `memory` — Short-term / Long-term / Session
- `session` — Workpaper-Erstellung, Logging, Audit
- `tools` — externe Tools und API-Bindings
- `workspace` — Struktur, Onboarding, Regeln, Code-Hygiene
- `governance` — Spec-Version, Validierung, Review-Intervall

### Minimal: `.agent.json`
Kleinste portable Form. Bootstrap-Contract.  
Enthält nur: `workspace.structure`, `documentation_model`, `bootstrap_rules`, `secrets_policy`, `agent_contract`.  
Kann in jedes Repo ohne den vollen Manifest gelegt werden.

---

## 4. Dreischichten-Dokumentationsmodell

Das Herzstück der AAMS-Architektur:

```
WORKING/
├── WHITEPAPER/     Stabile Systemwahrheit — Was ist dieses System?
│                   Nie löschen. Nur bei Architekturentscheidungen updaten.
│
├── WORKPAPER/      Operative Session-Arbeit — Was tue ich jetzt?
│                   Pro Session eine Datei. Nach Abschluss → closed/
│   └── closed/
│
└── MEMORY/         Langzeitgedächtnis — Was haben wir gelernt?
                    Cross-Session-Kontext. Ingest nach jeder Session.
```

**Warum drei Schichten?**

Ein menschlicher Entwickler hat:
- Notizblock (Workpaper) — was er gerade macht
- Architektur-Doku (Whitepaper) — wie das System aufgebaut ist
- Erfahrung / Gedächtnis (LTM) — was er über die Zeit gelernt hat

Ein Agent braucht dasselbe, aber explizit und persistent.

---

## 5. Bootstrap-Ablauf (normativ)

Wenn ein Agent ein Repo mit AAMS betritt:

```
1. READ-AGENT.md lesen
2. WORKING/-Struktur prüfen → anlegen wenn fehlend (idempotent)
3. Repository scannen → Inventory im ersten Workpaper
4. LTM befragen für Session-Thema
5. Workpaper öffnen / erstellen
6. Arbeiten
7. Workpaper abschließen (File Protocol + Next Steps)
8. LTM ingestieren
9. Workpaper → closed/
```

---

## 6. Interoperabilität

AAMS ist framework-neutral.  
Jedes Agenten-Framework das `WORKING/`-Struktur erkennt, kann AAMS-Repos direkt nutzen.

- **Eigenes Framework vorhanden:** AAMS-Struktur wird als Subagenten-Workspace erkannt
- **Kein Framework:** `.agent.json` + `READ-AGENT.md` mocken ein Minimal-Framework

Langfristiges Ziel: AAMS wird zu einem **de-facto Standard** den jedes Agenten-Framework versteht.

---

## 7. Kernprinzipien

1. **Deklarativ** — Manifest beschreibt Struktur, Agent handelt
2. **Idempotent** — mehrfaches Lesen ändert nichts
3. **Nie löschen** — Bootstrap-Regeln erzeugen nur, vernichten nie
4. **Secret-frei** — keine Credentials in Manifesten, Workpapers oder LTM
5. **Local-first** — funktioniert ohne Cloud, ohne externe Dienste
6. **Portabel** — eine Datei, funktioniert in jedem Repo

---

## 8. Aktueller Stand (2026-02-22)

| Bereich | Status |
|---|---|
| Spezifikation (SPEC.md / SPEC-DE.md) | Vollständig, Draft |
| Referenz-Manifest (AGENT.json) | Vollständig, annotiert |
| JSON Schema (AGENT_SCHEMA.json) | Vollständig |
| Minimal-Bootstrap (.agent.json) | Neu erstellt |
| READ-AGENT.md | Neu erstellt |
| WORKING/-Struktur | Angelegt, aktiv |
| Erstes Workpaper | Vorhanden |
| LTM | Initial befüllt |
| GitHub Issues #1-#3 | Adressiert, zur Schließung bereit |
