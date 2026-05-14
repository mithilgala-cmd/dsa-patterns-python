class Solution:
    def solve(self, n: int) -> int:
        """
        Problem: Factorial of N
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if n == 0 or n == 1:
            return 1
        return n * self.solve(n - 1)
