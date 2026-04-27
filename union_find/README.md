# Union Find

## Overview
Pattern set for dynamic connectivity with disjoint set union (DSU).

## Pattern signals
- Need to merge sets and query if nodes are connected
- Connectivity checks happen repeatedly
- Graph edges processed incrementally

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Use path compression + union by rank/size for near-constant amortized operations.
- Explain parent/rank storage in solution docstring.

## Starter problems
- [ ] Number of Connected Components in an Undirected Graph
- [ ] Redundant Connection
- [ ] Accounts Merge

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern union_find --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
