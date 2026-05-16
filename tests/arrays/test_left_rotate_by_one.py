from arrays.left_rotate_by_one import Solution


def test_left_rotate_by_one() -> None:
    solution = Solution()
    
    assert solution.solve([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]
    assert solution.solve([3]) == [3]
    assert solution.solve([]) == []
    assert solution.solve([1, 2]) == [2, 1]
    assert solution.solve([7, 7, 7]) == [7, 7, 7]
