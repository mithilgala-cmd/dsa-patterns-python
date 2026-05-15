from arrays.largest_element import Solution


def test_largest_element() -> None:
    solution = Solution()
    
    assert solution.solve([1, 8, 7, 56, 90]) == 90
    assert solution.solve([1, 2, 3, 4, 5]) == 5
    assert solution.solve([5, 4, 3, 2, 1]) == 5
    assert solution.solve([-1, -2, -3]) == -1
    assert solution.solve([10]) == 10
