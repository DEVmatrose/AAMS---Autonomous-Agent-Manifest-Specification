# AAMS Bootstrap Prompt

> The missing handoff: the one sentence that turns a repo with `.agent.json` into a running AAMS workspace.

---

## Minimal Bootstrap (Works with all tools)

```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

Paste this into any agent that reads `.agent.json` or `AGENTS.md`:
Cursor, Claude Code, GitHub Copilot, Aider, Continue.dev, Codex, Windsurf.

---

## Two-Step Onboarding (Complete Flow)

**Step 1 — Drop `.agent.json` into your repo:**

```bash
curl -sO https://raw.githubusercontent.com/DEVmatrose/AAMS/main/.agent.json
```

**Step 2 — Tell your agent:**

```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

That's it. The agent creates the `WORKING/` structure, scans the repo, writes the first workpaper, and indexes into LTM.

---

## Tool-Specific Variants

### Claude Code / Claude Desktop
```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

### GitHub Copilot (Chat)
```
Read .agent.json and AGENTS.md, then execute the agent_contract defined in READ-AGENT.md. Start with on_first_entry. No confirmation needed.
```

### Cursor
```
Read .agent.json and execute the agent_contract.on_first_entry as documented in READ-AGENT.md. Start immediately.
```

### Aider / Continue.dev
```
Read .agent.json and execute the full agent_contract.on_first_entry. Start immediately. No confirmation needed.
```

---

## What the Agent Does After This Prompt

1. Reads `READ-AGENT.md` — full project context
2. Creates `WORKING/` folder structure (idempotent — safe to repeat)
3. Scans the repository
4. Creates `READ-AGENT.md` if missing
5. Derives coding guidelines
6. Indexes documentation into LTM (`WORKING/AGENT-MEMORY/`)
7. Creates first workpaper with scan results

**Idempotent:** Running bootstrap on an existing AAMS workspace is safe. Existing files are not overwritten.

---

## Session Start Prompt (Subsequent Sessions)

For sessions after the initial bootstrap:

```
Read READ-AGENT.md and execute agent_contract.on_session_start. Query LTM for context, then open or create a workpaper for this session.
```

---

*AAMS/1.0 — prompts/bootstrap.md*
