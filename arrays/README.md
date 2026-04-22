# Arrays

## Overview
Linear collections accessed by index. Core base for many interview problems.

## Pattern signals
- Need fast index access
- Need prefix/suffix preprocessing
- Need subarray reasoning

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Two Sum
- [ ] Contains Duplicate
- [ ] Product of Array Except Self

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern arrays --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
