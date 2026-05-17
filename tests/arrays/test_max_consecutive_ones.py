from arrays.max_consecutive_ones import Solution


def test_max_consecutive_ones() -> None:
    solution = Solution()
    
    assert solution.solve([1, 1, 0, 1, 1, 1]) == 3
    assert solution.solve([1, 0, 1, 1, 0, 1]) == 2
    assert solution.solve([0, 0, 0]) == 0
    assert solution.solve([1, 1, 1, 1]) == 4
    assert solution.solve([]) == 0
    assert solution.solve([0]) == 0
    assert solution.solve([1]) == 1
