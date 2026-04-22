from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of two values whose sum equals target.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen: Dict[int, int] = {}

        for idx, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], idx]
            seen[value] = idx

        return []
