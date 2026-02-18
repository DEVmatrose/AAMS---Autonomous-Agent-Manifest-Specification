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
├── src/              ← main source code
├── tests/            ← test suite
├── docs/             ← human documentation
├── WORKING/          ← agent workspace (see AGENT.json)
│   ├── docs/         ← whitepapers
│   ├── WORKPAPER/    ← active sessions
│   ├── GUIDELINES/   ← coding standards
│   └── AGENT-MEMORY/ ← LTM vector store
├── AGENT.json        ← agent manifest
└── README.md         ← human readme
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

## Reading List

<!-- Which documents should the agent read to understand the project? In order of priority. -->

1. This file (READ-AGENT.md)
2. `AGENT.json` — workspace rules, permissions, session hygiene
3. `WORKING/GUIDELINES/` — coding standards
4. `WORKING/docs/` — architecture whitepapers
5. ...

---

## Known Issues / Tech Debt

<!-- Things the agent should be aware of but that are not the current focus. -->

- ...
- ...

---

> **Last updated:** {date}  
> **Updated by:** {agent or human}
