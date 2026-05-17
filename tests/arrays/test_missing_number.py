from arrays.missing_number import Solution


def test_missing_number() -> None:
    solution = Solution()
    
    assert solution.solve([1, 2, 4, 5], 5) == 3
    assert solution.solve([1, 3], 3) == 2
    assert solution.solve([2, 3, 4], 4) == 1
    assert solution.solve([1, 2, 3], 4) == 4
    assert solution.solve([], 1) == 1
