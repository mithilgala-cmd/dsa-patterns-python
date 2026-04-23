from intervals.merge_intervals import Solution


def test_merge_intervals() -> None:
    solution = Solution()
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
