# Binary Search

## Overview
Search on sorted or monotonic answer spaces in O(log n).

## Pattern signals
- Sorted input or monotonic predicate
- Need left or right boundary
- Need minimum feasible answer

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Binary Search
- [ ] Search a 2D Matrix
- [ ] Koko Eating Bananas

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern binary_search --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
