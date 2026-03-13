#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path


DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"


class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    DIM = "\033[2m"


def use_color() -> bool:
    return sys.stdout.isatty() and "NO_COLOR" not in os.environ


def style(text: str, *codes: str) -> str:
    if not use_color():
        return text
    return "".join(codes) + text + Color.RESET


def is_blank(line: str) -> bool:
    return line.strip() == ""


def is_math_delimiter(line: str) -> bool:
    return line.strip() == "$$"


@dataclass
class Change:
    kind: str
    index: int
    reason: str
    line: str = ""
    replacement: str = ""


CONTEXT_LINES = 5
FOUR_BACKSLASHES = "\\" * 4
TWO_BACKSLASHES = "\\" * 2


def collect_changes(lines: list[str]) -> list[Change]:
    changes: list[Change] = []
    in_math_block = False
    i = 0

    while i < len(lines):
        line = lines[i]

        if FOUR_BACKSLASHES in line:
            changes.append(
                Change(
                    kind="replace",
                    index=i,
                    reason="将 \\\\\\\\ 替换为 \\\\",
                    line=line,
                    replacement=line.replace(FOUR_BACKSLASHES, TWO_BACKSLASHES),
                )
            )

        if not is_math_delimiter(line):
            if in_math_block and is_blank(line):
                changes.append(
                    Change(
                        kind="delete",
                        index=i,
                        reason="删除公式块内的空行",
                        line=lines[i],
                    )
                )
            i += 1
            continue

        if not in_math_block:
            if i > 0 and not is_blank(lines[i - 1]):
                changes.append(
                    Change(
                        kind="insert_before",
                        index=i,
                        reason="在公式块前补一个空行",
                        line="\n",
                    )
                )
            in_math_block = True
            i += 1
            continue

        if i + 1 < len(lines) and not is_blank(lines[i + 1]):
            changes.append(
                Change(
                    kind="insert_after",
                    index=i,
                    reason="在公式块后补一个空行",
                    line="\n",
                )
            )
        in_math_block = False
        i += 1

    return changes


def render_line(line: str) -> str:
    text = line.rstrip("\n")
    if text == "":
        return style("<BLANK>", Color.DIM)
    if is_math_delimiter(line):
        return style(text, Color.CYAN, Color.BOLD)
    return text


def print_context(lines: list[str], change: Change) -> None:
    if change.kind == "insert_after":
        anchor = min(change.index + 1, len(lines))
    else:
        anchor = max(change.index, 0)

    start = max(0, anchor - CONTEXT_LINES)
    end = min(len(lines), anchor + CONTEXT_LINES)

    print(style("上下文:", Color.BOLD))
    for idx in range(start, end):
        prefix = " "
        line_text = render_line(lines[idx])

        if change.kind == "delete" and idx == change.index:
            prefix = style("-", Color.RED)
            line_text = style(line_text, Color.RED)
        elif change.kind == "replace" and idx == change.index:
            print(
                f"  {style(f'{idx + 1:>4}', Color.DIM)} "
                f"{style('-', Color.RED)} {style(render_line(change.line), Color.RED)}"
            )
            prefix = style("+", Color.GREEN)
            line_text = style(render_line(change.replacement), Color.GREEN)
        elif change.kind == "insert_before" and idx == change.index:
            inserted = style(render_line(change.line), Color.GREEN)
            print(f"  {style(f'{change.index + 1:>4}', Color.DIM)} {style('+', Color.GREEN)} {inserted}")
            prefix = style("=", Color.CYAN)
        elif change.kind == "insert_after" and idx == change.index:
            prefix = style("=", Color.CYAN)
        elif change.kind == "insert_after" and idx == change.index + 1:
            inserted = style(render_line(change.line), Color.GREEN)
            print(f"  {style(f'{change.index + 2:>4}', Color.DIM)} {style('+', Color.GREEN)} {inserted}")

        print(f"  {style(f'{idx + 1:>4}', Color.DIM)} {prefix} {line_text}")

    if change.kind == "insert_before" and change.index >= len(lines):
        inserted = style(render_line(change.line), Color.GREEN)
        print(f"  {style(f'{change.index + 1:>4}', Color.DIM)} {style('+', Color.GREEN)} {inserted}")
    elif change.kind == "insert_after" and change.index + 1 >= len(lines):
        inserted = style(render_line(change.line), Color.GREEN)
        print(f"  {style(f'{len(lines) + 1:>4}', Color.DIM)} {style('+', Color.GREEN)} {inserted}")


def prompt_for_change(path: Path, lines: list[str], change: Change) -> str:
    line_no = min(change.index + 1, len(lines))
    print(style(f"\n{path.relative_to(DOCS_DIR.parent)}:{line_no}", Color.BOLD))
    print(style(change.reason, Color.YELLOW))
    print_context(lines, change)

    while True:
        answer = input(
            style("应用这个修改? [y]es/[n]o/[a]ll/[q]uit: ", Color.BOLD)
        ).strip().lower()
        if answer in {"y", "n", "a", "q"}:
            return answer


def apply_changes(
    path: Path,
    lines: list[str],
    changes: list[Change],
    auto_apply: bool,
) -> tuple[list[str], int]:
    output = lines[:]
    accepted = 0
    offset = 0
    apply_all = auto_apply

    for change in changes:
        current_index = change.index + offset
        if not apply_all:
            current_change = Change(**{**change.__dict__, "index": current_index})
            decision = prompt_for_change(path, output, current_change)
            if decision == "q":
                raise KeyboardInterrupt
            if decision == "n":
                continue
            if decision == "a":
                apply_all = True

        if change.kind == "delete":
            if 0 <= current_index < len(output) and is_blank(output[current_index]):
                del output[current_index]
                offset -= 1
                accepted += 1
        elif change.kind == "replace":
            if 0 <= current_index < len(output) and FOUR_BACKSLASHES in output[current_index]:
                output[current_index] = output[current_index].replace(
                    FOUR_BACKSLASHES, TWO_BACKSLASHES
                )
                accepted += 1
        elif change.kind == "insert_before":
            output.insert(current_index, "\n")
            offset += 1
            accepted += 1
        elif change.kind == "insert_after":
            output.insert(current_index + 1, "\n")
            offset += 1
            accepted += 1

    return output, accepted


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="规范 docs 目录下 Markdown 公式块的空行。"
    )
    parser.add_argument(
        "-a",
        "--auto-apply",
        action="store_true",
        help="自动应用所有修改，不逐条确认。",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = sorted(DOCS_DIR.rglob("*.md"))
    changed_files = 0
    applied_changes = 0

    try:
        for path in files:
            original = path.read_text(encoding="utf-8").splitlines(keepends=True)
            changes = collect_changes(original)
            if not changes:
                continue

            updated, accepted = apply_changes(
                path, original, changes, args.auto_apply
            )
            if accepted == 0 or updated == original:
                continue

            path.write_text("".join(updated), encoding="utf-8")
            changed_files += 1
            applied_changes += accepted
            print(
                f"{path.relative_to(DOCS_DIR.parent)}: "
                f"{accepted} change(s) applied"
            )
    except KeyboardInterrupt:
        print("\n已中止。")
        return 130

    print(f"完成: 更新了 {changed_files} 个文件，应用了 {applied_changes} 处修改。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
