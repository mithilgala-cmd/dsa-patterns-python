from __future__ import annotations


class Solution:
    def climb_stairs(self, steps: int) -> int:
        if steps <= 2:
            return steps

        first = 1
        second = 2
        for _ in range(3, steps + 1):
            first, second = second, first + second
        return second
