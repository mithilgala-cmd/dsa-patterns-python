# Linked List

## Overview
Pointer-based sequence operations and in-place node manipulation.

## Pattern signals
- Need node rewiring
- Need cycle detection
- Need fast head/tail updates

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [x] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Linked List Cycle

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern linked_list --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
