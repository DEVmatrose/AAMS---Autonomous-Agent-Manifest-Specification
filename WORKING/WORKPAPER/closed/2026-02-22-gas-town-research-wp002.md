# WORKPAPER — Gas Town Research + WP-002 Update

**Session:** 2026-02-22 (continuation after summarization)
**Status:** CLOSED
**Commits:** `8f8203b`

---

## File Protocol

| Action | File | Result |
|---|---|---|
| READ | `WORKING/WHITEPAPER/WP-002-related-work.md` | Lines 1-45, 100-142 read to determine structure |
| READ | `WORKING/MEMORY/ltm-index.md` | Last entry: 046 confirmed |
| FETCH | https://heise.de/-11177514 | Full Gas Town article retrieved |
| EDIT | `WORKING/WHITEPAPER/WP-002-related-work.md` | 6 replacements applied, v1.0 → v1.1, +50 lines |
| EDIT | `WORKING/MEMORY/ltm-index.md` | Entry 047 added |
| COMMIT | Both files | `8f8203b` |
| PUSH | `main` | Remote updated `f7a9c2b` → `8f8203b` |

---

## Research Summary: Gas Town

**What it is:** Multi-agent orchestrator for coding agents (primarily Claude Code). 10-30+ parallel Polecats in Git Worktrees. By Steve Yegge. Released 2026-01-01.

**Architecture:** Mayor (task decomp) → Deacon (watchdog) → Polecats (workers) → Refinery (QA) → Sweeps (arch debt). Beads/Convoys/Mailboxes/Handoffs for coordination.

**Key finding:** Heise article (2026-02-21) explicitly states Gas Town does NOT replace rule files (`AGENT.md`/`CLAUDE.md`) — they are required complements. This is direct in-the-wild validation of AAMS's premise.

---

## Decisions

1. Gas Town is "Complementary + Validating" — not a competitor. Different layers (execution vs. repo contract).
2. Position Gas Town as the strongest external validation found to date.
3. "Cattle not Pets" convergence noted: disposable agents require standardized entry contracts → exactly `.agent.json`.
4. Section placed after FIPA (chronologically + architecturally appropriate).
5. Comparison table, Gap Analysis, Conclusion, References all updated for consistency.

---

## WP-002 Changes

- Version: 1.0 → 1.1
- Comparison table: +1 row (Gas Town)
- Detailed analysis: new `### Gas Town` section (~40 lines including inner comparison table)
- Gap Analysis: +1 row (Multi-agent repo contract)
- Conclusion: +1 paragraph citing Gas Town as strongest external validation
- References: +2 entries (Yegge 2026 + heise 2026)

---

## Next Steps

- Consider updating `docs/index.html` proof card (currently shows "2 external reviews, 46 LTM entries") → now 47 LTM entries
- Consider `README.md` / landing page: mention Gas Town validation as a proof point
- WP-003 candidate: "AAMS Integration Patterns" — how Gas Town, Cursor, Claude Code, Copilot all compose with AAMS
