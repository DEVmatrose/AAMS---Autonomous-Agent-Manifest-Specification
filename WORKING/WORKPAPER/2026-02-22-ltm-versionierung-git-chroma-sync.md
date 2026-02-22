# 2026-02-22 — Copilot — LTM-Versionierung: internes Git + ChromaDB-Sync

**Project:** Autonomous Agent Manifest Specification  
**Module:** LTM-Architektur / WORKING/  
**Status:** 🚧 IN PROGRESS  
**Date:** 2026-02-22

---

## Kernfrage

> Macht es Sinn, neben ChromaDB **ein internes Git-Repository für `WORKING/`** zu betreiben, das mit ChromaDB synchronisiert ist?  
> Und falls ja: Ist das ein echter Mehrwert für Agenten — oder zusätzliche Komplexität ohne Gewinn?

---

## Ausgangslage

Aktuell haben wir ein Dual-Layer-LTM:

| Layer | Pfad | Was | Git |
|---|---|---|---|
| Audit-Log | `WORKING/MEMORY/ltm-index.md` | Menschenlesbar, append-only, 29 Einträge | ✅ im Haupt-Git |
| Vektorspeicher | `WORKING/AGENT-MEMORY/` | ChromaDB, 114 Chunks, semantisch querybar | ❌ `.gitignore` |

Das Haupt-Git versioniert alles in `WORKING/MEMORY/`, `WORKING/WHITEPAPER/`, `WORKING/WORKPAPER/`, Templates usw.  
ChromaDB läuft lokal, ist ephemer (kein Remote), kein History-Tracking.

---

## Die Idee: internes Git für WORKING/

Ein separates `.git`-Repo nur in `WORKING/` — mit eigener Commit-History, eigenem Branch-Modell, ggf. eigenem Remote.  
Synchronisationspunkt mit ChromaDB: nach jedem ChromaDB-Ingest wird ein Git-Commit gemacht (oder umgekehrt).

---

## Analyse: Pro

### 1. Zeitreise für LTM-State
Git kann zeigen **was der Agent vor 3 Wochen in ChromaDB hatte** — welche Chunks existierten, was noch nicht. Das ist heute nicht möglich: ChromaDB hat keine eingebaute History. Wenn ein Chunk überschrieben wird, ist der alte Zustand weg.

**Konkreter Nutzen:** Debugging. Wenn ein Agent falsche Entscheidungen auf Basis veralteten Kontexts getroffen hat — kann man den LTM-State zu dem Zeitpunkt rekonstruieren.

### 2. LTM-State als Deploy-Artefakt
Ein Git-Tag `ltm-v1.2` könnte den exakten ChromaDB-Ingeststand markieren. Team-übergreifend: jeder Clone kann exakt den gleichen LTM-Stand reproduzieren.

**Konkreter Nutzen:** Reproduzierbarkeit in Multi-Agent-Setups. Heute ist ChromaDB-State pro Machine unterschiedlich.

### 3. Rollback nach fehlerhaftem Ingest
Wenn ein Bulk-Ingest fehlerhafte oder vertrauliche Chunks erzeugt: `git revert` + `ltm_chroma.py reset` + re-ingest aus dem vorherigen Stand.

**Konkreter Nutzen:** Safety. Heute gibt es keinen Recovery-Pfad außer manuellem Reset.

### 4. Audit-Trail für ChromaDB-Operationen
Heute weiß der Audit-Log nur "was ingested wurde" — nicht "was gelöscht oder ersetzt wurde". Mit Git-Diff auf den exportierten ChromaDB-State wird der Unterschied sichtbar.

---

## Analyse: Contra

### 1. ChromaDB-Format ist nicht diff-freundlich
`WORKING/AGENT-MEMORY/` enthält SQLite + Binary-Blobs. Git-Diffs darauf sind unleserlich. Sinn macht das nur wenn **exportierte Text-Snapshots** committed werden (z.B. JSON-Dumps aller Chunks).

**Konsequenz:** Nicht ChromaDB-Files committen, sondern Export. Das ist ein zusätzlicher Build-Step.

### 2. Zwei Gits = zwei Sync-Punkte
Ein separates `WORKING/`-Git muss gepusht, rebased, gemerged werden — unabhängig vom Haupt-Git. Das ist nicht "ein Repo" mehr, das ist ein verschachteltes Submodule-Problem.

**Alternativer Gedanke:** Statt separatem Git → Branch im Haupt-Repo dediziert für LTM-Snapshots.

### 3. Synchronisation ist nicht trivial
Wann ist der ChromaDB-Stand "commit-würdig"? Nach jedem Ingest? Nach jeder Session? Wer triggert den Export? Wenn der Agent es vergisst, läuft Git-State und ChromaDB-State auseinander.

**Konsequenz:** Braucht ein definiertes Protokoll — sonst entsteht genau die Art von Chaos, die AAMS lösen soll.

### 4. Mehrwert für Agenten ist indirekt
Agenten fragen ChromaDB ab, nicht Git. Der Mehrwert des Gits liegt bei **Menschen** (Debugging, Audit, Reproduzierbarkeit) und bei **DevOps** (Deployment). Ein Agent selbst profitiert davon nur indirekt über bessere Recovery-Prozesse.

---

## Hybrider Ansatz: Git-Snapshots statt Git-Sync

Statt echtem Sync: **periodische Snapshot-Exports** der ChromaDB, committed ins Haupt-Git.

```
WORKING/
├── AGENT-MEMORY/           ← ChromaDB (gitignore, live)
└── MEMORY/
    ├── ltm-index.md        ← Audit-Log (immer im Git)
    └── snapshots/          ← JSON-Exports, commit nach Session
        ├── 2026-02-22-after-bulk-ingest.json
        └── ...
```

**Vorgehen:** Nach jedem Bulk-Ingest exportiert `ltm_chroma.py snapshot` alle Chunks als `.json` → committed. Roll-forward/backward mit `ltm_chroma.py restore <snapshot>`.

**Aufwand:** `snapshot`-Command in `ltm_chroma.py` + `restore`-Command. ~50 Zeilen Python.

---

## Empfehlung (Hypothese)

| Option | Empfehlung |
|---|---|
| Separates Git-Repo für `WORKING/` | ❌ Zu viel Overhead. Submodule-Komplexität. |
| Git-Sync mit rohen ChromaDB-Files | ❌ Binary-Diffs. Nicht verwendbar. |
| **Snapshot-Export nach Session, committet ins Haupt-Git** | ✅ Pragmatisch. Reproduzierbar. Rollback möglich. |
| Dedizierter LTM-Branch im Haupt-Repo | ⚠️ Möglich, aber erhöht Branch-Modell-Komplexität. |

**Kernaussage:** Kein separates Git. Aber ein **`ltm_chroma.py snapshot`-Command** der nach jeder Session einen JSON-Dump committet — das ist der Mehrwert ohne die Komplexität.

---

## Offene Fragen

- [ ] Wie groß werden Snapshot-JSONs? (114 Chunks × ~500 Zeichen = ~57KB — vertretbar)
- [ ] Soll der Snapshot automatisch beim `closing_checklist`-Step erzwungen werden?
- [ ] Macht es Sinn, Snapshots in `WORKING/MEMORY/snapshots/` oder in `WORKING/AGENT-MEMORY/snapshots/` zu legen? (Letzteres würde gitignored bleiben — widerspricht dem Ziel)
- [ ] Kann `ltm_chroma.py restore` aus einem Snapshot deterministisch denselben Vektorspeicher aufbauen? (Ja, da Hash-Embedding deterministisch ist — kein ML, kein Zufall)

---

## File Protocol

| Action | File | Details |
|--------|------|---------|
| ✏️ Modified | `WORKING/MEMORY/ltm-index.md` | Eintrag #29 (Repo-Umbenennung + URL-Update) |
| ✅ Created | `WORKING/WORKPAPER/2026-02-22-ltm-versionierung-git-chroma-sync.md` | Dieses Workpaper |

## Next Steps

- [ ] `ltm_chroma.py snapshot` Command implementieren (JSON-Export aller Chunks)
- [ ] `ltm_chroma.py restore <file>` Command implementieren
- [ ] Entscheidung: automatischer Snapshot als Teil des Session-Closing?
- [ ] Workpaper schließen + LTM ingestieren

---

**Status:** 🚧 IN PROGRESS
