from binary_search.binary_search import Solution


def test_binary_search_found_and_not_found() -> None:
    solution = Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
