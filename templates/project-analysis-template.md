# PROJECT-ANALYSIS.md
# Pre-Manifest Project Analysis — AAMS/1.0

> **Fill this out before writing `AGENT.json` and `READ-AGENT.md`.**  
> This document captures the reality of your project — topology, tools, history, constraints.  
> It becomes the single source of truth for all manifest decisions.  
> Save it as `PROJECT-ANALYSIS.md` in the repo root.

---

## 1. Project Identity

| Field | Value |
|---|---|
| Project name | |
| Short description (one sentence) | |
| Project type | `web-app` / `api` / `library` / `cli` / `data-pipeline` / `infrastructure` / `other` |
| Tech stack (main language + frameworks) | |
| Current status | `greenfield` / `active` / `maintenance` / `legacy` |
| Team size (humans working on this) | |
| License | |
| Primary language of documentation | |

---

## 2. Repository Topology

> Affects: `gitignore_patterns`, `permissions.filesystem.write`, `workspace.root`

| Question | Answer |
|---|---|
| How many repositories? | `1` / `monorepo` / `polyrepo (N repos)` |
| Does a remote exist? | `yes — URL:` / `no (local only)` |
| Is `WORKING/` in the same repo as the code? | `yes` / `no — separate repo at:` |
| Nested repos / submodules? | `none` / `yes — describe:` |
| Default branch name | `main` / `master` / other: |
| Branch strategy | `trunk-based` / `gitflow` / `other:` |
| Sensitive paths (write-critical) | |

---

## 3. Filesystem Reality

> Affects: `workspace.structure`, `permissions.filesystem`

| Path | Description |
|---|---|
| Project root | |
| `WORKING/` location | |
| Source code | |
| Config files | |
| Build output | |
| Test output | |
| Write-sensitive paths (must not be touched by agent) | |

---

## 4. Existing Tools & Scripts

> Affects: `tools.registry`, `workspace.code_hygiene`, `permissions.process`

| Name | Path | Type | Agent can use? | CI-integrated? |
|---|---|---|---|---|
| | | `cli` / `python` / `shell` / `http` | `yes` / `no` | `yes` / `no` |

**LTM tool (if exists):**
- Path: 
- Backend: `chromadb` / `json-file` / `sqlite` / `none`
- Commands available: 

**Secret scanner (if exists):**
- Tool: `gitleaks` / `trufflehog` / `custom` / `none`
- Pre-commit hook: `yes` / `no`

---

## 5. LTM State

> Affects: `memory.long_term`, `workspace.onboarding` (Erstaufbau vs. inkremental)

| Question | Answer |
|---|---|
| Does an LTM already exist? | `yes` / `no` |
| Backend | `chromadb` / `json-file` / `sqlite` / `none` |
| Location | |
| Approximate chunk count | |
| Audit log (`ltm-index.md`) exists? | `yes` / `no` |
| Onboarding mode | `fresh-build` / `incremental (existing LTM, add only new)` |

---

## 6. Session & Workpaper History

> Affects: `workspace.workpaper_rules.naming_pattern`, `session.workpaper_path`

| Question | Answer |
|---|---|
| Existing naming pattern | e.g. `YYYY-MM-DD-topic.md` / `{date}-{agent}-{topic}.md` / none |
| Number of archived workpapers | |
| Open / active workpapers | list or `none` |
| Active tasks (not in a workpaper) | |
| Last session date | |

---

## 7. Security Enforcement

> Affects: `workspace.secrets_policy`, `workspace.output_validation`, `workspace.gitignore_patterns`

| Question | Answer |
|---|---|
| Existing secret scanner | `gitleaks` / `trufflehog` / `custom` / `none` |
| Pre-commit hook for secrets | `yes — tool:` / `no` |
| CI secret scan | `yes — tool:` / `no` |
| Exit-code standard for hooks | `0=ok, 1=block` / `other:` |
| Permitted secret storage locations | `.env` / `secret manager:` / `other:` |
| Files that must never be committed | `.env`, `.env.*`, `*.pem`, `*.key` — add others: |

---

## 8. Governance

> Affects: `governance`, `permissions`

| Question | Answer |
|---|---|
| Who may change `AGENT.json`? | |
| Review interval | `never` / `quarterly` / `on major changes` |
| Maintainer contact | |
| Approval required for agent permission changes? | `yes` / `no` |

---

## 9. Open Debt & Current Priorities

> Affects: `READ-AGENT.md` (Known Issues), first workpaper

**What must the agent know at session start?**
<!-- List blockers, known broken things, active work in progress -->

- 

**Active focus (current sprint / milestone):**

- 

**Backlog (known but not started):**

- 

**Known tech debt:**

- 

---

## How to use this document

1. Fill out all 9 sections **before** writing `AGENT.json`
2. Save as `PROJECT-ANALYSIS.md` in the repo root
3. Reference in `AGENT.json` via `workspace.project_analysis_path: "./PROJECT-ANALYSIS.md"`
4. The agent reads this file as Step 0 of onboarding (`read_project_analysis` action)
5. After the manifest is written, keep this document — it is the "why" behind every manifest decision

---

*Template: AAMS/1.0 — `templates/project-analysis-template.md`*
