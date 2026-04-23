# Bit Manipulation

## Overview
Use bitwise operations to optimize checks, counting, and state transitions.

## Pattern signals
- Need parity or toggles
- Need compact state encoding
- Need set/unset bit operations

## Complexity habits
- Start with a brute-force baseline and write down its complexity.
- Target O(n) or O(n log n) when possible.
- Note extra memory trade-offs clearly in the solution docstring.

## Starter problems
- [ ] Single Number
- [ ] Number of 1 Bits
- [ ] Counting Bits

## Progress log
| Date | Problem | Difficulty | Status | Notes |
| ---- | ------- | ---------- | ------ | ----- |

## How to add a problem in this folder
1. Run: python scripts/create_problem.py --pattern bit_manipulation --problem your_problem_name
2. Implement Solution.solve() in the generated module.
3. Replace the placeholder test with real test cases.
4. Run python -m pytest from repository root.
