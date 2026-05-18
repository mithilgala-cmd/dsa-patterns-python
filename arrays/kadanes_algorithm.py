from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> int:
        """
        Problem: Kadane's Algorithm (Maximum Subarray Sum)
        Find the contiguous subarray with the largest sum.
        
        Approach:
        Maintain a running sum (current_sum) and a max_sum.
        For each element, add it to current_sum and update max_sum.
        If current_sum drops below 0, reset it to 0 because a negative sum
        will only decrease the total sum of any future subarray.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not arr:
            return 0
            
        max_sum = float('-inf')
        current_sum = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
                
            if current_sum < 0:
                current_sum = 0
                
        return int(max_sum)
