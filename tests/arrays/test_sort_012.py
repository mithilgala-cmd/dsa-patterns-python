from arrays.sort_012 import Solution


def test_sort_012() -> None:
    solution = Solution()
    
    assert solution.solve([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert solution.solve([2, 0, 1]) == [0, 1, 2]
    assert solution.solve([0]) == [0]
    assert solution.solve([1]) == [1]
    assert solution.solve([2, 2, 2]) == [2, 2, 2]
    assert solution.solve([]) == []
    assert solution.solve([1, 1, 1, 0, 0, 0, 2, 2, 2]) == [0, 0, 0, 1, 1, 1, 2, 2, 2]
