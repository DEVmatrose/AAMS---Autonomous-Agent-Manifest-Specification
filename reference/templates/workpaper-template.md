# {date} — {agent} — {topic}

**Project:** {project}  
**Module:** {module}  
**Status:** 🚧 IN PROGRESS  
**Date:** {date}

> **Template:** AAMS Workpaper Standard v1.0  
> **Generated from:** `workspace.workpaper_rules.template_file`

---

## 1. Session Scope

### Context from Previous Sessions

<!-- LTM query performed? Open items from previous workpapers? Cleanup tasks? -->

| Source | Relevant Context |
|--------|-----------------|
| LTM query: "{topic}" | |
| Last workpaper: {date} | |
| Open cleanup tasks | |

### Goal of this Session
<!-- One sentence: What should be achieved by the end of this session? Concrete, measurable. -->

### Affected Areas
<!-- Which parts of the project will be touched? -->

- [ ] Infrastructure / Project structure
- [ ] Backend
- [ ] Frontend
- [ ] Database
- [ ] Documentation

---

## 2. Running Log ⚡

> **Live during the session — mandatory.**  
> One entry per completed step. Append-only. Do NOT wait until session end.
> After every deployment, fix, configuration change, or decision — output this block unprompted:
>
> ```
> 📋 Workpaper-Checkpoint
> - Changed: `<file>` — <what> (<why>)
> - Decision: <what was decided and why>
> - Abandoned: <what was discarded> (if applicable)
> ```

| Time | What | File / Area | Decision / Reason |
|------|------|-------------|-------------------|
| | | | |

---

## 3. Session Overview

### Starting Situation
<!-- Where does the project stand now? What is the current state? -->

### Approach
<!-- How will the goal be achieved? What steps? -->

1. ...
2. ...
3. ...

### Technical Decisions
<!-- Key technical decisions made during this session. Can also be documented in section 5. -->

---

## 4. Results

<!-- What was achieved? Code snippets, configurations, decisions. -->

### Result 1

```
// Code or configuration here
```

### Result 2

---

## 5. File Protocol

> **The heart of session hygiene.** Maintain continuously, not just at the end.

### Created
| File | Purpose | Status |
|------|---------|--------|
| | | ✅ done / 🔄 in progress / ⚠️ temporary |

### Modified
| File | What changed | Why |
|------|-------------|-----|
| | | |

### Moved
| From | To | Why |
|------|----|-----|
| | | |

### Archived
| File | Why |
|------|-----|
| | |

### Deleted
| File | Why | Verified? |
|------|-----|-----------|
| | | ✅ / ❌ |

### Leftovers (known remnants)
| File/Folder | Why not cleaned up | Who cleans up | By when |
|-------------|-------------------|---------------|---------|
| | | | |

---

## 6. Decisions and Rationale

| Decision | Rationale | Alternatives considered |
|----------|-----------|----------------------|
| | | |

---

## 7. Next Steps

> **Concrete formulation:** Who, when, what. Not "sometime".

- [ ] **Next session:** ...
- [ ] **Cleanup:** ...
- [ ] **Review needed:** ...

---

## 8. Session Closing Checklist

- [ ] File protocol complete (created/modified/moved/archived/deleted)?
- [ ] No temporary test files in repo (`test-*`, `debug-*`, `temp-*`)?
- [ ] No commented-out code blocks without explanation?
- [ ] **⚠️ No secrets/passwords/tokens/API keys in plain text in workpaper?** *(Absolute Secret Exclusion Policy — scan before saving. See `workspace.output_validation.forbidden_patterns` in AGENT.json)*
- [ ] `.env.example` updated if new environment variables?
- [ ] Relevant whitepapers checked for currency?
- [ ] Architecture decisions noted in corresponding whitepaper?
- [ ] Discarded work branches explicitly marked as ABANDONED?
- [ ] Next steps are concretely formulated (not "sometime")?
- [ ] Cleanup tasks for next session named?
- [ ] LTM re-ingest performed?

---

**Session ended:** {date}  
**Status:** ✅ Completed / ⚠️ Interrupted — Reason: ...
