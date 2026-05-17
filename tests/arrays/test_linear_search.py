from arrays.linear_search import Solution


def test_linear_search() -> None:
    solution = Solution()
    
    assert solution.solve([1, 2, 3, 4, 5], 3) == 2
    assert solution.solve([5, 4, 3, 2, 1], 5) == 0
    assert solution.solve([1, 2, 3, 4, 5], 6) == -1
    assert solution.solve([], 1) == -1
    assert solution.solve([2, 2, 2], 2) == 0
