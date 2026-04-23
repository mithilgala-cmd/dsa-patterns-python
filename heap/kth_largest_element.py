from __future__ import annotations

import heapq


class Solution:
    def find_kth_largest(self, nums: list[int], k: int) -> int:
        heap: list[int] = []

        for value in nums:
            if len(heap) < k:
                heapq.heappush(heap, value)
            elif value > heap[0]:
                heapq.heapreplace(heap, value)

        return heap[0]
