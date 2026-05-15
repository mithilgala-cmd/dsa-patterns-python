from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> int:
        """
        Problem: Remove Duplicates from Sorted Array
        
        Approach:
        Use two pointers: 'i' for the last unique element and 'j' to traverse.
        If arr[j] != arr[i], increment 'i' and update arr[i].

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not arr:
            return 0
            
        i = 0
        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]
        
        return i + 1
