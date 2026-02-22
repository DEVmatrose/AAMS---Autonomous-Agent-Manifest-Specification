# Land in Sicht: Dein Repo als agentischer Arbeitsraum

> **AAMS — Autonomous Agent Manifest Specification**  
> `README.md` ist für Menschen. `AGENT.json` ist für Maschinen.

Wer auf hoher See überleben will, braucht zwei Dinge: eine gute Crew — und eine Karte, die jeder lesen kann. Auch der neue Matrose. Auch die Ablösung in der Nachtschicht. Auch eine KI.

Genau das ist AAMS — die Autonomous Agent Manifest Specification.

---

## Das Problem bleibt. Die Lösung ist jetzt klarer.

Session 48 weiß nicht, was Session 47 entschieden hat. Das war das Problem damals. Es ist das Problem heute. Und kein Agenten-Framework der Welt löst es — weil das Problem nicht im Framework liegt. Es liegt in der Struktur des Repos.

Ein Repo ohne Agenten-Struktur ist wie ein Schiff ohne Logbuch. Jeder weiß, was er gestern gemacht hat. Niemand weiß, was vor ihm war.

---

## Die Erkenntnis nach einem Jahr

Ich habe über ein Jahr mit KI-Agenten in echten Projekten gearbeitet. Was ich gelernt habe:

> Das Wichtigste ist nicht, dass Agenten Code schreiben können.  
> Das Wichtigste ist, dass sie wissen **wo sie sind**.

Wer keine Struktur hat, verliert den Kontext. Wer den Kontext verliert, macht Fehler. Doppelentscheidungen. Verwaiste Dateien. Technische Schuld die kein Mensch bestellt hat.

Die Lösung ist keine neue KI. Die Lösung ist **Disziplin im Repo**.

---

## AAMS ist kein Framework

Das ist die wichtigste Klarstellung.

AAMS ist kein Tool. Keine Runtime. Kein Framework das installiert werden muss.

AAMS ist eine **einzelne Datei** die in jedes Repo gelegt wird:

```
.agent.json
```

Ein Agent der diese Datei liest, weiß sofort:

- Wo Dokumentation hingehört
- Wie Sessions strukturiert werden
- Wo das Langzeitgedächtnis liegt
- Was er darf — und was nicht

Kein `npm install`. Kein `pip install`. Kein Setup.

---

## Das Dreischichten-Dokumentationsmodell

Der eigentliche Kern von AAMS. Drei Schichten, verbindlich:

**Workpaper** — Was mache ich gerade in dieser Session?  
Wird beim Sessionstart erstellt, beim Sessionende archiviert. Mit vollständigem File Protocol: was wurde erstellt, geändert, gelöscht.

**Whitepaper** — Wie ist dieses System aufgebaut?  
Stabile Architekturwahrheit. Wird einmal geschrieben, nur bei Architekturentscheidungen angepasst. Nie gelöscht.

**Long-Term Memory** — Was haben wir über die Zeit gelernt?  
Nach jeder Session wird das Workpaper ins LTM ingested. Session N+1 fragt das LTM bevor sie anfängt. Kein Kontextverlust mehr.

```
WORKING/
├── WHITEPAPER/     ← Stabile Systemwahrheit. Nie löschen.
├── WORKPAPER/      ← Aktive Session-Arbeit. Pro Session eine Datei.
│   └── closed/     ← Archivierte abgeschlossene Sessions.
└── MEMORY/         ← Langzeitgedächtnis. Cross-Session-Kontext.
```

Ein guter Entwickler macht das im Kopf. Ein Agent braucht es explizit und persistent.

---

## Der Agent Contract

Eine `READ-AGENT.md` im Repo-Root definiert den normativen Contract für jeden Agenten der dieses Repo betritt.

Wer als Agent dieses Repo betritt, führt diesen Contract aus. Keine Diskussion. Keine Interpretation.

```
On first entry:       Read READ-AGENT.md → check structure → scan repo → index into MEMORY/
On session start:     Read READ-AGENT.md → check last workpaper → query MEMORY/
On session end:       Complete workpaper → ingest → move to closed/ → update READ-AGENT.md
```

Funktioniert mit jedem Agenten-Framework. Und ohne jedes Framework.

---

## Portabel in jedes Repo

Das entscheidende Designziel: **eine Datei, jedes Repo**.

Hat ein Entwickler ein eigenes Agenten-Framework? Sein Framework erkennt die `WORKING/`-Struktur und nutzt sie direkt als Subagenten-Workspace.

Hat ein Entwickler kein Framework? `.agent.json` + `READ-AGENT.md` sind das kleinste mögliche Agentenframework — deklarativ, idempotent, ohne Abhängigkeiten.

Langfristiges Ziel: AAMS wird zum de-facto Standard den jeder Agent in jedem Repo erkennt.

---

## Der Beweis: AAMS an sich selbst getestet

Dieses Projekt — das Projekt das den Standard beschreibt — hat ihn heute live angewendet.

Eine `.agent.json` gelesen. Struktur angelegt. Erstes Workpaper erstellt. Erstes Whitepaper geschrieben. LTM befüllt. Drei offene GitHub Issues aufgelöst.

Alles dokumentiert. Alles nachvollziehbar. Kein Kontextverlust.

**Das ist der Beweis.**

---

## Technische Spezifikation

| Datei | Inhalt |
|---|---|
| [`SPEC-DE.md`](./SPEC-DE.md) | Vollständige technische Referenz |
| [`AGENT.json`](./AGENT.json) | Annotiertes Referenz-Manifest |
| [`.agent.json`](./.agent.json) | Minimaler Bootstrap-Contract |
| [`AGENT_SCHEMA.json`](./AGENT_SCHEMA.json) | JSON Schema zur Validierung |

---

## Lizenz

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) — gemeinfrei. Nutzen, forken, drauf aufbauen.

---

*Eine Datei. Jedes Repo. Kein Chaos mehr.*

