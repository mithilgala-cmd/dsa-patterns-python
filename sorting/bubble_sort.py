from typing import List


class Solution:
    def solve(self, arr: List[int]) -> List[int]:
        """
        Problem: Bubble Sort
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        for i in range(n - 1, 0, -1):
            did_swap = False
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    did_swap = True
            if not did_swap:
                break
        return arr
