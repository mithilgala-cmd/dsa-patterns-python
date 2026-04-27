# Stack

## Overview
LIFO structure for parsing, monotonic constraints, and undo-style logic.

## Pattern signals
- Need nearest greater/smaller element
- Need balanced symbol checking
- Need function call style backtracking

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [x] Valid Parentheses
- [ ] Min Stack
- [ ] Daily Temperatures

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern stack --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
