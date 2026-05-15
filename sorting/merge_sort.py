from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Merge Sort
        
        Algorithm:
        1. Divide the array into two halves.
        2. Recursively sort each half.
        3. Merge the two sorted halves.

        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.solve(arr[:mid])
        right = self.solve(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
