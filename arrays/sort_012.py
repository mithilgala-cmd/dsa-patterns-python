from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Sort an array of 0s, 1s, and 2s
        
        Approach: Dutch National Flag Algorithm
        Use three pointers: low, mid, and high.
        - arr[0..low-1] will be 0s
        - arr[low..mid-1] will be 1s
        - arr[high+1..n-1] will be 2s
        Iterate until mid crosses high.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
                
        return arr
