from arrays.move_zeroes import Solution


def test_move_zeroes() -> None:
    solution = Solution()
    
    assert solution.solve([1, 0, 2, 3, 0, 4, 0, 1]) == [1, 2, 3, 4, 1, 0, 0, 0]
    assert solution.solve([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solution.solve([0]) == [0]
    assert solution.solve([1, 2, 3]) == [1, 2, 3]
    assert solution.solve([0, 0, 0]) == [0, 0, 0]
    assert solution.solve([]) == []
