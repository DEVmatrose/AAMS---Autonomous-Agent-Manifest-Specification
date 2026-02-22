#!/usr/bin/env python3
"""
AAMS LTM — ChromaDB Tool
Usage (from repo root):
    python WORKING/TOOLS/ltm_chroma.py status
    python WORKING/TOOLS/ltm_chroma.py bulk-ingest
    python WORKING/TOOLS/ltm_chroma.py ingest <file> [--type <doc_type>]
    python WORKING/TOOLS/ltm_chroma.py query "<text>" [--n <results>]
    python WORKING/TOOLS/ltm_chroma.py list
    python WORKING/TOOLS/ltm_chroma.py delete <file>

AAMS/1.0 — WORKING/AGENT-MEMORY/ (ChromaDB, gitignored)
"""

import sys
import os
import argparse
import hashlib
import math
from datetime import datetime, timezone
from pathlib import Path

# ── Pfade (relativ zum Repo-Root, nicht zum Script-Ordner) ─────────────────────
SCRIPT_DIR   = Path(__file__).resolve().parent
REPO_ROOT    = SCRIPT_DIR.parent.parent          # WORKING/TOOLS/ → repo root
CHROMA_PATH  = REPO_ROOT / "WORKING" / "AGENT-MEMORY"
COLLECTION   = "aams-ltm"

# ── Dokumente für bulk-ingest ──────────────────────────────────────────────────
BULK_DOCS = [
    ("SPEC.md",                                                    "spec"),
    ("SPEC-DE.md",                                                 "spec"),
    ("README.md",                                                  "readme"),
    ("README-DE.md",                                               "readme"),
    ("AGENT.json",                                                 "manifest"),
    ("READ-AGENT.md",                                              "entry_point"),
    ("WORKING/MEMORY/ltm-index.md",                                "ltm_audit"),
    ("WORKING/WHITEPAPER/WP-001-aams-overview.md",                 "whitepaper"),
    ("WORKING/WORKPAPER/closed/2026-02-22-bootstrap-session.md",   "workpaper"),
    ("WORKING/WORKPAPER/closed/2026-02-22-repo-analyse.md",        "workpaper"),
    ("WORKING/WORKPAPER/closed/2026-02-22-hartes-review-v1.md",    "workpaper"),
]

CHUNK_SIZE    = 2000   # Zeichen pro Chunk wenn kein H2-Split möglich
CHUNK_OVERLAP = 200    # Überlappung zwischen Chunks

EMBED_DIM = 128  # Dimensionen des Hash-Embeddings


# ── Leichtgewichtige Embedding-Funktion (kein ML, kein Download) ───────────────

class HashEmbeddingFunction:
    """
    Pure-Python TF-ähnliche Hash-Embedding.
    Keine externe Abhängigkeit, kein Modell-Download, kein GPU.
    Reicht für Keyword-Retrieval über AAMS-Dokumentation.
    """
    name = "hash-embedding-128"

    def __call__(self, input: list[str]) -> list[list[float]]:
        return [self._embed(text) for text in input]

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [self._embed(text) for text in texts]

    def _embed(self, text: str) -> list[float]:
        words = text.lower().split()
        vec = [0.0] * EMBED_DIM
        for w in words:
            # Zwei unabhängige Hash-Funktionen für bessere Verteilung
            h1 = int(hashlib.md5(w.encode()).hexdigest(), 16) % EMBED_DIM
            h2 = int(hashlib.sha1(w.encode()).hexdigest(), 16) % EMBED_DIM
            vec[h1] += 1.0
            vec[h2] += 0.5
        # L2-Normalisierung → Kosinus-Ähnlichkeit funktioniert korrekt
        norm = math.sqrt(sum(x * x for x in vec)) or 1.0
        return [x / norm for x in vec]


_EMBED_FN = HashEmbeddingFunction()


# ── Hilfsfunktionen ────────────────────────────────────────────────────────────

def get_collection():
    """Gibt ChromaDB-Collection zurück (persistent, auto-create)."""
    import chromadb
    CHROMA_PATH.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    try:
        return client.get_or_create_collection(
            name=COLLECTION,
            metadata={"hnsw:space": "cosine", "embedding": "hash-128"}
        )
    except Exception as e:
        print(f"\n❌ ChromaDB Fehler: {e}")
        print("   → Falls Embedding-Konflikt: python WORKING/TOOLS/ltm_chroma.py reset")
        sys.exit(1)


def chunk_by_h2(text: str) -> list[tuple[str, str]]:
    """
    Teilt einen Text an H2-Überschriften (## ).
    Gibt Liste von (section_title, content) zurück.
    """
    lines = text.splitlines(keepends=True)
    sections = []
    current_title = "_intro"
    current_lines = []

    for line in lines:
        if line.startswith("## "):
            if current_lines:
                sections.append((current_title, "".join(current_lines).strip()))
            current_title = line.strip().lstrip("# ").strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections.append((current_title, "".join(current_lines).strip()))

    # Leere Sections filtern
    return [(t, c) for t, c in sections if c.strip()]


def chunk_by_size(text: str) -> list[tuple[str, str]]:
    """Fallback: teilt Text in feste Chunks mit Überlappung."""
    chunks = []
    start = 0
    idx = 0
    while start < len(text):
        end = min(start + CHUNK_SIZE, len(text))
        chunks.append((f"chunk_{idx}", text[start:end]))
        if end >= len(text):
            break  # Ende erreicht — verhindert Endlosschleife bei kleinem Rest
        start = end - CHUNK_OVERLAP
        idx += 1
    return chunks


def make_id(file_rel: str, section: str) -> str:
    """Stabile, eindeutige ID für ein Dokument-Chunk."""
    raw = f"{file_rel}::{section}"
    return hashlib.sha1(raw.encode()).hexdigest()[:16]


def ingest_file(col, file_path: Path, doc_type: str = "document") -> int:
    """
    Ingested eine Datei in die ChromaDB-Collection.
    Gibt Anzahl der eingespielten Chunks zurück.
    Nutzt upsert → idempotent.
    """
    if not file_path.exists():
        print(f"  ⚠ Datei nicht gefunden: {file_path}")
        return 0

    text = file_path.read_text(encoding="utf-8", errors="replace")
    file_rel = str(file_path.relative_to(REPO_ROOT)).replace("\\", "/")

    # Chunking-Strategie: erst H2-Split, dann Größen-Split
    sections = chunk_by_h2(text)
    if len(sections) <= 1:
        sections = chunk_by_size(text)

    ids, docs, metas, embeddings = [], [], [], []
    now = datetime.now(timezone.utc).isoformat()

    for i, (title, content) in enumerate(sections):
        chunk_id = make_id(file_rel, f"{i}:{title}")
        ids.append(chunk_id)
        docs.append(content)
        embeddings.append(_EMBED_FN._embed(content))
        metas.append({
            "file":        file_rel,
            "doc_type":    doc_type,
            "section":     title,
            "chunk_index": i,
            "ingested_at": now,
        })

    col.upsert(ids=ids, documents=docs, embeddings=embeddings, metadatas=metas)
    return len(ids)


# ── CLI-Befehle ────────────────────────────────────────────────────────────────

def cmd_status(args):
    col = get_collection()
    count = col.count()
    print(f"\n📦 AAMS LTM — ChromaDB Status")
    print(f"   Collection : {COLLECTION}")
    print(f"   Pfad       : {CHROMA_PATH}")
    print(f"   Embedding  : Hash-128 (kein ML, kein Download)")
    print(f"   Dokumente  : {count} Chunks ingested")


def cmd_bulk_ingest(args):
    col = get_collection()
    total = 0
    print(f"\n🔄 Bulk-Ingest — {len(BULK_DOCS)} Dateien …\n")
    for rel_path, doc_type in BULK_DOCS:
        fp = REPO_ROOT / rel_path
        n = ingest_file(col, fp, doc_type)
        status = f"✅ {n} Chunks" if n > 0 else "⚠ übersprungen"
        print(f"  {status:20} {rel_path}")
        total += n
    print(f"\n✅ Bulk-Ingest abgeschlossen — {total} Chunks total")


def cmd_ingest(args):
    col = get_collection()
    fp = REPO_ROOT / args.file
    doc_type = args.type or _guess_type(args.file)
    n = ingest_file(col, fp, doc_type)
    if n > 0:
        print(f"\n✅ {args.file} ingested ({n} Chunks, Typ: {doc_type})")
    else:
        print(f"\n⚠ Ingest fehlgeschlagen: {args.file}")


def cmd_query(args):
    col = get_collection()
    n = args.n or 5
    query_embedding = _EMBED_FN._embed(args.text)
    results = col.query(
        query_embeddings=[query_embedding],
        n_results=n,
        include=["documents", "metadatas", "distances"]
    )
    docs      = results["documents"][0]
    metas     = results["metadatas"][0]
    distances = results["distances"][0]

    print(f"\n🔍 Query: \"{args.text}\" — Top {n} Ergebnisse\n")
    print("─" * 72)
    for i, (doc, meta, dist) in enumerate(zip(docs, metas, distances)):
        score = round(1 - dist, 3)
        print(f"[{i+1}] {meta['file']}  §{meta['section']}  (Score: {score})")
        print(f"     Typ: {meta['doc_type']}  |  Chunk: {meta['chunk_index']}")
        print()
        # Vorschau: erste 300 Zeichen
        preview = doc[:300].replace("\n", " ")
        print(f"  {preview}…")
        print("─" * 72)


def cmd_list(args):
    col = get_collection()
    count = col.count()
    if count == 0:
        print("\nℹ️  Keine Dokumente ingested.")
        return

    # Alle Metadaten abrufen (max 10000)
    results = col.get(include=["metadatas"], limit=10000)
    metas = results["metadatas"]

    # Nach Datei gruppieren
    files: dict[str, list] = {}
    for m in metas:
        f = m["file"]
        files.setdefault(f, []).append(m)

    print(f"\n📋 AAMS LTM — {count} Chunks in {len(files)} Dateien\n")
    for filepath, chunks in sorted(files.items()):
        print(f"  {filepath:60} ({len(chunks)} Chunks, Typ: {chunks[0]['doc_type']})")


def cmd_delete(args):
    col = get_collection()
    file_rel = args.file.replace("\\", "/")

    # Alle Chunks dieser Datei finden
    results = col.get(
        where={"file": file_rel},
        include=["metadatas"]
    )
    ids = results["ids"]
    if not ids:
        print(f"\n⚠ Keine Chunks gefunden für: {file_rel}")
        return

    col.delete(ids=ids)
    print(f"\n✅ {len(ids)} Chunks gelöscht für: {file_rel}")


def cmd_reset(args):
    """Löscht die gesamte Collection und AGENT-MEMORY (bei Embedding-Wechsel nötig)."""
    import shutil
    if CHROMA_PATH.exists():
        shutil.rmtree(CHROMA_PATH)
        print(f"\n✅ AGENT-MEMORY gelöscht: {CHROMA_PATH}")
    else:
        print(f"\nℹ️  Nichts zu löschen — {CHROMA_PATH} existiert nicht")
    print("   Jetzt 'bulk-ingest' ausführen um neu aufzubauen.")


# ── Hilfsfunktionen ────────────────────────────────────────────────────────────

def _guess_type(path: str) -> str:
    p = path.lower()
    if "workpaper" in p: return "workpaper"
    if "whitepaper" in p: return "whitepaper"
    if "memory/ltm" in p: return "ltm_audit"
    if "read-agent" in p: return "entry_point"
    if "spec" in p: return "spec"
    if "readme" in p: return "readme"
    if "agent.json" in p: return "manifest"
    return "document"


# ── Entry Point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="AAMS LTM — ChromaDB Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("status",       help="Collection-Status anzeigen")
    sub.add_parser("bulk-ingest",  help="Alle AAMS-Kerndokumente einspielen")
    sub.add_parser("list",         help="Alle ingestierten Dokumente auflisten")
    sub.add_parser("reset",        help="Collection + AGENT-MEMORY löschen (bei Embedding-Wechsel)")

    p_ingest = sub.add_parser("ingest", help="Einzelne Datei ingestieren")
    p_ingest.add_argument("file",             help="Pfad relativ zum Repo-Root")
    p_ingest.add_argument("--type", dest="type", default=None,
                           help="Dokumenttyp (z.B. workpaper, spec, readme)")

    p_query = sub.add_parser("query", help="Semantische Suche")
    p_query.add_argument("text",         help="Suchtext")
    p_query.add_argument("--n", type=int, default=5, help="Anzahl Ergebnisse (default: 5)")

    p_del = sub.add_parser("delete", help="Datei aus LTM entfernen")
    p_del.add_argument("file", help="Pfad relativ zum Repo-Root")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    dispatch = {
        "status":      cmd_status,
        "bulk-ingest": cmd_bulk_ingest,
        "ingest":      cmd_ingest,
        "query":       cmd_query,
        "list":        cmd_list,
        "delete":      cmd_delete,
        "reset":       cmd_reset,
    }

    fn = dispatch.get(args.cmd)
    if fn:
        fn(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
