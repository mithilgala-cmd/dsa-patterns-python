from basics.reverse_number import Solution


def test_reverse_number_happy_path() -> None:
    solution = Solution()
    assert solution.solution(12345) == 54321


def test_reverse_number_with_trailing_zeros() -> None:
    solution = Solution()
    assert solution.solution(1200) == 21


def test_reverse_number_edge_case_zero() -> None:
    solution = Solution()
    assert solution.solution(0) == 0


def test_reverse_number_negative_value() -> None:
    solution = Solution()
    assert solution.solution(-9070) == -709
