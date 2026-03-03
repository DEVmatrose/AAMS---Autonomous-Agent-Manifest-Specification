# READ-AGENT

> **You are reading this because you entered this repository.**  
> Do not skip. Do not summarize. Read fully. Then execute.

**You are an AI agent. Your next action is determined by which state applies:**

| State | Action |
|---|---|
| **First entry — `WORKING/` does not exist or is empty** | Execute `on_first_entry` below |
| **New session — `WORKING/` exists, workpapers present** | Execute `on_session_start` below |

Start immediately. No confirmation needed.

---

## What this project is

**Autonomous Agent Manifest Specification (AAMS)**  
A portable workspace and documentation standard for AI agents working in any repository.

Core idea:  
> Drop `.agent.json` into any repo. Every agent that reads it creates and follows the same workspace structure — independent of framework, language, or runtime.

---

## Workspace Structure

| Folder | Purpose |
|---|---|
| `WORKING/WHITEPAPER/` | Stable architecture and system truth. Not for daily work. See [INDEX.md](WORKING/WHITEPAPER/INDEX.md). |
| `WORKING/WORKPAPER/` | Session- and task-scoped working documents. One per session. |
| `WORKING/WORKPAPER/closed/` | Finished workpapers after session close. |
| `WORKING/MEMORY/` | Long-term context store. Cross-session knowledge. |
| `WORKING/LOGS/` | Agent action logs and audit trail. |
| `WORKING/GUIDELINES/` | Coding standards and architecture rules derived from this project. |
| `WORKING/TOOLS/` | Agent-specific helper tools and scripts. |

---

## Documentation Model

**Three layers — mandatory:**

1. **Workpaper** — What am I doing right now in this session?
   - Created at session start, closed at session end.
   - File protocol (created/modified/moved/deleted) is mandatory.
   - Naming: `{date}-{agent}-{topic}.md`

2. **Whitepaper** — What does this system look like?
   - Stable. Written once. Updated only on architecture decisions.
   - Never moved, never deleted.

3. **Memory** — What did we learn across sessions?
   - Ingest every closed workpaper.
   - Query at every session start.

---

## Agent Contract

> **Any instruction referencing READ-AGENT.md means: execute this contract. Start immediately. No confirmation needed.**

---

### On first entry (Onboarding)
1. Read this file fully
2. Check: does `WORKING/` structure exist? → if not: create all folders
3. Scan entire repository → write first workpaper  
   Minimum sections: **session goal · repository inventory** (file tree + status) **· key findings** (from README/docs) **· open questions · file protocol · next steps**
4. Create `READ-AGENT.md` if missing
5. Index existing documentation into `WORKING/MEMORY/`

---

### On every session start
1. Read this file
2. Check last workpaper in `WORKING/WORKPAPER/` — what was the last state?
3. Query `WORKING/MEMORY/` for the session topic
4. Open or create workpaper for this session

---

### State Recovery (when agent state is uncertain)

> **File system and git log are ground truth — never rely solely on in-memory task tracking.**  
> If task state is unclear: re-read the current workpaper’s **File Protocol** section. What exists on disk and in `git log` is what was actually done. Treat in-memory todo state as advisory only.

---

### On every session end
1. Complete workpaper (file protocol + decisions + next steps)
2. Ingest workpaper into `WORKING/MEMORY/`
3. Move workpaper to `WORKING/WORKPAPER/closed/`
4. Update this file if architecture or structure changed

---

### Mandatory LTM triggers — document in these situations:

| Trigger | Action |
|---|---|
| Context limit reached | Ingest current state → query in new session |
| Before new workpaper | Query LTM for topic context first |
| Before new whitepaper | Query LTM for existing architecture notes |
| Folder or file structure changed | Re-ingest affected documentation |
| Workpaper updated | Log change in workpaper file protocol |
| Workpaper closed | Ingest → move to `closed/` |
| Whitepaper updated | Re-ingest whitepaper into LTM |

---

### LTM Commands — two tracks

#### Track A — Markdown-only (default, zero dependencies)

No Python, no ChromaDB needed. Works on any fresh repo.

- **Query:** Read `WORKING/MEMORY/ltm-index.md` directly — scan for session topic
- **Ingest:** Append new entry to `WORKING/MEMORY/ltm-index.md` at session end

> Use Track A when: no Python environment exists, repo is freshly bootstrapped, or `ltm_mode: "markdown"` in `.agent.json`.

#### Track B — Vector store (ChromaDB, requires Python)

> ⚠️ **NICHT `wsl python3`, `python`, oder System-Python verwenden.**  
> Nur das `.venv` im Workspace-Root enthält `chromadb`.

**Query (Sessionstart):**
```powershell
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\query.py "<Session-Thema>"
```

**Ingest (Sessionende):**
```powershell
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\ingest.py
```

> Use Track B when: `.venv` with `chromadb` exists and `ltm_mode: "vector"` in `.agent.json`.

---

## Key Files

| File | Role |
|---|---|
| `.agent.json` | Minimal bootstrap contract (portable, drop into any repo) |
| `reference/AGENT.json` | Full agent manifest with runtime, permissions, skills |
| `reference/AGENT_SCHEMA.json` | JSON Schema for validating AGENT.json |
| `reference/SPEC.md` | Full specification (English) |
| `reference/SPEC-DE.md` | Full specification (German) |

---

## Current Status

- Bootstrap: **complete** (2026-02-22)
- Spec version: AAMS/1.0
- Workspace: initialized, all folders present (incl. `WORKING/DIARY/` — Temporal Context Layer)
- LTM: 58 entries → `WORKING/MEMORY/ltm-index.md` (Audit-Log) + `WORKING/AGENT-MEMORY/` (ChromaDB ✅ aktiv, 114 Chunks)
- Whitepapers: 2 → `WORKING/WHITEPAPER/INDEX.md` (WP-001 AAMS Overview, WP-002 Related Work)
- Open workpapers: 1 → `2026-02-22-feldtest-independentes-repo.md` (SUSPENDED: pending external repo test)
- READMEs: DE ✅ · EN ✅ (CH archived) — review fixes applied ✅
- LTM architecture: dual-layer (audit-log + vector store) ✅
- SPEC path bugs: fixed ✅ · Skills: `bootstrap_workspace` ✅
- GitHub Issues #1–6: addressed and closed
- Diary Layer: **active** — `WORKING/DIARY/2026-02.md` (four-layer documentation model)
