from __future__ import annotations


class Solution:
    def solution(self, number: int) -> int:
        """
        Problem: Reverse Number
        A2Z Step: Step 1 (Learn the basics)
        Pattern: Math (digit construction)
        Difficulty: easy
        LeetCode: 7 (variant)
        Time: O(log10(n))  Space: O(1)
        Key insight: Build reversed value by shifting result left (x10), then append last digit.
        """
        sign = -1 if number < 0 else 1
        number = abs(number)

        reversed_number = 0
        while number > 0:
            reversed_number = (reversed_number * 10) + (number % 10)
            number //= 10

        return sign * reversed_number
