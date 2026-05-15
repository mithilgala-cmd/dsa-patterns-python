from arrays.second_largest import Solution


def test_second_largest() -> None:
    solution = Solution()
    
    assert solution.solve([12, 35, 1, 10, 34, 1]) == 34
    assert solution.solve([10, 5, 10]) == 5
    assert solution.solve([10, 10, 10]) == -1
    assert solution.solve([1, 2, 3, 4, 5]) == 4
    assert solution.solve([5, 4, 3, 2, 1]) == 4
    assert solution.solve([10]) == -1
    assert solution.solve([]) == -1
