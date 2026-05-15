from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Quick Sort
        
        Algorithm:
        1. Pick a pivot (here, the last element).
        2. Partition the array into elements less than pivot and elements greater than pivot.
        3. Recursively sort the partitions.

        Time Complexity: O(N log N) average, O(N^2) worst case
        Space Complexity: O(log N) stack space
        """
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr

    def _quick_sort(self, arr: list[int], low: int, high: int) -> None:
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quick_sort(arr, low, pivot_index - 1)
            self._quick_sort(arr, pivot_index + 1, high)

    def _partition(self, arr: list[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
