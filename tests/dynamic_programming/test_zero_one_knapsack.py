import pytest
from dynamic_programming.zero_one_knapsack import Solution


def test_zero_one_knapsack_happy_path() -> None:
    solution = Solution()
    assert solution.solve([1, 2, 4, 5], [5, 4, 8, 6], 5) == 13


def test_zero_one_knapsack_edge_cases() -> None:
    solution = Solution()
    assert solution.solve([], [], 10) == 0
    assert solution.solve([1, 2, 3], [10, 20, 30], 0) == 0
    assert solution.solve([6, 7], [30, 40], 5) == 0


def test_zero_one_knapsack_constraint_validation() -> None:
    solution = Solution()
    with pytest.raises(ValueError, match="same length"):
        solution.solve([1], [10, 20], 5)
    with pytest.raises(ValueError, match="non-negative"):
        solution.solve([1], [10], -1)


def test_zero_one_knapsack_brute_force_matches_optimal() -> None:
    solution = Solution()
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 8]
    capacity = 8
    assert solution.solve_brute_force(weights, values, capacity) == solution.solve(
        weights, values, capacity
    )
