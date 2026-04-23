from bit_manipulation.single_number import Solution


def test_single_number() -> None:
    solution = Solution()
    assert solution.single_number([2, 2, 1]) == 1
    assert solution.single_number([4, 1, 2, 1, 2]) == 4
