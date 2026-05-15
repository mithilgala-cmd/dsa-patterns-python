from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> int:
        """
        Problem: Second Largest Element in an Array (without sorting)
        
        Approach:
        Maintain two variables: largest and second_largest.
        Update them as we traverse the array.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if len(arr) < 2:
            return -1
            
        largest = float('-inf')
        second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        
        return int(second_largest) if second_largest != float('-inf') else -1
