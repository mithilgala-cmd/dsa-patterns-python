from typing import Any


class Solution:
    def solve(self, arr: list[int], d: int) -> list[int]:
        """
        Problem: Left Rotate the Array by D places
        
        Approach:
        To rotate left by D elements in-place:
        1. Reverse the first D elements.
        2. Reverse the remaining N-D elements.
        3. Reverse the entire array.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        n = len(arr)
        if n == 0:
            return arr
            
        d = d % n
        if d == 0:
            return arr
            
        def reverse(start: int, end: int) -> None:
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                
        reverse(0, d - 1)
        reverse(d, n - 1)
        reverse(0, n - 1)
        
        return arr
