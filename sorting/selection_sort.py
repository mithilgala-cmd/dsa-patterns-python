from typing import List


class Solution:
    def solve(self, arr: List[int]) -> List[int]:
        """
        Problem: Selection Sort
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        for i in range(n - 1):
            mini = i
            for j in range(i + 1, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
        return arr
