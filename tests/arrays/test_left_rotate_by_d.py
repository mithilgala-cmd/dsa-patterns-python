from arrays.left_rotate_by_d import Solution


def test_left_rotate_by_d() -> None:
    solution = Solution()
    
    assert solution.solve([1, 2, 3, 4, 5, 6, 7], 2) == [3, 4, 5, 6, 7, 1, 2]
    assert solution.solve([1, 2, 3, 4, 5, 6, 7], 3) == [4, 5, 6, 7, 1, 2, 3]
    assert solution.solve([1, 2, 3], 4) == [2, 3, 1]  # d > n
    assert solution.solve([1, 2, 3], 0) == [1, 2, 3]
    assert solution.solve([], 5) == []
    assert solution.solve([1], 5) == [1]
