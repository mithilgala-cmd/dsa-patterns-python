from backtracking.subsets import Solution


def test_subsets() -> None:
    solution = Solution()
    output = solution.subsets([1, 2])
    normalized = sorted(sorted(item) for item in output)
    assert normalized == [[], [1], [1, 2], [2]]
