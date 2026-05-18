from typing import Any


class Solution:
    def solve(self, arr: list[int]) -> list[int]:
        """
        Problem: Rearrange Array Elements by Sign
        Given an array of even length with an equal number of positive and negative integers.
        Rearrange them such that every consecutive pair has opposite signs.
        
        Approach:
        Use two indices, one for positive numbers (starts at 0) and one for negative (starts at 1).
        Iterate through the array and place elements in a new result array at their corresponding indices.
        Increment the respective index by 2 after placement.

        Time Complexity: O(N)
        Space Complexity: O(N) for the result array
        """
        n = len(arr)
        result = [0] * n
        pos_idx = 0
        neg_idx = 1
        
        for num in arr:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2
                
        return result
