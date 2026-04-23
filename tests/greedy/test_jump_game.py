from greedy.jump_game import Solution


def test_jump_game() -> None:
    solution = Solution()
    assert solution.can_jump([2, 3, 1, 1, 4]) is True
    assert solution.can_jump([3, 2, 1, 0, 4]) is False
