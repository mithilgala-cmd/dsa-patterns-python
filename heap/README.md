# Heap

## Overview
Maintain top-k or min/max priority elements efficiently.

## Pattern signals
- Need repeated min/max extraction
- Need top-k items
- Need running median

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Kth Largest Element in a Stream
- [ ] Last Stone Weight
- [ ] Find Median from Data Stream

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern heap --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
