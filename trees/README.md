# Trees

## Overview
Hierarchical structures solved mainly with DFS or BFS traversal patterns.

## Pattern signals
- Recursive decomposition fits
- Need ancestor/descendant logic
- Need level-wise traversal

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Maximum Depth of Binary Tree
- [ ] Invert Binary Tree
- [ ] Lowest Common Ancestor of a BST

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern trees --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
