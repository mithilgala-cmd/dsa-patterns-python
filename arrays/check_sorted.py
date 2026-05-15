from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> bool:
        """
        Problem: Check if the Array is Sorted
        
        Approach:
        Check if every element is less than or equal to the next element.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
