# DSA Patterns in Python

Pattern-first practice repository for Data Structures and Algorithms in Python.

## Goal
- Build strong interview-ready problem-solving habits.
- Track progress pattern by pattern.
- Keep every solution testable with `pytest`.

## Repository layout
```text
arrays/
backtracking/
binary_search/
bit_manipulation/
dynamic_programming/
graphs/
greedy/
hashing/
heap/
intervals/
linked_list/
math_geometry/
sliding_window/
stack/
trees/
trie/
two_pointers/

tests/
  arrays/
  backtracking/
  ...
```

## Quick start
```bash
pip install -r requirements.txt
python -m pytest
```

## Add a new problem
Use the scaffold script:
```bash
python scripts/create_problem.py --pattern arrays --problem contains_duplicate
```

This command creates:
- `<pattern>/<problem>.py`
- `tests/<pattern>/test_<problem>.py`

## Patterns covered
- [x] [Arrays](./arrays/README.md)
- [x] [Hashing](./hashing/README.md)
- [x] [Two Pointers](./two_pointers/README.md)
- [x] [Sliding Window](./sliding_window/README.md)
- [x] [Stack](./stack/README.md)
- [x] [Linked List](./linked_list/README.md)
- [x] [Binary Search](./binary_search/README.md)
- [x] [Trees](./trees/README.md)
- [x] [Backtracking](./backtracking/README.md)
- [x] [Dynamic Programming](./dynamic_programming/README.md)
- [x] [Graphs](./graphs/README.md)
- [x] [Heap](./heap/README.md)
- [x] [Greedy](./greedy/README.md)
- [x] [Intervals](./intervals/README.md)
- [x] [Trie](./trie/README.md)
- [x] [Bit Manipulation](./bit_manipulation/README.md)
- [x] [Math and Geometry](./math_geometry/README.md)

## Recommended workflow
1. Pick one pattern.
2. Solve 2-3 easy problems, then medium, then hard.
3. Write tests for edge cases immediately.
4. Revisit solved problems after 2-3 days.
5. Track mistakes and recurring tricks in each pattern README.
