# AAMS — Autonomous Agent Manifest Specification

> **The missing standard for AI agents working in repositories.**  
> `README.md` is for humans. `AGENT.json` is for machines.

---

## The Problem

Every repository has a `README.md`. It tells humans what the project is, how to install it, and how to contribute.

But when an AI agent clones that repo, it has no idea: Where should I store my work? How do I keep context between sessions? What am I allowed to touch? Where do I document my decisions? How do I build up long-term memory for this project?

Every new chat session starts from zero. Context gets lost. Decisions get repeated. Files get orphaned. What was decided in session 47, session 48 doesn't know.

We fix that.

---

## What is AAMS?

AAMS is an open specification for a machine-readable manifest file — `AGENT.json` — that sits in any repository, right next to the `README.md`, and tells an AI agent **how to work in this project**.

It defines:
- **Workspace structure** — where to put whitepapers, workpapers, guidelines, and tools
- **Memory** — how to build and maintain long-term memory (LTM) for the project
- **Session hygiene** — how to log work, create audit trails, and close sessions cleanly
- **Permissions** — what the agent may read, write, execute, and what is forbidden
- **Tools** — which external tools and APIs the agent may use

```
any-project/
├── README.md        ← for humans    (overview, setup, contribution)
├── AGENT.json       ← for machines  (workspace, permissions, memory, sessions, tools)
└── WORKING/         ← agent workspace (created per AGENT.json)
    ├── docs/        ← whitepapers (long-term project knowledge)
    ├── WORKPAPER/   ← active work sessions
    │   └── close/   ← archived sessions
    ├── GUIDELINES/  ← coding standards, architecture rules
    └── TOOLS/       ← project-specific scripts
```

One file. One standard. Lives alongside your README. Works with any model, any runtime, any stack.

---

## How It Works

### First Contact (Onboarding)

1. **Agent clones a repo** and finds `AGENT.json`
2. **Reads entry point** (`READ-AGENT.md`) — gets project context in 30 seconds
3. **Creates workspace structure** — the `WORKING/` folder with all subdirectories
4. **Scans the repository** — files, languages, dependencies, existing documentation
5. **Creates guidelines** — derives coding standards and architecture rules from the project
6. **Indexes everything into LTM** — all docs into the vector store (e.g. ChromaDB)
7. **Creates first workpaper** — onboarding protocol documenting what was found

All these steps are defined in `workspace.onboarding` — not hardcoded, configurable per project.

### Every Session

1. **Query LTM** — load context for the session topic (mandatory trigger)
2. **Read open workpapers** — continue where the last session left off
3. **Work** — following permissions, tool bindings, coding guidelines, and code hygiene rules
4. **Document** — every created/changed/deleted file goes into the workpaper (tracked continuously, not at the end)
5. **Close session** — run closing checklist (no secrets? no temp files? no abandoned code?), re-ingest LTM, archive workpaper

### The Result

No context loss. No duplicate work. No orphaned files. Session N+1 knows what session N decided.

---

## Quick Example

A minimal `AGENT.json` with the essential fields. The full annotated template in [`AGENT.json`](./AGENT.json) contains all available options including onboarding steps, workpaper rules, code hygiene, and secrets policy.

```json
{
  "_spec": "AAMS/1.0",
  "identity": {
    "name": "my-agent",
    "version": "1.0.0",
    "type": "worker"
  },
  "runtime": {
    "model": "mistral-nemo",
    "provider": "ollama",
    "local": true,
    "endpoint": "http://localhost:11434"
  },
  "skills": {
    "capabilities": ["code_generation", "documentation", "security_audit"]
  },
  "permissions": {
    "filesystem": {
      "read": ["./"],
      "write": ["./WORKING"],
      "forbidden": ["/etc", "/root", "~/.ssh"]
    },
    "network": { "allowed": ["localhost"], "forbidden": ["0.0.0.0/0"] },
    "process": { "shell_execution": false, "sudo": false, "spawn_agents": false },
    "data": { "can_read_secrets": false, "can_exfiltrate": false, "pii_handling": "forbidden" }
  },
  "memory": {
    "short_term": { "backend": "in-memory", "ttl_seconds": 3600 },
    "long_term":  { "backend": "chroma", "path": "./WORKING/AGENT-MEMORY" }
  },
  "session": {
    "log_actions": true,
    "log_level": "info",
    "audit_trail": true,
    "create_workpaper": true,
    "workpaper_path": "./WORKING/WORKPAPER/{date}-{agent}-session.md"
  },
  "workspace": {
    "root": "./WORKING",
    "entry_point": "./READ-AGENT.md",
    "structure": {
      "whitepapers": "./WORKING/docs",
      "workpapers": "./WORKING/WORKPAPER",
      "workpapers_closed": "./WORKING/WORKPAPER/close",
      "guidelines": "./WORKING/GUIDELINES"
    },
    "auto_create": true
  },
  "tools": { "enabled": [] }
}
```

---

## Validate Your Manifest

```bash
# Node.js
npm install -g ajv-cli
ajv validate -s AGENT_SCHEMA.json -d AGENT.json

# Python
pip install check-jsonschema
check-jsonschema --schemafile AGENT_SCHEMA.json AGENT.json
```

✅ Valid. Ship it.

---

## Specification

The full specification lives in [`SPEC.md`](./SPEC.md).

### Sections at a Glance

| Section       | Required | Purpose |
|---------------|----------|---------|
| `identity`    | ✅        | Name, version, agent type |
| `runtime`     | ✅        | Model, provider, endpoint |
| `skills`      | ✅        | Declared capabilities |
| `permissions` | ✅        | Explicit allow/deny rules |
| `memory`      | ✅        | Short-term, long-term, session persistence |
| `session`     | ✅        | Logging, workpaper, audit trail |
| `tools`       | ✅        | External tool and API bindings |
| `workspace`   | ✅        | Working directory, onboarding, session hygiene, code hygiene, secrets policy |
| `governance`  | ⬜        | Compliance and review metadata |
| `metadata`    | ⬜        | Free-form field for provider extensions and project-specific data |

**Core principle: Default-Deny.** Everything not explicitly permitted is forbidden.

---

## Design Principles

**Local-first.** Version 1.0 is built for self-hosted agents running local models. Cloud and multi-agent mesh profiles are planned and contributions are welcome.

**Workspace-driven.** An agent that clones a repo gets a defined workspace structure — whitepapers for long-term knowledge, workpapers for sessions, guidelines for standards. No more guessing where to put things.

**Explicit over implicit.** Permissions are declared, not assumed. An agent that doesn't declare a capability doesn't have one.

**Continuity across sessions.** Long-term memory, session logs, and workpaper archives ensure that session N+1 knows what session N decided.

**Machine-readable, human-auditable.** JSON for machines, comments (`_doc` fields) for the humans reviewing it.

**Stack-agnostic.** Works with Ollama, LM Studio, llama.cpp, OpenAI, Anthropic, or any custom endpoint.

---

## Roadmap

| Profile    | Status        | Description |
|------------|---------------|-------------|
| `local-v1` | ✅ Current     | Self-hosted, local models |
| `cloud-v1` | 🔜 Planned    | Cloud providers, API keys, rate limits |
| `mesh-v1`  | 🔜 Planned    | Multi-agent coordination, trust levels |
| `edge-v1`  | 💡 Idea       | IoT and edge deployment |

---

## Repository Structure

```
aams/
├── README.md              ← you are here
├── SPEC.md                ← full specification
├── AGENT.json             ← annotated template
├── AGENT_SCHEMA.json      ← JSON Schema for validation
└── registry/
    └── capabilities.md    ← standard capability registry (coming soon)
```

**In your project (after agent setup):**

```
your-project/
├── README.md              ← for humans
├── AGENT.json             ← for agents
├── READ-AGENT.md          ← agent entry point
└── WORKING/               ← created by agent
    ├── docs/              ← whitepapers (architecture, decisions)
    ├── WORKPAPER/         ← active sessions
    │   └── close/         ← archived sessions
    ├── GUIDELINES/        ← coding standards, rules
    ├── TOOLS/             ← project-specific scripts
    └── AGENT-MEMORY/      ← LTM vector store (e.g. ChromaDB)
```

---

## Contributing

AAMS is an open standard. The field is empty and there's a lot to build.

**Ways to contribute:**
- Propose new standard capabilities → `registry/capabilities.md`
- Help design the `cloud-v1` or `mesh-v1` profiles
- Build validator tooling or GitHub Actions
- Share your `AGENT.json` as a reference implementation
- Open issues for edge cases the spec doesn't cover yet

Open an issue or a pull request. All backgrounds welcome — agent developers, security researchers, platform engineers, and anyone who thinks AI infrastructure deserves proper standards.

---

## License

AAMS Specification 1.0 is released under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

The specification is public domain. Use it, fork it, build on it. No permission needed.

---

*Yes, this project has a `README.md`. The irony is intentional.*