from pathlib import Path


PATTERNS = [
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
    "math_geometry",
    "sliding_window",
    "stack",
    "trees",
    "trie",
    "two_pointers",
]


def test_pattern_folders_have_readme_and_test_package() -> None:
    repo_root = Path(__file__).resolve().parents[1]

    for pattern in PATTERNS:
        assert (repo_root / pattern / "README.md").exists()
        assert (repo_root / pattern / "__init__.py").exists()
        assert (repo_root / "tests" / pattern / "__init__.py").exists()
