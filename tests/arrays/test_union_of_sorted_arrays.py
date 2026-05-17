from arrays.union_of_sorted_arrays import Solution


def test_union_of_sorted_arrays() -> None:
    solution = Solution()
    
    assert solution.solve([1, 2, 3, 4, 5], [2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert solution.solve([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert solution.solve([1, 1, 1], [2, 2, 2]) == [1, 2]
    assert solution.solve([], [1, 2, 3]) == [1, 2, 3]
    assert solution.solve([1, 2, 3], []) == [1, 2, 3]
    assert solution.solve([], []) == []
    assert solution.solve([1, 1, 2, 3, 4, 5], [2, 3, 4, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
