# DSA Patterns in Python

Pattern-first interview preparation repository for Data Structures and Algorithms in Python.

## Placement-ready stack
- `pytest` for correctness
- `ruff` for lint + formatting
- `mypy` for type safety
- `pre-commit` for local quality gates
- GitHub Actions CI for push/PR validation

## Quick start
```bash
pip install -r requirements.txt
python -m pytest
python -m ruff check .
python -m mypy .
```

## Daily workflow
1. Pick a pattern and one problem.
2. Solve in the pattern folder.
3. Add or update tests in `tests/<pattern>/`.
4. Run quality checks.
5. Log result in `problem_tracker.csv`.
6. Revisit due problems from `python scripts/revision_queue.py`.

## Commands
```bash
# Generate new problem + test files
python scripts/create_problem.py --pattern arrays --problem contains_duplicate

# Show due revisions
python scripts/revision_queue.py

# Run full local quality suite
python -m ruff check .
python -m ruff format --check .
python -m mypy .
python -m pytest
```

## Repo structure
```text
arrays/
backtracking/
binary_search/
bit_manipulation/
dynamic_programming/
graphs/
greedy/
hashing/
heap/
intervals/
linked_list/
math_geometry/
recursion/
sliding_window/
stack/
strings/
trees/
trie/
two_heaps/
two_pointers/
union_find/

interview_notes/
scripts/
tests/
problem_tracker.csv
```

## Solved starter set
Each pattern now has at least one solved starter problem with tests.

- Arrays: `two_sum.py`
- Backtracking: `subsets.py`
- Binary Search: `binary_search.py`
- Bit Manipulation: `single_number.py`
- Dynamic Programming: `climbing_stairs.py`
- Graphs: `number_of_islands.py`
- Greedy: `jump_game.py`
- Hashing: `valid_anagram.py`
- Heap: `kth_largest_element.py`
- Intervals: `merge_intervals.py`
- Linked List: `reverse_linked_list.py`
- Math and Geometry: `rotate_image.py`
- Recursion: folder scaffolded
- Sliding Window: `best_time_to_buy_sell_stock.py`
- Stack: `valid_parentheses.py`
- Strings: folder scaffolded
- Trees: `maximum_depth_binary_tree.py`
- Trie: `implement_trie.py`
- Two Heaps: folder scaffolded
- Two Pointers: `valid_palindrome.py`
- Union Find: folder scaffolded

## Placement notes
- Fast revision notes: `interview_notes/pattern_quick_notes.md`
- Revision schedule: `interview_notes/revision_system.md`
- Mock practice template: `interview_notes/mock_round_checklist.md`

## CI
Workflow file: `.github/workflows/ci.yml`
- Triggered on push to `main` and on pull requests.
- Runs lint, formatting check, type check, and tests.
