class Solution:
    def solve(self, n: int) -> int:
        """
        Problem: Nth Fibonacci Number
        Time Complexity: O(2^N)
        Space Complexity: O(N)
        """
        if n <= 1:
            return n
        return self.solve(n - 1) + self.solve(n - 2)
