# Math and Geometry

## Overview
Use numeric properties and geometric invariants to simplify computation.

## Pattern signals
- Need formula-based optimization
- Need matrix traversal logic
- Need coordinate transformations

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [x] Rotate Image
- [ ] Spiral Matrix
- [ ] Pow(x, n)

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern math_geometry --problem your_problem_name
2. Implement `class Solution` method(s) in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
