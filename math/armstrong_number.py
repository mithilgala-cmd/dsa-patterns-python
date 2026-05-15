from typing import Any


class Solution:
    def solve(self, n: int) -> bool:
        """
        Problem: Armstrong Number
        An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
        Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

        Time Complexity: O(log10(N))
        Space Complexity: O(1)
        """
        if n < 0:
            return False
            
        s = str(n)
        num_digits = len(s)
        total = sum(int(digit) ** num_digits for digit in s)
        return total == n
