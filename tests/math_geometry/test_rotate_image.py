from math_geometry.rotate_image import Solution


def test_rotate_image() -> None:
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
