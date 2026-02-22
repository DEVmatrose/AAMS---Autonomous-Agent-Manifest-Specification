# WP-002 — Related Work: AAMS in Context

**WHITEPAPER — AAMS / Autonomous Agent Manifest Specification**
**Status:** Active
**Version:** 1.0
**Created:** 2026-02-22

---

## Purpose

This whitepaper positions AAMS relative to existing work in agent memory, workflow orchestration, reproducibility tooling, and emerging AI coding conventions. The goal is not to argue superiority, but to show what problem space AAMS occupies and how it relates to adjacent standards and frameworks.

---

## Core Positioning Statement

> AAMS is not solving the LTM problem. It is creating the scaffolding that makes LTM solutions pluggable.

AAMS declares *where* memory lives, *when* it must be queried, and *how* sessions are documented. It does not implement retrieval, embedding, or summarization. This makes AAMS infrastructure-neutral and intentionally layered *below* memory frameworks.

---

## Comparison Table

| Approach | Memory Model | Persistence | Cross-Agent Coordination | AAMS Relationship |
|---|---|---|---|---|
| **MemGPT / Letta** (Packer et al., 2023) | Tiered (in-context + archival) | Managed internally | Single agent | AAMS sits below: declares where archival store is, MemGPT manages what goes in |
| **LangChain Memory** | Pluggable buffer/summary abstractions | Runtime-dependent | Framework-specific | AAMS is backend-agnostic; LangChain memory is a valid `ltm_store_backend_recommended` target |
| **DVC (Data Version Control)** | Artifact + pipeline tracking | Git + remote storage | Human team coordination | Non-overlapping; DVC tracks model artifacts, AAMS tracks agent session artifacts — could coexist |
| **FIPA ACL / BDI agents** | Agent communication language + belief-desire-intention | Runtime shared state | Multi-agent, standardized | Historical predecessor; AAMS is a simpler, repo-scoped, file-based coordination layer |
| **`.cursorrules`** | Instruction injection per-editor | File in repo | Single editor | AAMS generalizes: `.agent.json` covers all agents, not just Cursor |
| **`CLAUDE.md` / `CODEX.md`** | Tool-specific instruction injection | File in repo | Tool-specific | AAMS unifies: `AGENTS.md` + `.agent.json` replace all per-tool files as the canonical entry point |
| **`.github/copilot-instructions.md`** | Copilot-specific context | File in repo | GitHub Copilot only | Bridged by AAMS: `AGENTS.md` redirects Copilot to the canonical AAMS context |
| **OpenAI Assistants API** | Thread + file store | Cloud-managed | Per-assistant | No overlap; AAMS is repo-local, not cloud-hosted |

---

## Detailed Analysis

### MemGPT / Letta
*Packer et al., "MemGPT: Towards LLMs as Operating Systems", 2023.*

MemGPT introduces a two-tier memory model: a finite in-context window (main memory) and an unbounded external archival store. The system manages swapping between them automatically, with the LLM itself issuing memory function calls.

**What MemGPT solves:** The within-session context limit — how to process documents longer than the context window.

**What MemGPT does not solve:** What workspace the agent operates in when it arrives at a fresh repo. There is no session discipline, no workpaper protocol, no permission model.

**AAMS Relationship:** Complementary. An AAMS-conforming agent could use MemGPT-style managed memory as its LTM backend. `.agent.json` would declare `ltm_store_backend_recommended: "letta"` and the session protocol remains AAMS.

---

### LangChain Memory

LangChain provides a family of memory abstractions: `ConversationBufferMemory`, `ConversationSummaryMemory`, `VectorStoreRetrieverMemory`, etc. These are runtime constructs that get injected into chain calls.

**What LangChain solves:** How to pass relevant history into the LLM's next call, within a running process.

**What LangChain does not solve:** Persistent session documentation, cross-session identity (which project, which role), or structured workspace governance.

**AAMS Relationship:** LangChain memory is a valid implementation for the inner retrieval mechanism declared in `.agent.json`. The workpaper/LTM discipline AAMS imposes is orthogonal to the runtime abstraction LangChain provides.

---

### DVC (Data Version Control)

DVC adds Git-like versioning for large files, datasets, and ML pipelines. It tracks reproducibility artifacts: data sources, model weights, metrics, pipeline stages.

**What DVC solves:** Reproducibility of ML experiments.

**What DVC does not solve:** Agent session discipline, LLM coordination, or multi-agent continuity.

**AAMS Relationship:** Non-competing. In a data science repo, DVC manages the data artifacts; AAMS manages the agent session artifacts (`WORKING/`). They can coexist without conflict in the same repository.

---

### Per-Tool Instruction Files (`.cursorrules`, `CLAUDE.md`, `CODEX.md`, `.github/copilot-instructions.md`)

The current landscape has an emerging proliferation of per-tool instruction files:
- Cursor reads `.cursorrules`
- Claude Code reads `CLAUDE.md`
- OpenAI Codex reads `CODEX.md`
- GitHub Copilot reads `.github/copilot-instructions.md`

This fragmentation forces maintainers to duplicate context across multiple files, with no coordination standard between them.

**What these files solve:** Tool-specific instruction injection.

**What they do not solve:** Cross-tool consistency, machine-readable structure, session memory, or governance.

**AAMS Relationship:** AAMS unifies under one canonical entry point (`AGENTS.md` → `.agent.json`). Each per-tool file simply redirects to AAMS. This was the original motivation for AAMS: one repo contract, all agents.

---

### FIPA ACL and BDI Agent Standards (Historical)

The Foundation for Intelligent Physical Agents (FIPA) developed multi-agent communication standards in the late 1990s. BDI (Belief-Desire-Intention) architectures formalized agent state representation. These influenced early agent frameworks (JADE, Jason).

**Why they did not transfer to LLM coding agents:** They assume a managed runtime, message broker, and agent registry — none of which exist in the IDE-coding-agent context. LLM agents are transient, repo-local, and do not maintain distributed agent registries.

**AAMS Relationship:** AAMS is conceptually similar in intent (coordination, shared understanding of agent role) but architecturally minimal — the repo filesystem is the coordination bus, files are the messages, and `AGENTS.md` is the single entry point. No broker required.

---

## Gap Analysis: What Nothing Else Covers

After reviewing adjacent work, these capabilities are unique to AAMS or not addressed by existing standards:

| Capability | Covered by existing work? | AAMS position |
|---|---|---|
| Per-repo agent identity (`agent_id`, `role`, `version`) | No | Core |
| Explicit workspace structure enforcement (`must_exist` paths) | No | Core |
| Workpaper protocol (session-as-artifact) | No | Core |
| LTM backend declaration (declarative, not implementation) | No | Core |
| Filesystem permission model (`read_only`, `restricted_write`, etc.) | No | Core |
| Cross-tool canonical entry point | Partially (AGENTS.md convention emerging) | Core |
| LTM trigger conditions (threshold-based) | No | Extended |
| Skill registry + tool declarations | Partially (OpenAI Functions) | Extended |

---

## Conclusion

AAMS occupies a layer that no existing standard or framework fills: **the coordination contract between a developer's repository and any AI coding agent that enters it.** It is not a memory framework, not a runtime, and not a workflow engine. It is the interface layer on top of which those systems operate.

The closest analogy is a constitution for a codebase: it declares the workspace structure, agent role, permissions, and session discipline — and is indifferent to which agent or backend fulfills those declarations.

---

## References

- Packer, C. et al. (2023). *MemGPT: Towards LLMs as Operating Systems.* arXiv:2310.08560
- LangChain Documentation: [https://docs.langchain.com/docs/components/memory](https://docs.langchain.com/docs/components/memory)
- DVC Documentation: [https://dvc.org/doc](https://dvc.org/doc)
- FIPA Specifications: [http://www.fipa.org/specs/](http://www.fipa.org/specs/)
- AAMS Specification: `SPEC.md` in this repository

---

*Whitepaper maintained by project maintainer. Update when major adjacent frameworks release new coordination-layer features.*
