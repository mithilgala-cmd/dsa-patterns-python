# Dynamic Programming

## Overview
Solve overlapping subproblems with memoization or tabulation.

## Pattern signals
- Optimal substructure exists
- Repeated subproblems appear
- Choices depend on previous states

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [x] Climbing Stairs
- [x] 0/1 Knapsack
- [ ] Longest Common Subsequence

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern dynamic_programming --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
