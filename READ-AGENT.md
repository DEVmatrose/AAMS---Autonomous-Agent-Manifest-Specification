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
3. Scan entire repository → write inventory + analysis to first workpaper
4. Create `READ-AGENT.md` if missing
5. Index existing documentation into `WORKING/MEMORY/`

---

### On every session start
1. Read this file
2. Check last workpaper in `WORKING/WORKPAPER/` — what was the last state?
3. Query `WORKING/MEMORY/` for the session topic
4. Open or create workpaper for this session

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

### LTM Commands — mandatory Python paths

> ⚠️ **NICHT `wsl python3`, `python`, oder System-Python verwenden.**  
> Nur das `.venv` im Workspace-Root enthält `chromadb` und `sentence-transformers`.

**Query (Sessionstart — vor jedem neuen Workpaper):**
```powershell
# Windows PowerShell — immer so:
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\query.py "<Session-Thema>"
```

**Ingest (Sessionende — nach Workpaper-Abschluss):**
```powershell
.venv\Scripts\python.exe WORKING\AGENT-MEMORY\ingest.py
```

**Warum:** Jeder andere Interpreter (WSL `python3`, System-Python, Conda) hat `chromadb` nicht installiert und darf nicht verwendet werden. Kein `pip install` in fremde Environments.

---

## Key Files

| File | Role |
|---|---|
| `.agent.json` | Minimal bootstrap contract (portable, drop into any repo) |
| `AGENT.json` | Full agent manifest with runtime, permissions, skills |
| `AGENT_SCHEMA.json` | JSON Schema for validating AGENT.json |
| `SPEC.md` | Full specification (English) |
| `SPEC-DE.md` | Full specification (German) |

---

## Current Status

- Bootstrap: **complete** (2026-02-22)
- Spec version: AAMS/1.0
- Workspace: initialized, all folders present
- LTM: 28 entries → `WORKING/MEMORY/ltm-index.md` (Audit-Log) + `WORKING/AGENT-MEMORY/` (ChromaDB ✅ aktiv, 114 Chunks)
- Whitepapers: 1 → `WORKING/WHITEPAPER/INDEX.md`
- Open workpapers: 1 → `2026-02-22-feldtest-independentes-repo.md` (pending: external repo test)
- READMEs: DE ✅ · EN ✅ (CH archived) — review fixes applied ✅
- LTM architecture: dual-layer (audit-log + vector store) ✅
- SPEC path bugs: fixed ✅ · Skills: `bootstrap_workspace` ✅
- GitHub Issues #1–3: addressed, ready to close on GitHub
