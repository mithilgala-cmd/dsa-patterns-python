from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Move all Zeroes to the end of the array
        
        Approach:
        Use two pointers. 'j' points to the first zero found.
        Iterate 'i' through the array. If a non-zero is found, swap it with 'j' and increment 'j'.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        j = -1
        n = len(arr)
        
        # Find the first zero
        for i in range(n):
            if arr[i] == 0:
                j = i
                break
                
        # If no zero exists, return
        if j == -1:
            return arr
            
        # Swap non-zeroes with the first available zero position
        for i in range(j + 1, n):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
                
        return arr
