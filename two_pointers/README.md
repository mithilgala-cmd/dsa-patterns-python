# Two Pointers

## Overview
Coordinate two indices to reduce nested loops and scan efficiently.

## Pattern signals
- Input is sorted or can be sorted
- Need pair or triplet constraints
- Need in-place partitioning

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Valid Palindrome
- [ ] 3Sum
- [ ] Container With Most Water

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern two_pointers --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
