# AAMS Capability Registry

> **Version:** 1.0  
> **Status:** Stable  
> **Part of:** [AAMS — Autonomous Agent Manifest Specification](../SPEC.md)

This is the canonical registry of standard capability identifiers for the `skills.capabilities` field in `AGENT.json`.

---

## Usage

```json
"skills": {
  "capabilities": [
    "code_generation",
    "file_management",
    "shell_execution"
  ]
}
```

`capabilities` is a **self-description** — it declares what the agent can do, not what it is permitted to do. Permissions are controlled exclusively by the `permissions` section.

> Validators SHOULD warn when a capability listed here is contradicted by the `permissions` section (e.g. `shell_execution` capability + `permissions.process.shell_execution: false`).

---

## Standard Capabilities

### Code

| Identifier              | Description | Related Permission |
|-------------------------|-------------|-------------------|
| `code_generation`       | Generate source code in any language from requirements or context | — |
| `code_review`           | Analyse existing code for bugs, style issues, and architecture | — |
| `refactoring`           | Restructure code without changing external behaviour | — |
| `test_generation`       | Write unit, integration, or end-to-end tests | — |
| `debugging`             | Identify and fix bugs in existing code | — |
| `dependency_management` | Add, remove, or update package dependencies | `filesystem.write` |

### Documentation

| Identifier         | Description | Related Permission |
|--------------------|-------------|-------------------|
| `documentation`    | Write technical documentation, READMEs, API docs, comments | `filesystem.write` |
| `spec_writing`     | Write formal specifications, RFCs, or architecture decision records | `filesystem.write` |
| `changelog_writing`| Maintain CHANGELOG.md from git history or task descriptions | `filesystem.write` |

### File System

| Identifier         | Description | Related Permission |
|--------------------|-------------|-------------------|
| `file_management`  | Create, move, rename, delete files within permitted paths | `filesystem.write` |
| `directory_management` | Create and manage directory structures | `filesystem.write` |
| `file_search`      | Search file contents and names across the repository | `filesystem.read` |

### Shell & Process

| Identifier         | Description | Related Permission |
|--------------------|-------------|-------------------|
| `shell_execution`  | Execute shell commands and scripts | `process.shell_execution: true` |
| `process_management` | Start, stop, monitor processes | `process.shell_execution: true` |
| `build_tooling`    | Run build systems (make, npm, cargo, gradle, etc.) | `process.shell_execution: true` |
| `ci_cd_integration`| Interact with CI/CD pipeline APIs or configurations | `process.shell_execution: true` |

### Data & Analysis

| Identifier          | Description | Related Permission |
|---------------------|-------------|-------------------|
| `data_analysis`     | Analyse datasets, produce statistics, detect patterns | — |
| `data_transformation` | Convert, clean, or reshape data between formats | `filesystem.write` |
| `image_processing`  | Analyse or generate images | — |
| `pdf_processing`    | Read, parse, or generate PDF documents | `filesystem.read` |

### Network & Web

| Identifier      | Description | Related Permission |
|-----------------|-------------|-------------------|
| `web_search`    | Search the web and retrieve information | `network.allowed` |
| `web_scraping`  | Extract structured data from web pages | `network.allowed` |
| `api_calls`     | Make HTTP API calls to external or internal services | `network.allowed` |
| `webhook_handling` | Receive and process inbound webhooks | `network.allowed` |

### Memory & Context

| Identifier        | Description | Related Permission |
|-------------------|-------------|-------------------|
| `ltm_management`  | Ingest, query, and maintain the long-term memory store | `filesystem.write` |
| `context_summarization` | Summarize long contexts to reduce token usage | — |
| `workpaper_management` | Create, update, close, and archive session workpapers | `filesystem.write` |

### Security

| Identifier          | Description | Related Permission |
|---------------------|-------------|-------------------|
| `security_audit`    | Review code and configurations for security vulnerabilities | — |
| `secret_scanning`   | Detect secrets, tokens, and credentials in files or changes | — |
| `dependency_audit`  | Check dependencies for known CVEs | — |

### Multi-Agent

| Identifier           | Description | Related Permission |
|----------------------|-------------|-------------------|
| `agent_orchestration`| Coordinate and delegate to sub-agents | `process.spawn_agents: true` |
| `agent_communication`| Send/receive structured messages with other agents | `network.allowed` |
| `task_routing`       | Route tasks to the most capable available agent | `process.spawn_agents: true` |

---

## Custom Skills

For capabilities not in this registry, use `custom_skills`:

```json
"skills": {
  "capabilities": ["code_generation"],
  "custom_skills": [
    {
      "name": "erp_integration",
      "description": "Read and write data via the company ERP REST API",
      "input_schema": {
        "type": "object",
        "properties": {
          "endpoint": { "type": "string" },
          "payload":  { "type": "object" }
        }
      }
    }
  ]
}
```

Custom skills SHOULD use `snake_case` identifiers. If a custom skill becomes broadly used, submit it for inclusion in this registry.

---

## Contributing

To propose a new standard capability:

1. Open an issue in the AAMS repository with the proposed identifier, description, and related permission fields
2. The identifier must be `snake_case`, globally unique, and unambiguous
3. Include at least one real-world use case
4. The capability is added here once accepted

→ Repository: [DEVmatrose/AAMS](https://github.com/DEVmatrose/AAMS)

---

*AAMS Capability Registry 1.0 — CC0 1.0 Universal*
