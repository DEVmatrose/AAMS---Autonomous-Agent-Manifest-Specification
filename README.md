# Land Ahoy: Your Repo as an Agentic Workspace

> **AAMS — Autonomous Agent Manifest Specification**  
> `README.md` is for humans. `AGENT.json` is for machines.

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

## The Three-Layer Documentation Model

The actual core of AAMS. Three layers, mandatory:

**Workpaper** — What am I doing in this session?  
Created at session start, archived at session end. With a complete file protocol: what was created, changed, deleted.

**Whitepaper** — How is this system built?  
Stable architecture truth. Written once, updated only on architecture decisions. Never deleted.

**Long-Term Memory** — What have we learned over time?  
After every session the workpaper is ingested into LTM. Session N+1 queries LTM before starting. No more context loss.

```
WORKING/
├── WHITEPAPER/     ← Stable system truth. Never delete.
├── WORKPAPER/      ← Active session work. One file per session.
│   └── closed/     ← Archived completed sessions.
└── MEMORY/         ← Long-term memory. Cross-session context.
```

A good developer does this in their head. An agent needs it explicit and persistent.

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

## Proof: AAMS Tested on Itself

This project — the project that describes the standard — applied it live today.

One `.agent.json` read. Structure created. First workpaper written. First whitepaper written. LTM populated. Three open GitHub issues resolved.

Everything documented. Everything traceable. No context loss.

**That's the proof.**

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

*One file. Every repo. No more chaos.*