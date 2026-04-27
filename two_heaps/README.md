# Two Heaps

## Overview
Pattern set for maintaining streaming median and split-order statistics.

## Pattern signals
- Need fast access to both lower-half max and upper-half min
- Online insertion with balancing constraints
- Median or k-th boundary queried after each update

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Use max-heap + min-heap balancing for O(log n) updates.
- Document heap size invariants in solution docstring.

## Starter problems
- [ ] Find Median from Data Stream
- [ ] Sliding Window Median
- [ ] IPO

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern two_heaps --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
