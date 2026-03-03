# READ-AGENT.md — {project}

> **Purpose:** This is the entry point for AI agents working in this repository.  
> Read this file first. It gives you project context in 30 seconds.  
> **Template:** AAMS Read-Agent v1.0

---

## Project Overview

<!-- One paragraph: What is this project? What does it do? Who is it for? -->

**Name:** {project}  
**Type:** {type} <!-- e.g. web-application, CLI tool, library, API service -->  
**Stack:** {stack} <!-- e.g. Node.js + TypeScript, Python + FastAPI, etc. -->  
**Status:** {status} <!-- e.g. Active development, Maintenance, Pre-release -->

---

## Architecture

<!-- High-level architecture. Keep it short — max 10 lines. Link to whitepapers for details. -->

```
<!-- ASCII diagram or short description of the main components -->
```

**Key components:**
- **Component A** — what it does, where it lives
- **Component B** — what it does, where it lives
- **Component C** — what it does, where it lives

---

## Getting Started

```bash
# Install dependencies
# ...

# Start the project
# ...

# Run tests
# ...
```

---

## Repository Structure

```
project-root/
├── src/                  ← main source code
├── tests/                ← test suite
├── docs/                 ← human documentation
├── WORKING/              ← agent workspace (see AGENT.json)
│   ├── WHITEPAPER/       ← stable architecture docs
│   ├── WORKPAPER/        ← active sessions
│   │   └── closed/       ← archived sessions
│   ├── MEMORY/           ← LTM context store
│   ├── GUIDELINES/       ← coding standards
│   ├── LOGS/             ← agent audit trail
│   └── TOOLS/            ← project-specific scripts
├── .agent.json           ← minimal bootstrap contract
├── AGENT.json            ← full agent manifest
└── README.md             ← human readme
```

---

## Current Priorities

<!-- What should the agent focus on? What is the most important work right now? -->

1. ...
2. ...
3. ...

---

## Key Decisions

<!-- Important architectural or design decisions the agent must know about. Link to whitepapers. -->

| Decision | Rationale | Whitepaper |
|----------|-----------|------------|
| | | |

---

## Conventions

<!-- Short list of the most important rules. Full details in WORKING/GUIDELINES/. -->

- **Branching:** ...
- **Naming:** ...
- **Testing:** ...
- **Commit messages:** ...

---

## Agent Contract

> **Any instruction referencing READ-AGENT.md means: execute this contract. Start immediately.**

**On first entry:**
1. Read this file fully
2. Check `WORKING/` structure → create if missing (idempotent)
3. Scan repository → write inventory + analysis to first workpaper
4. Index existing documentation into `WORKING/MEMORY/`

**On every session start:**
1. Read this file
2. Check last workpaper in `WORKING/WORKPAPER/` — what was the last state?
3. Query `WORKING/MEMORY/` for the session topic
4. Open or create workpaper for this session

**On every session end:**
1. Complete workpaper (file protocol + decisions + next steps)
2. Ingest workpaper into `WORKING/MEMORY/`
3. Move workpaper to `WORKING/WORKPAPER/closed/`
4. Update this file if architecture or structure changed

**Mandatory LTM triggers:**

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

## Reading List

<!-- Which documents should the agent read to understand the project? In order of priority. -->

1. This file (READ-AGENT.md)
2. `AGENT.json` — workspace rules, permissions, session hygiene
3. `WORKING/GUIDELINES/` — coding standards
4. `WORKING/WHITEPAPER/INDEX.md` — architecture whitepapers
5. ...

---

## Known Issues / Tech Debt

<!-- Things the agent should be aware of but that are not the current focus. -->

- ...
- ...

---

> **Last updated:** {date}  
> **Updated by:** {agent or human}
