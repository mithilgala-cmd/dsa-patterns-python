from typing import Any


class Solution:
    def solve(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        Problem: Union of Two Sorted Arrays
        
        Approach:
        Use two pointers. Compare elements from both arrays.
        Add the smaller element to the union array, ensuring no duplicates are added.
        If elements are equal, add one and increment both pointers.

        Time Complexity: O(N + M)
        Space Complexity: O(N + M) for returning the union array
        """
        n, m = len(arr1), len(arr2)
        i = j = 0
        union = []
        
        while i < n and j < m:
            # Handle duplicates
            while i > 0 and i < n and arr1[i] == arr1[i - 1]:
                i += 1
            while j > 0 and j < m and arr2[j] == arr2[j - 1]:
                j += 1
                
            if i >= n or j >= m:
                break
                
            if arr1[i] < arr2[j]:
                union.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                union.append(arr2[j])
                j += 1
            else:
                union.append(arr1[i])
                i += 1
                j += 1
                
        # Add remaining elements from arr1
        while i < n:
            if i == 0 or arr1[i] != arr1[i - 1]:
                union.append(arr1[i])
            i += 1
            
        # Add remaining elements from arr2
        while j < m:
            if j == 0 or arr2[j] != arr2[j - 1]:
                union.append(arr2[j])
            j += 1
            
        return union
