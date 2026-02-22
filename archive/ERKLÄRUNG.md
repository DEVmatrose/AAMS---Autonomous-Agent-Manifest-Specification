Agent-Infrastruktur DreamMall Luna-1 — Was wir gebaut haben
Das Problem
Ein KI-Agent (wie GitHub Copilot) hat kein Gedächtnis zwischen Chat-Sessions. Jeder neue Chat startet bei Null. Bei einem Projekt mit 150+ Dokumenten, 60+ historischen Sessions, 5 Subprojekten und laufender Entwicklung über Wochen/Monate geht Kontext unweigerlich verloren. Das führt zu:

Doppelarbeit (Agent kennt vorherige Entscheidungen nicht)
Inkonsistenzen (widersprüchliche Architekturentscheidungen)
Verwaiste Dateien (niemand räumt auf, was ein vergessener Arbeitsstrang hinterlassen hat)
Wissensverlust (was in Session 47 entschieden wurde, weiß Session 48 nicht)
Die Lösung: 4 Säulen
1. WORKING/ — Der Agent-Koordinations-Hub
Ein zentraler Ordner im Projekt-Root, der alles bündelt, was ein Agent zum Arbeiten braucht:
WORKING/
├── WHITEPAPER-DREAMMALL/docs/  ← 60+ permanente technische Dokumente
├── WORKPAPER/                  ← Aktive Sessions (6 offen)
│   └── close/                  ← 60+ abgeschlossene Sessions (historisch)
├── DATABASE/                   ← Migrations + Scripts (zentral, nicht im Backend)
├── GUIDELINES/                 ← Coding-Standards, Architektur-Regeln
├── TOOLS/                      ← vastai-manager, whitepaper-export
└── AGENT-MEMORY/               ← ChromaDB Vector Store (LTM)


Warum: Ein Agent muss wissen wo er nachschauen soll. Statt über 20 Ordner verstreuter Doku gibt es jetzt einen einzigen Hub. Jedes Unterverzeichnis hat eine klare Rolle.

2. READ-AGENT.md — Single Entry Point
Ein Dokument, das jeder Agent, Mensch oder KI-Tool zuerst lesen soll. Enthält:

Projektstruktur auf einen Blick
"Wo anfangen?" — priorisierte Leseliste
Kernarchitektur in 4 Zeilen
Service-Ports und Start-Befehle
KI-Infrastruktur (lokal vs. Vast.ai)
Security-Regeln (Kurzform)
LTM-Pflicht-Trigger (die 11 Punkte)
Warum: Ohne klaren Einstiegspunkt liest ein Agent zufällig irgendwelche Dateien. READ-AGENT.md gibt ihm in 30 Sekunden Orientierung.

3. Agent Long-Term Memory (LTM) — ChromaDB Vector Store
Das Herzstück. Ein lokaler semantischer Suchindex über alle Projekt-Dokumentation:

Was es kann:
```
# Kontext laden (vor der Arbeit)
python query.py "Wie funktioniert die Supabase Auth im Backend?"
# → Findet AUTH-Access-System.md, DEV-Coding-Standards.md, relevante Workpapers

# Re-Index (nach Änderungen)
python ingest.py
# → 152 Dateien → 1.776 Chunks → ~29 Sekunden
```

Technisch:

ChromaDB (Open Source, lokal, kein API-Key nötig)
all-MiniLM-L6-v2 Embedding-Modell (~80MB, kostenlos)
Chunking an H2-Headern, Metadaten pro Chunk (Quelle, Kategorie, Abschnitt)
18 Kategorien (architecture, feature, kairos-ai, workpaper, etc.)
Cosine Similarity Suche mit HNSW-Index
Das Entscheidende sind die 11 Trigger-Punkte — feste Regeln, WANN das LTM benutzt werden MUSS:

Priorität	Trigger	Aktion
PFLICHT	Neues Workpaper erstellen	Query: Kontext laden
PFLICHT	Neuen Copilot-Chat öffnen	Query: Session-Thema laden
PFLICHT	Chat-Kontextlimit erreicht	Ingest → Query im neuen Chat
PFLICHT	Workpaper abgeschlossen	Ingest VOR Verschiebung nach close/
Session-Ende	Workpaper/Whitepaper geändert	Ingest (gebündelt)
Session-Ende	Dateien gelöscht/hinzugefügt	Ingest
Session-Ende	DB-Migration hinzugefügt	Ingest
Empfohlen	Code-Änderungen	Query: Standards prüfen
Empfohlen	Package installiert	Ingest bei Doku-Relevanz
Empfohlen	Testscript erstellt	Query: Modul-Kontext
Warum Trigger statt "benutze es halt": Ohne verbindliche Trigger wird das LTM vergessen. Die Trigger sind jetzt in 4 Dokumenten gleichzeitig verankert (copilot-instructions.md, READ-AGENT.md, Workpaper-Standard, AGENT-MEMORY/README.md), sodass ein Agent sie nicht übersehen kann.

4. Session-Hygiene-Standard — Nachvollziehbarkeit
Jedes Workpaper hat Pflichtabschnitte:

Session Scope — Was ist das Ziel? Welcher Kontext aus vorherigen Sessions?
Datei-Protokoll — Jede erstellte/geänderte/gelöschte Datei wird erfasst
Session-Abschluss Checkliste — Inkl. "Keine Secrets?", "LTM Re-Ingest?"
Warum: Ein Agent der in 3 Wochen ein altes Workpaper liest, muss sofort sehen: Was wurde gebaut, was wurde verworfen, was ist offen, welche Dateien gehören dazu.

Zusammenspiel im Alltag

                    ┌─────────────────────────────────┐
                    │   Neuer Copilot-Chat geöffnet   │
                    └──────────────┬──────────────────┘
                                   ▼
                    ┌─────────────────────────────────┐
                    │  🧠 LTM Query: Session-Kontext  │ ← PFLICHT (T2)
                    │  python query.py "<Thema>"      │
                    └──────────────┬──────────────────┘
                                   ▼
                    ┌─────────────────────────────────┐
                    │  READ-AGENT.md lesen             │ ← Orientierung
                    │  Aktive Workpapers lesen         │
                    └──────────────┬──────────────────┘
                                   ▼
                    ┌─────────────────────────────────┐
                    │  Arbeiten + Datei-Protokoll      │
                    │  Bei Code-Änderungen: LTM Query  │ ← EMPFOHLEN (T6)
                    └──────────────┬──────────────────┘
                                   ▼
                    ┌─────────────────────────────────┐
                    │  Session-Ende:                    │
                    │  🧠 LTM Re-Ingest               │ ← PFLICHT
                    │  Checkliste ausfüllen            │
                    │  Workpaper → close/ wenn fertig  │
                    └─────────────────────────────────┘

                    
Was das NICHT ist
Kein autonomer Agent — es ist ein Agent-Unterstützungssystem. Der Mensch arbeitet weiterhin mit Copilot, aber Copilot hat jetzt Regeln, wann er sein Gedächtnis benutzen muss.
Kein Cloud-Service — alles lokal. ChromaDB auf Disk, kein API-Key, kein Abo, keine Kosten.
Kein Ersatz für Dokumentation — es macht vorhandene Dokumentation auffindbar. Die Qualität hängt weiterhin davon ab, dass Whitepapers und Workpapers gut geschrieben sind.