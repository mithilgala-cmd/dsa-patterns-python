from __future__ import annotations


class Solution:
    def num_islands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited: set[tuple[int, int]] = set()

        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] == "0"
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)

        return islands
