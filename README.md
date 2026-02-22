# Land Ahoy: Your Repo as an Agentic Workspace

> **AAMS — Autonomous Agent Manifest Specification**  
> `README.md` is for humans. `AGENT.json` is for machines.

**[→ devmatrose.github.io/Autonomous-Agent-Manifest-Specification](https://devmatrose.github.io/AAMS---Autonomous-Agent-Manifest-Specification/)**

---

If you want to survive on the open sea, you need two things: a good crew — and a map everyone can read. The new deckhand. The night watch relief. The AI.

That's exactly what AAMS is — the Autonomous Agent Manifest Specification.

---

## The Problem Remains. The Solution Is Now Clearer.

Session 48 doesn't know what session 47 decided. That was the problem back then. It's the problem today. And no agent framework in the world solves it — because the problem isn't in the framework. It's in the structure of the repo.

A repo without agent structure is like a ship without a logbook. Everyone knows what they did yesterday. Nobody knows what came before.

---

## One Year of Lessons

I've worked with AI agents in real projects for over a year. What I learned:

> The most important thing is not that agents can write code.  
> The most important thing is that they know **where they are**.

Without structure, context is lost. Without context, mistakes happen. Duplicate decisions. Orphaned files. Technical debt nobody ordered.

The solution is not a new AI. The solution is **discipline in the repo**.

---

## AAMS Is Not a Framework

This is the most important clarification.

AAMS is not a tool. Not a runtime. Not a framework that needs to be installed.

AAMS is a **single file** dropped into any repo:

```
.agent.json
```

An agent that reads this file immediately knows:

- Where documentation belongs
- How sessions are structured
- Where long-term memory lives
- What it's allowed to do — and what it's not

No `npm install`. No `pip install`. No setup.

---

## Works With Every Agent. Not Just One.

Cursor has `.cursorrules`. Copilot has `.github/copilot-instructions.md`. Claude Code has `CLAUDE.md`. Codex has `AGENTS.md`. Windsurf has `.windsurfrules`.

Every tool has its own convention. If you commit to one, you lock out the others.

AAMS solves this with a single bridge file:

```
AGENTS.md  ←  read by all major AI tools
    ↓
READ-AGENT.md  ←  project context and agent contract
    ↓
.agent.json    ←  bootstrap rules and workspace structure
```

One setup. Copilot, Cursor, Claude Code, Codex, Windsurf, Aider, Continue.dev — they all read `AGENTS.md`. From there, they reach the same contract. No duplication. No tool lock-in.

**That's the actual differentiator.** Not the folder structure. The portability.

---

## Which File Do I Need?

Three files, three different purposes — not three versions of the same thing:

| File | Who reads it | What it is |
|---|---|---|
| `AGENTS.md` | Every AI tool (Copilot, Cursor, Claude Code, Codex, Windsurf...) | Thin bridge. Points to READ-AGENT.md. |
| `.agent.json` | Any agent doing bootstrap | Minimal contract. Drop into any repo. |
| `AGENT.json` | Reference / full manifest | Fully annotated template. All fields, all options. |

**Starting a new project?** Copy `.agent.json`. Done.

**Onboarding an existing project?** Fill out `templates/project-analysis-template.md` first — it captures repo topology, existing tools, LTM state, and conventions before you write a single line of manifest.

**Building a framework or harness?** Use `AGENT.json` as the reference manifest.

**Working with Copilot, Cursor, etc.?** `AGENTS.md` in the root is all you need — it routes them to the rest automatically.

---

## The Three-Layer Documentation Model

The actual core of AAMS. Three layers, mandatory:

**Workpaper** — What am I doing in this session?  
Created at session start, archived at session end. With a complete file protocol: what was created, changed, deleted.

**Whitepaper** — How is this system built?  
Stable architecture truth. Written once, updated only on architecture decisions. Never deleted.

**Long-Term Memory** — What have we learned over time?  
After every session the workpaper is ingested into LTM. Session N+1 queries LTM before starting. Each session builds on the last.

```
WORKING/
├── WHITEPAPER/       ← Stable system truth. Never delete.
├── WORKPAPER/        ← Active session work. One file per session.
│   └── closed/        ← Archived completed sessions.
├── MEMORY/           ← Human-readable audit log. In Git. Always.
└── AGENT-MEMORY/     ← Vector store (ChromaDB). Queryable LTM. In .gitignore.
```

Two layers, both mandatory: the **audit log** (`ltm-index.md`) is what humans read and what survives a fresh clone. The **vector store** (`AGENT-MEMORY/`) is what agents query efficiently. Without the vector store, context degrades after ~100 sessions. Without the audit log, a fresh clone starts blind.

---

## The Agent Contract

A `READ-AGENT.md` in the repo root defines the normative contract for every agent entering this repo.

Any agent entering this repo executes this contract. No discussion. No interpretation.

```
On first entry:       Read READ-AGENT.md → check structure → scan repo → index into MEMORY/
On session start:     Read READ-AGENT.md → check last workpaper → query MEMORY/
On session end:       Complete workpaper → ingest → move to closed/ → update READ-AGENT.md
```

Works with any agent framework. And without any framework.

---

## Portable Into Any Repo

The decisive design goal: **one file, every repo**.

Does a developer have their own agent framework? Their framework recognizes the `WORKING/` structure and uses it directly as a subagent workspace.

Does a developer have no framework? `.agent.json` + `READ-AGENT.md` are the smallest possible agent framework — declarative, idempotent, zero dependencies.

Long-term goal: AAMS becomes the de-facto standard that every agent recognizes in every repo.

---

## Applied to Itself

This project — the project that describes the standard — built its own workspace using AAMS on day one.

One `.agent.json` read. Structure created. First workpaper written. First whitepaper written. LTM populated. Three open GitHub issues resolved. All of it documented, traceable, reproducible.

That's not proof that AAMS works at scale, in legacy repos, or with uncooperative agents. It's a working example of the workflow — what a session looks like, what gets created, what survives into the next session.

The real test is your project.

---

## Technical Specification

| File | Content |
|---|---|
| [`SPEC.md`](./SPEC.md) | Full technical reference |
| [`AGENT.json`](./AGENT.json) | Annotated reference manifest |
| [`.agent.json`](./.agent.json) | Minimal bootstrap contract |
| [`AGENT_SCHEMA.json`](./AGENT_SCHEMA.json) | JSON Schema for validation |

---

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) — public domain. Use it, fork it, build on it.

---

*One file. Every repo. No more starting from zero.*