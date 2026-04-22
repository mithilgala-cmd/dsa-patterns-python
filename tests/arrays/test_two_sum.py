from arrays.two_sum import Solution


def test_two_sum_basic_case() -> None:
    solution = Solution()
    assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]


def test_two_sum_with_duplicates() -> None:
    solution = Solution()
    assert sorted(solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(solution.twoSum([3, 3], 6)) == [0, 1]


def test_two_sum_not_found() -> None:
    solution = Solution()
    assert solution.twoSum([1, 2, 3], 10) == []
