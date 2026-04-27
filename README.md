# DSA Patterns in Python (Placement Prep)

Structured DSA prep repo for coding interviews and campus placements (Python 3.11+).

## Goal
- Build fast pattern recognition for interview rounds.
- Keep every solved problem test-backed and type-safe.
- Revise on schedule using `problem_tracker.csv`.

## Tech stack
- `pytest` for correctness
- `ruff` for linting/style
- `mypy` for static typing
- `pre-commit` for local quality gates
- GitHub Actions (`.github/workflows/ci.yml`) for CI

## Quick start
```bash
pip install -r requirements.txt
python -m pytest
python -m ruff check .
python -m mypy .
```

## Pattern status
Solved:
- Arrays: `two_sum.py`
- Backtracking: `subsets.py`
- Binary Search: `binary_search.py`
- Bit Manipulation: `single_number.py`
- Dynamic Programming: `climbing_stairs.py`, `zero_one_knapsack.py`
- Graphs: `number_of_islands.py`
- Greedy: `jump_game.py`
- Hashing: `valid_anagram.py`
- Heap: `kth_largest_element.py`
- Intervals: `merge_intervals.py`
- Linked List: `reverse_linked_list.py`
- Math Geometry: `rotate_image.py`
- Sliding Window: `best_time_to_buy_sell_stock.py`
- Stack: `valid_parentheses.py`
- Trees: `maximum_depth_binary_tree.py`
- Trie: `implement_trie.py`
- Two Pointers: `valid_palindrome.py`

Scaffolded (next to solve):
- `recursion/`
- `strings/`
- `two_heaps/`
- `union_find/`

## Priority next (Striver A2Z aligned)
1. Dynamic Programming: `longest_common_subsequence`
2. Graphs: `topological_sort`, `shortest_path_unweighted_bfs`
3. Two Pointers: `three_sum`
4. Linked List: reverse variants (`reverse_linked_list_ii`, `reverse_k_group`)
5. Two Heaps: `find_median_from_data_stream`
6. Union Find: `redundant_connection`

## Standard solve workflow
1. Create scaffold:
   `python scripts/create_problem.py --pattern <pattern> --problem <problem_name>`
2. Implement `class Solution:` in `<pattern>/<problem_name>.py`
3. Add tests in `tests/<pattern>/test_<problem_name>.py`
4. Run quality suite:
   ```bash
   python -m ruff check .
   python -m mypy .
   python -m pytest
   ```
5. Update `problem_tracker.csv`
6. Review due items:
   `python scripts/revision_queue.py`

## Definition of done (placement-ready)
- Brute force approach documented (if different from optimal)
- Optimal approach implemented with complexity docstring
- Edge cases covered by pytest
- `ruff`, `mypy`, `pytest` all pass
- Problem logged in `problem_tracker.csv`

## Repository layout
```text
<pattern>/
  problem_name.py
  README.md
  __init__.py

tests/<pattern>/
  test_problem_name.py
  __init__.py

scripts/
interview_notes/
problem_tracker.csv
```

## Revision notes
- `interview_notes/pattern_quick_notes.md`
- `interview_notes/revision_system.md`
- `interview_notes/mock_round_checklist.md`
