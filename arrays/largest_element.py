from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> int:
        """
        Problem: Largest Element in an Array
        
        Approach:
        Iterate through the array and keep track of the maximum element found so far.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not arr:
            raise ValueError("Array cannot be empty")
            
        max_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
        return max_val
