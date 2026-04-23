# Sliding Window

## Overview
Maintain a dynamic contiguous range with incremental updates.

## Pattern signals
- Need subarray/substring optimization
- Need max/min over moving range
- Need at-most or at-least constraints

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Best Time to Buy and Sell Stock
- [ ] Longest Substring Without Repeating Characters
- [ ] Minimum Window Substring

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern sliding_window --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
