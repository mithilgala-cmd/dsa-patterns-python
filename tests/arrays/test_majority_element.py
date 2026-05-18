from arrays.majority_element import Solution


def test_majority_element() -> None:
    solution = Solution()
    
    assert solution.solve([3, 2, 3]) == 3
    assert solution.solve([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.solve([1]) == 1
    assert solution.solve([6, 5, 5]) == 5
    assert solution.solve([10, 9, 9, 9, 10]) == 9
