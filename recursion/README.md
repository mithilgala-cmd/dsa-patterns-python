# Recursion

## Overview
Pattern set for divide-and-conquer, backtracking, and recursive state transitions.

## Pattern signals
- Problem naturally breaks into smaller self-similar subproblems
- Base case and transition are clear
- Tree-like exploration of choices

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Track recursion depth separately from branching complexity.
- Add memoization when overlapping subproblems appear.

## Starter problems
- [ ] Factorial
- [ ] Reverse String
- [ ] N-th Fibonacci Number

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern recursion --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
