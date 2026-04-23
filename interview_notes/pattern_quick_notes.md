# Pattern Quick Notes

Use this as a fast revision sheet before interviews.

## Arrays
- Default thought: can I reduce nested loops with hashing, prefix sums, or sorting?
- Watch for index boundaries and empty input.
- First optimize target: O(n).

## Hashing
- Use dictionary/set for complement checks and frequencies.
- Watch collisions of logic around duplicate elements.
- Validate key update order carefully.

## Two Pointers
- Best with sorted arrays or palindrome scans.
- Move only one pointer per condition branch.
- Avoid skipping valid candidates by wrong pointer movement.

## Sliding Window
- Define invariant first (window validity condition).
- Expand right; shrink left only when invalid.
- Track answer after each valid state.

## Stack
- Use for matching, monotonic constraints, and undo flow.
- Store indices when distance matters.
- Validate final stack state after traversal.

## Linked List
- Draw pointer movement before coding.
- Use dummy node to simplify edge handling.
- Protect next pointers before rewiring.

## Binary Search
- Use when space is sorted or answer is monotonic.
- Decide boundary policy (leftmost/rightmost).
- Prevent infinite loops with strict pointer updates.

## Trees
- Pick traversal style first: preorder/inorder/postorder/BFS.
- Base case should be explicit for null node.
- Think about recursion depth and iterative alternative.

## Backtracking
- State = path + choice index + constraints.
- Add choice, recurse, undo choice.
- Prune early to cut exponential branches.

## Dynamic Programming
- Define state and transition in one sentence.
- Start with memoized recursion, convert to tabulation.
- Track base cases separately.

## Graphs
- Decide representation: adjacency list or matrix.
- Use visited tracking to avoid cycles.
- For shortest path with weighted edges, use Dijkstra.

## Heap
- Use min-heap for top-k largest; max-heap by negation.
- Keep heap size constrained when possible.
- Analyze push/pop complexity: O(log k) often enough.

## Greedy
- Prove local decision safety with an argument.
- Sort when decision priority matters.
- If proof is unclear, re-check for DP need.

## Intervals
- Sort by start time first.
- Merge when overlap condition is true.
- Preserve non-overlapping segments as-is.

## Trie
- Use for prefix-heavy string queries.
- Each node stores children map and end-of-word flag.
- Complexity scales with word length, not dictionary size.

## Bit Manipulation
- XOR for pair cancellation and parity tricks.
- Use `n & (n - 1)` to clear lowest set bit.
- Confirm signed/unsigned assumptions in shifts.

## Math and Geometry
- Look for invariant or formula before brute force.
- Avoid floating-point error when integer arithmetic works.
- For matrix problems, test odd and even dimensions.
