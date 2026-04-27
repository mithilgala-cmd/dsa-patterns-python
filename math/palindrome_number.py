from __future__ import annotations


class Solution:
    def solution(self, number: int) -> bool:
        """
        Problem: Palindrome Number
        A2Z Step: Step 1 (Learn the basics)
        Pattern: Math (digit reversal)
        Difficulty: easy
        LeetCode: 9
        Time: O(log10(n))  Space: O(1)
        Key insight: Compare original number with its reversed numeric form.
        """
        if number < 0:
            return False

        original_number = number
        reversed_number = 0

        while number > 0:
            reversed_number = (reversed_number * 10) + (number % 10)
            number //= 10

        return original_number == reversed_number
