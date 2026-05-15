from arrays.check_sorted import Solution


def test_check_sorted() -> None:
    solution = Solution()
    
    assert solution.solve([10, 20, 30, 40, 50]) is True
    assert solution.solve([90, 80, 100]) is False
    assert solution.solve([1, 2, 2, 3]) is True
    assert solution.solve([1]) is True
    assert solution.solve([]) is True
    assert solution.solve([1, 2, 3, 2, 4]) is False
