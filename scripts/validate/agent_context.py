#!/usr/bin/env python3
"""Read-only health check for agent instructions and the live handoff.

This does not validate curriculum semantics. It catches continuity failures that
commonly follow chat compaction or model switches: missing entry points, bloated
startup context, a stale plan revision/hash, and incomplete handoff structure.
"""

from __future__ import annotations

import hashlib
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "docs/agent/CURRENT_HANDOFF.md"
PLAN = ROOT / "docs/plans/PHASE5_AUGMENTATION_PLAN.md"

REQUIRED_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "CLAUDE.md",
    ROOT / "docs/agent/CONTINUITY_AND_QUALITY.md",
    ROOT / "docs/agent/STAGE_RUNBOOK.md",
    HANDOFF,
    ROOT / "docs/prompts/CLAUDE_PHASE5_RECONCILE_GATE_B.md",
    PLAN,
    ROOT / "docs/decisions/0005-gate-a-approved.md",
    ROOT / "docs/decisions/0006-math-review-approved.md",
    ROOT / "docs/decisions/0007-opt-review-approved.md",
    ROOT / "docs/review/REVIEW_INDEX.md",
    ROOT / "scripts/validate/review_integrity.py",
)

REQUIRED_HANDOFF_HEADINGS = (
    "## Baseline and authority",
    "## Active objectives",
    "## Current review state",
    "## Write ownership and dirty worktree",
    "## Next safe actions and stop conditions",
    "## Verification required at the next boundary",
)

STARTUP_LIMITS = {
    "AGENTS.md": (180, 16 * 1024),
    "CLAUDE.md": (100, 10 * 1024),
    "docs/agent/CURRENT_HANDOFF.md": (160, 16 * 1024),
}


class Report:
    def __init__(self) -> None:
        self.failures = 0
        self.warnings = 0

    def ok(self, message: str) -> None:
        print(f"OK    {message}")

    def warn(self, message: str) -> None:
        self.warnings += 1
        print(f"WARN  {message}")

    def fail(self, message: str) -> None:
        self.failures += 1
        print(f"FAIL  {message}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    report = Report()

    missing = [relative(path) for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        for path in missing:
            report.fail(f"missing required continuity file: {path}")
        return 1
    report.ok(f"required continuity files present ({len(REQUIRED_FILES)})")

    for name, (line_limit, byte_limit) in STARTUP_LIMITS.items():
        path = ROOT / name
        contents = text(path)
        lines = len(contents.splitlines())
        size = len(contents.encode("utf-8"))
        if lines > line_limit or size > byte_limit:
            report.fail(
                f"{name} is too large for startup context: "
                f"{lines}/{line_limit} lines, {size}/{byte_limit} bytes"
            )
        else:
            report.ok(
                f"{name} within startup limit: "
                f"{lines}/{line_limit} lines, {size}/{byte_limit} bytes"
            )

    handoff = text(HANDOFF)
    for heading in REQUIRED_HANDOFF_HEADINGS:
        if heading not in handoff:
            report.fail(f"handoff missing heading: {heading}")
    if all(heading in handoff for heading in REQUIRED_HANDOFF_HEADINGS):
        report.ok("handoff contains required recovery sections")

    updated_match = re.search(r"^Updated:\s*(\d{4}-\d{2}-\d{2})", handoff, re.M)
    if not updated_match:
        report.fail("handoff has no parseable Updated: YYYY-MM-DD field")
    else:
        updated = date.fromisoformat(updated_match.group(1))
        age = (date.today() - updated).days
        if age > 14:
            report.warn(f"handoff is {age} days old; confirm it is still active")
        elif age < 0:
            report.warn(f"handoff date is {-age} days in the future")
        else:
            report.ok(f"handoff age is {age} day(s)")

    plan = text(PLAN)
    revision_match = re.search(r"\*\*Revision\s+([0-9.]+)\s+—", plan)
    if not revision_match:
        report.fail("active plan revision could not be parsed")
    else:
        plan_revision = revision_match.group(1)
        handoff_revision = re.search(
            r"Active Phase 5 plan:.*?revision\s+([0-9.]+)", handoff, re.S
        )
        if not handoff_revision:
            report.fail("handoff active-plan revision could not be parsed")
        elif handoff_revision.group(1) != plan_revision:
            report.fail(
                "handoff plan revision is stale: "
                f"{handoff_revision.group(1)} != {plan_revision}"
            )
        else:
            report.ok(f"handoff matches active plan revision {plan_revision}")

    actual_hash = hashlib.sha256(PLAN.read_bytes()).hexdigest()
    handoff_hashes = re.findall(r"\b[0-9a-f]{64}\b", handoff)
    if actual_hash not in handoff_hashes:
        report.fail(
            "handoff does not contain the active plan SHA-256 "
            f"{actual_hash}"
        )
    else:
        report.ok(f"handoff matches active plan SHA-256 {actual_hash[:12]}…")

    claude = text(ROOT / "CLAUDE.md")
    stale_phrases = (
        "Only `ML/ML-03.mdx` exists",
        "scripts/validate/` — quality-check scripts (Phase 4+, none yet)",
        "Content schema (to be finalized in Phase 2)",
    )
    found_stale = [phrase for phrase in stale_phrases if phrase in claude]
    if found_stale:
        for phrase in found_stale:
            report.fail(f"CLAUDE.md retains stale startup claim: {phrase}")
    else:
        report.ok("known stale CLAUDE.md startup claims are absent")

    overrides = list(ROOT.glob("**/AGENTS.override.md"))
    if overrides:
        report.warn(
            "AGENTS.override.md may supersede the root contract: "
            + ", ".join(relative(path) for path in overrides)
        )
    else:
        report.ok("no repository AGENTS.override.md shadows the root contract")

    project_state = ROOT / "PROJECT_STATE.md"
    if project_state.is_file():
        state_text = text(project_state)
        state_lines = len(state_text.splitlines())
        if state_lines > 250:
            if "HISTORICAL / NOT THE RESUME ENTRY POINT" in state_text:
                report.ok(
                    f"PROJECT_STATE.md is a {state_lines}-line history ledger "
                    "and is explicitly demoted from startup context"
                )
            else:
                report.warn(
                    f"PROJECT_STATE.md is a {state_lines}-line history ledger; "
                    "mark it historical and do not load it as startup context"
                )

    print(
        f"SUMMARY {report.failures} failure(s), {report.warnings} warning(s). "
        "Warnings require judgment but do not fail the check."
    )
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
