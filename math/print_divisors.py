from typing import Any


class Solution:
    def solve(self, n: int) -> list[int]:
        """
        Problem: Print all Divisors
        Find all divisors of a natural number n.
        
        Approach:
        Iterate from 1 to sqrt(n). If i is a divisor, then n/i is also a divisor.

        Time Complexity: O(sqrt(N))
        Space Complexity: O(sqrt(N)) to store divisors
        """
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i*i != n:
                    divisors.append(n // i)
        
        return sorted(divisors)
