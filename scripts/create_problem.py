"""Scaffold a new DSA problem module and test file."""

from __future__ import annotations

import argparse
from pathlib import Path

VALID_PATTERNS = {
    "basics",
    "arrays",
    "backtracking",
    "binary_search",
    "bit_manipulation",
    "dynamic_programming",
    "graphs",
    "greedy",
    "hashing",
    "heap",
    "intervals",
    "linked_list",
    "math",
    "math_geometry",
    "recursion",
    "sliding_window",
    "stack",
    "strings",
    "trees",
    "trie",
    "two_heaps",
    "two_pointers",
    "union_find",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create problem and test scaffolding")
    parser.add_argument("--pattern", required=True, help="Pattern folder name")
    parser.add_argument("--problem", required=True, help="Problem file name in snake_case")
    return parser.parse_args()


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        print(f"Skip existing file: {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"Created: {path}")


def main() -> None:
    args = parse_args()
    pattern = args.pattern.strip()
    problem = args.problem.strip()

    if pattern not in VALID_PATTERNS:
        raise ValueError(
            f"Unknown pattern '{pattern}'. Choose one of: {', '.join(sorted(VALID_PATTERNS))}"
        )

    if not problem.isidentifier():
        raise ValueError("Problem name must be a valid snake_case identifier")

    repo_root = Path(__file__).resolve().parents[1]
    problem_path = repo_root / pattern / f"{problem}.py"
    test_dir = repo_root / "tests" / pattern
    test_path = test_dir / f"test_{problem}.py"

    test_dir.mkdir(parents=True, exist_ok=True)

    module_content = (
        "from typing import Any\n\n\n"
        "class Solution:\n"
        "    def solve(self, *args: Any, **kwargs: Any) -> Any:\n"
        '        """Describe the problem and complexity here."""\n'
        '        raise NotImplementedError("Implement solve()")\n'
    )

    if pattern == "math":
        test_content = (
            "from importlib.util import module_from_spec, spec_from_file_location\n"
            "from pathlib import Path\n\n\n"
            "def load_solution_class() -> type:\n"
            "    module_path = (\n"
            f'        Path(__file__).resolve().parents[2] / "{pattern}" / "{problem}.py"\n'
            "    )\n"
            f'    spec = spec_from_file_location("a2z_{pattern}_{problem}", module_path)\n'
            "    if spec is None or spec.loader is None:\n"
            '        raise ImportError(f"Unable to load module from {module_path}")\n'
            "    module = module_from_spec(spec)\n"
            "    spec.loader.exec_module(module)\n"
            "    return module.Solution\n\n\n"
            "Solution = load_solution_class()\n\n\n"
            f"def test_{problem}_placeholder() -> None:\n"
            '    """Replace this with real test cases."""\n'
            "    solution = Solution()\n"
            '    assert hasattr(solution, "solve")\n'
        )
    else:
        test_content = (
            f"from {pattern}.{problem} import Solution\n\n\n"
            f"def test_{problem}_placeholder() -> None:\n"
            '    """Replace this with real test cases."""\n'
            "    solution = Solution()\n"
            '    assert hasattr(solution, "solve")\n'
        )

    write_if_missing(problem_path, module_content)
    write_if_missing(test_path, test_content)


if __name__ == "__main__":
    main()
