from __future__ import annotations


class Solution:
    def can_jump(self, nums: list[int]) -> bool:
        farthest = 0
        for idx, jump in enumerate(nums):
            if idx > farthest:
                return False
            farthest = max(farthest, idx + jump)
        return True
