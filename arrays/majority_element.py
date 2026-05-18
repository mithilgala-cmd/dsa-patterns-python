from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> int:
        """
        Problem: Majority Element
        Find the element that appears more than N/2 times.
        
        Approach: Moore's Voting Algorithm
        Initialize a candidate and a count.
        Iterate through the array. If count is 0, pick the current element as candidate.
        If the current element matches the candidate, increment count. Otherwise, decrement.
        The problem assumes a majority element always exists.

        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        candidate = -1
        count = 0
        
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
