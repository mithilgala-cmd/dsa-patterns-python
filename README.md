# DSA Patterns in Python (Placement 2027)

Python DSA prep repository aligned to Striver A2Z progression.

## Goal
- Follow A2Z in order for interview readiness.
- Keep every solved problem tested and type-safe.
- Track completion in `problem_tracker.csv`.

## Stack
- `pytest`
- `ruff`
- `mypy`
- `pre-commit`
- GitHub Actions (`.github/workflows/ci.yml`)

## Quick start
```bash
pip install -r requirements.txt
python -m ruff check .
python -m mypy .
python -m pytest
```

## Current solved snapshot
- `basics/`: `count_digits.py`, `reverse_number.py`
- `math/`: `palindrome_number.py`
- `arrays/`: `two_sum.py`
- `backtracking/`: `subsets.py`
- `binary_search/`: `binary_search.py`
- `bit_manipulation/`: `single_number.py`
- `dynamic_programming/`: `climbing_stairs.py`, `zero_one_knapsack.py`
- `graphs/`: `number_of_islands.py`
- `greedy/`: `jump_game.py`
- `hashing/`: `valid_anagram.py`
- `heap/`: `kth_largest_element.py`
- `intervals/`: `merge_intervals.py`
- `linked_list/`: `reverse_linked_list.py`
- `math_geometry/`: `rotate_image.py`
- `sliding_window/`: `best_time_to_buy_sell_stock.py`
- `stack/`: `valid_parentheses.py`
- `trees/`: `maximum_depth_binary_tree.py`
- `trie/`: `implement_trie.py`
- `two_pointers/`: `valid_palindrome.py`

## A2Z order currently in use
1. Step 1: `basics/`, `math/`, `recursion/`
2. Step 2: `sorting/`
3. Step 3: `arrays/`
4. Step 4: `binary_search/`
5. Step 5: `strings/`
6. Step 6: `linked_list/`
7. Step 7: `recursion/`
8. Step 8: `bit_manipulation/`
9. Step 9: `stack/`, `queue/`
10. Step 10: `sliding_window/`, `two_pointers/`
11. Step 11: `heap/`
12. Step 12: `greedy/`
13. Step 13: `trees/`
14. Step 14: `bst/`
15. Step 15: `graphs/`
16. Step 16: `dynamic_programming/`
17. Step 17: `trie/`
18. Step 18: `strings/advanced/`

## A2Z folder gaps (still to scaffold)
- `sorting/`
- `queue/`
- `bst/`
- `strings/advanced/`

## Standard solve flow
1. Add problem in A2Z order.
2. Implement under `<pattern>/<problem_name>.py`.
3. Add tests under `tests/<pattern>/test_<problem_name>.py`.
4. Run:
   ```bash
   python -m ruff check .
   python -m mypy .
   python -m pytest
   ```
5. Append solved record in `problem_tracker.csv`.

## Revision notes
- `https://github.com/mithilgala-cmd/dsa-patterns-python/tree/main/interview_notes/pattern_quick_notes.md`
- `https://github.com/mithilgala-cmd/dsa-patterns-python/tree/main/interview_notes/revision_system.md`
- `https://github.com/mithilgala-cmd/dsa-patterns-python/tree/main/interview_notes/mock_round_checklist.md`
