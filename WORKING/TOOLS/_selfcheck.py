#!/usr/bin/env python3
"""AAMS Self-Check — run from project root."""
import json, pathlib, re, sys
from jsonschema import Draft202012Validator

ok = True
root = pathlib.Path(".")

def check(label, passed, detail=""):
    global ok
    status = "OK  " if passed else "FAIL"
    if not passed:
        ok = False
    suffix = f"  {detail}" if detail else ""
    print(f"  [{status}] {label}{suffix}")


# ── 1. JSON syntax ──────────────────────────────────────────────────────────
try:
    schema = json.load(open("AGENT_SCHEMA.json", encoding="utf-8"))
    data   = json.load(open("AGENT.json",        encoding="utf-8"))
    check("JSON syntax (AGENT.json + AGENT_SCHEMA.json)", True)
except json.JSONDecodeError as e:
    check("JSON syntax", False, str(e)); sys.exit(1)

# ── 2. Schema validation ─────────────────────────────────────────────────────
errors = list(Draft202012Validator(schema).iter_errors(data))
check("AGENT.json validates against AGENT_SCHEMA.json", not errors,
      f"{len(errors)} error(s)" if errors else "0 errors")
for e in errors:
    print(f"       [{list(e.path)}] {e.message}")

# ── 3. Referenced files exist ─────────────────────────────────────────────────
refs = {
    "workspace.entry_point":              data["workspace"]["entry_point"],
    "workpaper_rules.template_file":      data["workspace"]["workpaper_rules"]["template_file"],
    "workpaper_rules.template_file_quick":data["workspace"]["workpaper_rules"]["template_file_quick"],
    "runtime.system_prompt_file":         data["runtime"].get("system_prompt_file", ""),
}
for key, val in refs.items():
    if val:
        p = pathlib.Path(val.replace("./", ""))
        check(f"Referenced file exists: {val}", p.exists())

# ── 4. workpaper_path placeholders ───────────────────────────────────────────
wp = data["session"]["workpaper_path"]
check("workpaper_path contains {date} and {agent}", "{date}" in wp and "{agent}" in wp, wp)

# ── 5. Capabilities vs. registry ─────────────────────────────────────────────
reg = pathlib.Path("registry/capabilities.md")
if reg.exists():
    registry_ids = set(re.findall(r"\| `(\w+)`", reg.read_text(encoding="utf-8")))
    caps = data["skills"]["capabilities"]
    unknown = [c for c in caps if c not in registry_ids]
    check("skills.capabilities all in registry/capabilities.md",
          not unknown,
          f"unknown: {unknown}" if unknown else f"{len(caps)} capabilities matched")
else:
    check("registry/capabilities.md exists", False)

# ── 6. Workspace root ─────────────────────────────────────────────────────────
wr = pathlib.Path(data["workspace"]["root"].replace("./", ""))
check(f"workspace.root exists ({wr})", wr.exists())

# ── 7. Workspace structure paths ──────────────────────────────────────────────
for role, path in data["workspace"]["structure"].items():
    if not role.startswith("_"):
        p = pathlib.Path(path.replace("./", ""))
        check(f"structure.{role} exists ({path})", p.exists())

# ── 8. Open workpapers ────────────────────────────────────────────────────────
wp_dir = pathlib.Path("WORKING/WORKPAPER")
open_wps = [f.name for f in wp_dir.glob("*.md")]
# WARN only — on-hold workpapers are valid; FAIL only if unexpected count
if not open_wps:
    check("Open workpapers", True, "NONE (clean)")
else:
    print(f"  [WARN] Open workpapers: {len(open_wps)} found (review if on-hold): {open_wps}")

# ── 9. _spec ──────────────────────────────────────────────────────────────────
check("_spec = AAMS/1.0", data.get("_spec") == "AAMS/1.0")

# ── 10. git status ─────────────────────────────────────────────────────────────
import subprocess
r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
check("Git working tree is clean", r.stdout.strip() == "", r.stdout.strip() or "clean")

# ── 11. SPEC.md cross-refs ───────────────────────────────────────────────────
spec = pathlib.Path("SPEC.md").read_text(encoding="utf-8")
for term in ["restricted_write", "notify_developer", "load_last_n_only",
             "read_project_analysis", "file_exists", "fallback_providers",
             "project_analysis_path"]:
    check(f"SPEC.md documents: {term}", term in spec)

# ── 12. AGENT_SCHEMA.json cross-refs ─────────────────────────────────────────
schema_raw = pathlib.Path("AGENT_SCHEMA.json").read_text(encoding="utf-8")
for term in ["restricted_write", "notify_developer", "load_last_n_only",
             "read_project_analysis", "file_exists", "fallback_providers",
             "project_analysis_path"]:
    check(f"AGENT_SCHEMA.json contains: {term}", term in schema_raw)

# ── Result ───────────────────────────────────────────────────────────────────
print()
print("══════════════════════════════════════════")
print("RESULT:", "✅ ALL CHECKS PASSED" if ok else "❌ ISSUES FOUND")
print("══════════════════════════════════════════")
sys.exit(0 if ok else 1)
