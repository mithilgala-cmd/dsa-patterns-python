from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> int:
        """
        Problem: Max Consecutive Ones
        Find the maximum number of consecutive 1s in a binary array.
        
        Approach:
        Maintain a count of current consecutive 1s and a max count.
        Reset current count when encountering a 0.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        max_ones = 0
        current_ones = 0
        
        for num in arr:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0
                
        return max_ones
