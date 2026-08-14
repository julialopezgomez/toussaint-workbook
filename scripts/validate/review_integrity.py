#!/usr/bin/env python3
"""Read-only structural validator for the evidence-based workbook review.

The review is pinned to a committed baseline, so this script reads module
frontmatter from that git commit rather than from the dirty worktree. It checks
inventory/index/record consistency only. It cannot judge mathematical truth,
source fidelity, pedagogical quality, or whether a finding disposition is wise.
"""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REVIEW_ROOT = ROOT / "docs/review"
INDEX = REVIEW_ROOT / "REVIEW_INDEX.md"
PROTOCOL = REVIEW_ROOT / "REVIEW_PROTOCOL.md"
MODULE_RECORDS = REVIEW_ROOT / "modules"
BLOCK_RECORDS = REVIEW_ROOT / "blocks"

VALID_STATES = {
    "NOT_STARTED",
    "CALIBRATION_DRAFT",
    "HUMAN_REVIEW_PENDING",
    "APPROVED",
    "PLAN_RECONCILIATION_PENDING",
    "RECONCILED_WITH_OPEN_ITEMS",
    "RECONCILED",
}

REQUIRED_MODULE_SECTIONS = (
    "## Verdict",
    "## Rubric scores",
)

REQUIRED_BLOCK_SECTION_PATTERNS = (
    r"^## Block verdict$",
    r"^## Module disposition$",
    r"^## Source and objective completeness$",
    r"^## Exercises, retrieval, and milestone$",
    r"^## Phase 5 reconciliation$",
    r"^## Batched owner approval$",
)


@dataclass(frozen=True)
class Module:
    block: str
    module_id: str
    tier: int
    title: str


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


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def extract_baseline(contents: str) -> str | None:
    match = re.search(r"Baseline:(?: commit)?\s+`([0-9a-f]{40})`", contents)
    if not match:
        match = re.search(r"Committed baseline:\s+`([0-9a-f]{40})`", contents)
    return match.group(1) if match else None


def scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def baseline_modules(baseline: str) -> list[Module]:
    paths = [
        line
        for line in run_git(
            "ls-tree", "-r", "--name-only", baseline, "--", "src/content/course"
        ).splitlines()
        if line.endswith(".mdx")
    ]
    modules: list[Module] = []
    for path in paths:
        contents = run_git("show", f"{baseline}:{path}")
        parts = contents.split("---", 2)
        if len(parts) < 3:
            raise RuntimeError(f"missing frontmatter in {path}")
        frontmatter = parts[1]
        module_id = scalar(frontmatter, "id")
        block = scalar(frontmatter, "block")
        tier = scalar(frontmatter, "tier")
        title = scalar(frontmatter, "title")
        if not all((module_id, block, tier, title)):
            raise RuntimeError(f"incomplete frontmatter identity in {path}")
        modules.append(Module(block, module_id, int(tier), title))
    return sorted(modules, key=lambda module: module.module_id)


def index_inventory(contents: str) -> tuple[dict[str, Module], dict[str, str]]:
    inventory: dict[str, Module] = {}
    states: dict[str, str] = {}
    in_inventory = False
    row_pattern = re.compile(
        r"^\|\s*([^|]+?)\s*\|\s*([A-Z0-9-]+)\s*\|\s*(\d+)\s*\|"
        r"\s*([^|]+?)\s*\|\s*(.+?)\s*\|$"
    )
    for line in contents.splitlines():
        if line == "## Full module inventory":
            in_inventory = True
            continue
        if in_inventory and line.startswith("## "):
            break
        if not in_inventory:
            continue
        match = row_pattern.match(line)
        if not match or match.group(2) == "Module":
            continue
        block, module_id, tier, title, state = match.groups()
        inventory[module_id] = Module(
            block.strip(), module_id, int(tier), title.strip()
        )
        states[module_id] = state.strip()
    return inventory, states


def state_tokens(cell: str) -> set[str]:
    return set(re.findall(r"`([A-Z_]+)`", cell))


def main() -> int:
    report = Report()
    if not INDEX.is_file() or not PROTOCOL.is_file():
        report.fail("review index or protocol is missing")
        return 1

    index_text = INDEX.read_text(encoding="utf-8")
    protocol_text = PROTOCOL.read_text(encoding="utf-8")
    index_baseline = extract_baseline(index_text)
    protocol_baseline = extract_baseline(protocol_text)
    if not index_baseline or not protocol_baseline:
        report.fail("could not parse baseline from review index/protocol")
        return 1
    if index_baseline != protocol_baseline:
        report.fail(
            f"review baseline mismatch: index {index_baseline} != "
            f"protocol {protocol_baseline}"
        )
        return 1
    baseline = index_baseline
    report.ok(f"review index/protocol share baseline {baseline[:12]}…")

    try:
        committed_modules = baseline_modules(baseline)
    except RuntimeError as error:
        report.fail(str(error))
        return 1
    committed = {module.module_id: module for module in committed_modules}
    indexed, states = index_inventory(index_text)

    if not indexed:
        report.fail("no module rows parsed from REVIEW_INDEX.md")
        return 1

    missing_from_index = sorted(set(committed) - set(indexed))
    extra_in_index = sorted(set(indexed) - set(committed))
    for module_id in missing_from_index:
        report.fail(f"baseline module missing from review index: {module_id}")
    for module_id in extra_in_index:
        report.fail(f"review index module absent from baseline: {module_id}")
    if not missing_from_index and not extra_in_index:
        report.ok(f"review index exactly covers {len(committed)} baseline modules")

    for module_id in sorted(set(committed) & set(indexed)):
        expected = committed[module_id]
        actual = indexed[module_id]
        if actual != expected:
            report.fail(
                f"review index metadata drift for {module_id}: "
                f"{actual} != {expected}"
            )
    if all(indexed.get(key) == value for key, value in committed.items()):
        report.ok("review-index block, tier, and title metadata match baseline")

    for module_id, cell in states.items():
        tokens = state_tokens(cell)
        if not tokens:
            report.fail(f"review index has no parseable state for {module_id}")
        unknown = tokens - VALID_STATES
        if unknown:
            report.fail(
                f"review index has unknown state(s) for {module_id}: "
                + ", ".join(sorted(unknown))
            )

    record_paths = sorted(MODULE_RECORDS.glob("*.md"))
    records = {path.stem: path for path in record_paths}
    orphan_records = sorted(set(records) - set(committed))
    for module_id in orphan_records:
        report.fail(f"module review record has no baseline module: {module_id}")

    expected_records = {
        module_id
        for module_id, cell in states.items()
        if "NOT_STARTED" not in state_tokens(cell)
    }
    for module_id in sorted(expected_records - set(records)):
        report.fail(f"started/approved module lacks review record: {module_id}")
    for module_id in sorted(set(records) - expected_records):
        report.fail(f"module review record is indexed as NOT_STARTED: {module_id}")

    for module_id, path in records.items():
        contents = path.read_text(encoding="utf-8")
        if not contents.startswith(f"# {module_id} review"):
            report.fail(f"{path.relative_to(ROOT)} has mismatched title/module ID")
        record_baseline = extract_baseline(contents)
        if record_baseline != baseline:
            report.fail(
                f"{path.relative_to(ROOT)} baseline {record_baseline} != {baseline}"
            )
        for heading in REQUIRED_MODULE_SECTIONS:
            if heading not in contents:
                report.fail(f"{path.relative_to(ROOT)} missing section {heading}")
        if not re.search(r"^## (?:Prioritized findings|Coverage and findings)$", contents, re.M):
            report.fail(f"{path.relative_to(ROOT)} missing findings section")
        if not re.search(r"^## Phase 5 (?:plan )?reconciliation$", contents, re.M):
            report.fail(f"{path.relative_to(ROOT)} missing Phase 5 reconciliation")
    if records and report.failures == 0:
        report.ok(f"{len(records)} module review records are structurally coherent")

    block_paths = sorted(BLOCK_RECORDS.glob("*.md"))
    for path in block_paths:
        block = path.stem
        contents = path.read_text(encoding="utf-8")
        block_baseline = extract_baseline(contents)
        if block_baseline != baseline:
            report.fail(
                f"{path.relative_to(ROOT)} baseline {block_baseline} != {baseline}"
            )
        for pattern in REQUIRED_BLOCK_SECTION_PATTERNS:
            if not re.search(pattern, contents, re.M):
                report.fail(
                    f"{path.relative_to(ROOT)} missing required block-review "
                    f"section matching {pattern}"
                )
        block_modules = {
            module.module_id for module in committed_modules if module.block == block
        }
        missing_records = sorted(block_modules - set(records))
        for module_id in missing_records:
            report.fail(
                f"completed block record {block} lacks module record {module_id}"
            )
        not_started = sorted(
            module_id
            for module_id in block_modules
            if "NOT_STARTED" in state_tokens(states.get(module_id, ""))
        )
        for module_id in not_started:
            report.fail(
                f"completed block record {block} contains NOT_STARTED module "
                f"{module_id}"
            )
    if block_paths and report.failures == 0:
        report.ok(f"{len(block_paths)} block review records have complete module sets")

    print(
        f"SUMMARY {report.failures} failure(s), {report.warnings} warning(s). "
        "This is structural validation, not semantic review."
    )
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
