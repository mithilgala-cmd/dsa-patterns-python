from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Left Rotate the Array by One
        
        Approach:
        Store the first element. Shift all other elements one position to the left.
        Place the stored first element at the last position.
        Modifies the array in-place.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not arr or len(arr) <= 1:
            return arr
            
        first = arr[0]
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
            
        arr[-1] = first
        return arr
