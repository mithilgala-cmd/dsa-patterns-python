from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Insertion Sort
        
        Algorithm:
        1. Start from the second element (index 1).
        2. Compare it with the elements before it.
        3. Shift elements greater than the current element to the right.
        4. Insert the current element into its correct position.

        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
