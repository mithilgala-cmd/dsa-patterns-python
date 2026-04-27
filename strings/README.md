# Strings

## Overview
Pattern set for immutable sequence operations, frequency counting, and substring logic.

## Pattern signals
- Character-level parsing or transformations
- Prefix/suffix or two-pointer substring scans
- Hash-based frequency comparison

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) where one pass or two pointers are possible.
- Keep extra memory trade-offs explicit in the solution docstring.

## Starter problems
- [ ] Valid Anagram
- [ ] Longest Common Prefix
- [ ] String to Integer (atoi)

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern strings --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
