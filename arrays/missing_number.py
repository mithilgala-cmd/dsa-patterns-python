from typing import Any


class Solution:
    def solve(self, arr: list[int], n: int) -> int:
        """
        Problem: Find the missing number in an array
        Given an array of size N-1 containing distinct integers in the range [1, N].
        Find the missing number.
        
        Approach:
        Calculate the expected sum of first N natural numbers.
        Subtract the actual sum of the array from the expected sum.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(arr)
        
        return expected_sum - actual_sum
