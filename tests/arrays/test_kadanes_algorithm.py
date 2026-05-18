from arrays.kadanes_algorithm import Solution


def test_kadanes_algorithm() -> None:
    solution = Solution()
    
    assert solution.solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.solve([1]) == 1
    assert solution.solve([5, 4, -1, 7, 8]) == 23
    assert solution.solve([-1, -2, -3, -4]) == -1
    assert solution.solve([]) == 0
    assert solution.solve([2, -1, 2, 3, 4, -5]) == 10
