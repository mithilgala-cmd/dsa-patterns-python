from arrays.rearrange_by_sign import Solution


def test_rearrange_by_sign() -> None:
    solution = Solution()
    
    assert solution.solve([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
    assert solution.solve([-1, 1]) == [1, -1]
    assert solution.solve([1, -1, 2, -2]) == [1, -1, 2, -2]
    assert solution.solve([-2, -3, 1, 4]) == [1, -2, 4, -3]
    assert solution.solve([]) == []
