from __future__ import annotations


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        size = len(matrix)

        for row in range(size):
            for col in range(row + 1, size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for current_row in matrix:
            current_row.reverse()
