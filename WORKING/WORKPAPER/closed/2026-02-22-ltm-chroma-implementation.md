# Workpaper: 2026-02-22 — LTM ChromaDB — Umsetzung & Bestand

- **Date:** 2026-02-22
- **Agent:** GitHub Copilot / Claude Sonnet 4.6
- **Topic:** ChromaDB als LTM-Backend einrichten — Bestand, Ingest, Query, Disziplin
- **Status:** ✅ COMPLETED

---

## Session Scope

ChromaDB war als LTM-Standard ab Session 1 beschlossen (Eintrag 022). Diese Session setzt es um:
- `WORKING/TOOLS/ltm_chroma.py` anlegen — Ingest, Query, List, Bulk-Ingest
- Bestehende Dokumente einspielen (Audit-Log + Workpapers + SPEC + READMEs)
- `WORKING/AGENT-MEMORY/` von geplant → aktiv
- Vollständiger Repo-Bestand als Checkpoint dokumentiert

**Kontext aus vorherigen Sessions:**
- Dual-Layer-LTM beschlossen (Entry 022): `ltm-index.md` = Audit-Log, `WORKING/AGENT-MEMORY/` = ChromaDB
- `WORKING/AGENT-MEMORY/` in `.gitignore` — korrekt
- `WORKING/TOOLS/` existiert als Ordner (leer) — korrekt
- LTM-Index: 24 Einträge

---

## Repo-Bestand (Stand 2026-02-22 — Snapshot bei Session-Start)

### Tracked Files (git ls-files)

| Pfad | Typ | Status |
|------|-----|--------|
| `.agent.json` | Bootstrap-Manifest | ✅ Aktuell |
| `.github/copilot-instructions.md` | Tool-Bridge | ✅ Aktuell |
| `.gitignore` | Ignore-Regeln | ✅ Aktuell |
| `AGENT_SCHEMA.json` | JSON Schema | ✅ Aktuell |
| `AGENT.json` | Referenz-Manifest | ✅ Aktuell |
| `AGENTS.md` | Tool-Bridge (alle Agenten) | ✅ Aktuell |
| `READ-AGENT.md` | Agent-Einstiegspunkt | ✅ Aktuell |
| `README-DE.md` | Public README (Deutsch) | ✅ v2 nach Review |
| `README.md` | Public README (Englisch) | ✅ v2 nach Review |
| `SPEC-DE.md` | Vollspezifikation (Deutsch) | ✅ 809 Zeilen, vollständig |
| `SPEC.md` | Vollspezifikation (Englisch) | ✅ 830 Zeilen |
| `archive/ERKLÄRUNG.md` | Archiv | ✅ Archiviert |
| `archive/README-CH.md` | Archiv | ✅ Archiviert |
| `templates/read-agent-template.md` | Template | ✅ Aktuell |
| `templates/whitepaper-index-template.md` | Template | ✅ Aktuell |
| `templates/workpaper-template-quick.md` | Template | ✅ Aktuell |
| `templates/workpaper-template.md` | Template | ✅ Aktuell |
| `WORKING/MEMORY/ltm-index.md` | LTM Audit-Log | ✅ 24 Einträge |
| `WORKING/WHITEPAPER/INDEX.md` | Whitepaper-Index | ✅ 1 Whitepaper |
| `WORKING/WHITEPAPER/WP-001-aams-overview.md` | Whitepaper | ✅ Aktuell |
| `WORKING/WORKPAPER/closed/2026-02-22-bootstrap-session.md` | Closed WP | ✅ |
| `WORKING/WORKPAPER/closed/2026-02-22-hartes-review-v1.md` | Closed WP | ✅ |
| `WORKING/WORKPAPER/closed/2026-02-22-repo-analyse.md` | Closed WP | ✅ |

### Nicht verfolgte Ordner (leer, gitignored)

| Pfad | Gitignore-Status |
|------|-----------------|
| `WORKING/AGENT-MEMORY/` | ✅ Ignored (wird durch ChromaDB befüllt) |
| `WORKING/GUIDELINES/` | Leer (noch keine Guidelines-Files) |
| `WORKING/LOGS/` | ✅ Ignored |
| `WORKING/TOOLS/` | Leer → wird diese Session gefüllt |
| `docs/` | Existiert nicht → wird Session GitHub-Pages angelegt |

### Git-Commit-Historie (relevant)

| Commit | Beschreibung |
|--------|-------------|
| `6242c4f` (HEAD, main) | Session complete — SPEC-DE gap fill, hartes-review close, dual-layer LTM |
| `c4b610e` | Gitignore-Strategie |
| `4201677` (origin/main) | AAMS v1.0 — initial push |

---

## Ziel dieser Session

```
VORHER:  WORKING/TOOLS/          (leer)
         WORKING/AGENT-MEMORY/   (geplant, nicht aktiv)

NACHHER: WORKING/TOOLS/ltm_chroma.py  (ingest / query / list / bulk-ingest)
         WORKING/AGENT-MEMORY/        (ChromaDB aktiv, Dokumente eingespielt)
```

---

## Session Overview

### ChromaDB-Design

**Collection:** `aams-ltm`  
**Persistence:** `./WORKING/AGENT-MEMORY/` (relativ zum Repo-Root)  
**Backend:** ChromaDB (lokal, kein API-Key, kein Cloud-Vendor)  
**Embedding:** ChromaDB-Default (`all-MiniLM-L6-v2`) — offline, keine externe Abhängigkeit  
**Anforderungen:** `pip install chromadb` (einmalig)

### Funktionen des Scripts

| Funktion | Beschreibung |
|----------|-------------|
| `ingest(path, doc_type)` | Einzelne Datei in ChromaDB aufnehmen |
| `query(text, n)` | Semantische Suche, gibt n Treffer zurück |
| `list_all()` | Alle ingestierten Dokumente auflisten |
| `bulk_ingest()` | Alle AAMS-Kerndokumente auf einmal einspielen |
| `status()` | Collection-Größe und Pfad anzeigen |

### Initiales Bulk-Ingest (alle Kerndokumente)

Folgende Dateien werden beim ersten `bulk_ingest()` eingespielt:

| Datei | Typ |
|-------|-----|
| `SPEC.md` | spec |
| `SPEC-DE.md` | spec |
| `README.md` | readme |
| `README-DE.md` | readme |
| `AGENT.json` | manifest |
| `READ-AGENT.md` | entry_point |
| `WORKING/MEMORY/ltm-index.md` | ltm_audit |
| `WORKING/WHITEPAPER/WP-001-aams-overview.md` | whitepaper |
| `WORKING/WORKPAPER/closed/2026-02-22-bootstrap-session.md` | workpaper |
| `WORKING/WORKPAPER/closed/2026-02-22-repo-analyse.md` | workpaper |
| `WORKING/WORKPAPER/closed/2026-02-22-hartes-review-v1.md` | workpaper |

---

## Ergebnisse

- [x] `WORKING/TOOLS/ltm_chroma.py` erstellt (306 → 363 Zeilen nach Bug-Fixes)
- [x] ChromaDB per `pip install` verfügbar (`.venv`)
- [x] Bug gefixt: Endlosschleife in `chunk_by_size` (fehlende `break` bei `end >= len(text)`)
- [x] Embedding-Strategie: Hash-128 (pure Python, kein ML, kein Download, kein GPU)
- [x] Bulk-Ingest: 11 Dateien, 114 Chunks erfolgreich eingespielt
- [x] Query-Test erfolgreich (`dual-layer LTM ChromaDB Architektur` → korrekte Treffer)
- [x] Status-Ausgabe zeigt `Hash-128 (kein ML, kein Download)`

## File Protocol

| Action | Datei | Notiz |
|--------|-------|-------|
| CREATED | `WORKING/WORKPAPER/2026-02-22-ltm-chroma-implementation.md` | Diese Datei |
| CREATED | `WORKING/TOOLS/ltm_chroma.py` | ChromaDB Ingest/Query Tool — Hash-128 Embedding |
| CREATED | `WORKING/AGENT-MEMORY/` | ChromaDB Datenbank (gitignored) — 114 Chunks aktiv |

## Entscheidungen & Rationale

| Entscheidung | Rationale |
|---|---|
| Hash-128 statt all-MiniLM-L6-v2 | ML-Modell verursachte CPU-Vollauslastung + Lüfterturbine. Hash-Embedding: kein Download, kein GPU, sofort fertig. Für AAMS-Dokumenten-Retrieval ausreichend. |
| ChromaDB-Default-Embedding | abgelehnt — löste automatischen Modell-Download aus |
| Embeddings via `upsert(embeddings=...)` | Umgeht ChromaDB's `EmbeddingFunction`-API — keine Versions-Kompatibilitätsprobleme |
| Pfad relativ zu Repo-Root | Script wird immer aus dem Repo-Root aufgerufen |
| `reset`-Befehl | Nötig wenn Embedding-Dimensionen sich ändern (z.B. bei späterem Wechsel zu ML-Embeddings) |
| Bulk-Ingest als CLI-Befehl | Agent wie Mensch kann mit `python ltm_chroma.py bulk-ingest` starten |
| Collection-Name `aams-ltm` | Eindeutig, kein Konflikt mit anderen Projekten |
| Chunking: 2000 Zeichen + H2-Split | H2-Split bevorzugt (semantische Grenzen), Size als Fallback |

## Next Steps

- [x] `WORKING/TOOLS/ltm_chroma.py` implementieren
- [x] `pip install chromadb` ausführen und Verfügbarkeit prüfen
- [x] Bulk-Ingest ausführen
- [ ] `ltm-index.md` Backend-Status aktualisieren: `⬜ → ✅`
- [ ] LTM-Eintrag 025 anlegen
- [ ] Workpaper nach `closed/` verschieben

## Session Closing Checklist

- [x] Scope klar definiert
- [x] Repo-Bestand vollständig dokumentiert
- [x] Offene Entscheidungsfragen identifiziert und gelöst
- [x] Keine Secrets in diesem Workpaper
- [x] `WORKING/TOOLS/ltm_chroma.py` erstellt und getestet
- [x] File Protocol vollständig
- [ ] LTM-Update (Eintrag 025)
- [ ] Workpaper nach `closed/` verschieben
