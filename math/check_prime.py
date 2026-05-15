from typing import Any


class Solution:
    def solve(self, n: int) -> bool:
        """
        Problem: Check for Prime
        A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

        Approach:
        Check for divisors from 2 to sqrt(n).

        Time Complexity: O(sqrt(N))
        Space Complexity: O(1)
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
            
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True
