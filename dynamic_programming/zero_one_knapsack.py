from __future__ import annotations


class Solution:
    @staticmethod
    def _validate_inputs(weights: list[int], values: list[int], capacity: int) -> None:
        if len(weights) != len(values):
            raise ValueError("weights and values must have the same length")
        if capacity < 0:
            raise ValueError("capacity must be non-negative")

    def solve_brute_force(self, weights: list[int], values: list[int], capacity: int) -> int:
        """
        Problem: 0/1 Knapsack
        Pattern: Dynamic Programming
        Difficulty: medium

        Time Complexity: O(2^n)
        Space Complexity: O(n)

        Key insight: At each item, branch into skip/take and keep the best valid value.
        """
        self._validate_inputs(weights, values, capacity)
        total_items = len(weights)

        def dfs(index: int, remaining_capacity: int) -> int:
            if index == total_items or remaining_capacity == 0:
                return 0

            skip_value = dfs(index + 1, remaining_capacity)
            if weights[index] > remaining_capacity:
                return skip_value

            take_value = values[index] + dfs(index + 1, remaining_capacity - weights[index])
            return max(skip_value, take_value)

        return dfs(0, capacity)

    def solve(self, weights: list[int], values: list[int], capacity: int) -> int:
        """
        Problem: 0/1 Knapsack
        Pattern: Dynamic Programming
        Difficulty: medium

        Time Complexity: O(n * capacity)
        Space Complexity: O(capacity)

        Key insight: 1D DP updated right-to-left enforces 0/1 usage of each item.
        """
        self._validate_inputs(weights, values, capacity)
        if not weights or capacity == 0:
            return 0

        best_value = [0] * (capacity + 1)

        for index, weight in enumerate(weights):
            value = values[index]
            # Right-to-left keeps previous row states intact for this iteration.
            for current_capacity in range(capacity, weight - 1, -1):
                best_value[current_capacity] = max(
                    best_value[current_capacity],
                    value + best_value[current_capacity - weight],
                )

        # Pattern note: Include or exclude each item once; DP stores best value per capacity.
        return best_value[capacity]
