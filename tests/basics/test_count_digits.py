from basics.count_digits import Solution


def test_count_digits_happy_path() -> None:
    solution = Solution()
    assert solution.solution(12345) == 5


def test_count_digits_edge_case_zero() -> None:
    solution = Solution()
    assert solution.solution(0) == 1


def test_count_digits_constraint_large_input() -> None:
    solution = Solution()
    assert solution.solution(10**18) == 19


def test_count_digits_negative_input() -> None:
    solution = Solution()
    assert solution.solution(-9876) == 4
