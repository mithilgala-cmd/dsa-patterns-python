from heap.kth_largest_element import Solution


def test_find_kth_largest() -> None:
    solution = Solution()
    assert solution.find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert solution.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
