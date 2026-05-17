from typing import Any


class Solution:
    def solve(self, arr: list[int], num: int) -> int:
        """
        Problem: Linear Search
        Find the first index of the given number in the array.
        
        Approach:
        Iterate through the array and return the index if the element is found.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        for i in range(len(arr)):
            if arr[i] == num:
                return i
        return -1
