from __future__ import annotations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(index: int) -> None:
            if index == len(nums):
                result.append(path.copy())
                return

            path.append(nums[index])
            dfs(index + 1)
            path.pop()

            dfs(index + 1)

        dfs(0)
        return result
