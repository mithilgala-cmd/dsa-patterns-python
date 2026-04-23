from __future__ import annotations


class Solution:
    def single_number(self, nums: list[int]) -> int:
        value = 0
        for number in nums:
            value ^= number
        return value
