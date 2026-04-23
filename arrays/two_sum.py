class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Return indices of two values whose sum equals target.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen: dict[int, int] = {}

        for idx, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], idx]
            seen[value] = idx

        return []
