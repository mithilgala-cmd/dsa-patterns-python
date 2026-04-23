from dynamic_programming.climbing_stairs import Solution


def test_climbing_stairs() -> None:
    solution = Solution()
    assert solution.climb_stairs(2) == 2
    assert solution.climb_stairs(5) == 8
