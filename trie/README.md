# Trie

## Overview
Prefix tree for efficient string insert/search/prefix operations.

## Pattern signals
- Need prefix queries
- Need dictionary word filtering
- Need character-by-character branching

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Implement Trie
- [ ] Design Add and Search Words Data Structure
- [ ] Word Search II

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern trie --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
