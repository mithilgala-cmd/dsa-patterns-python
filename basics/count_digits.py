from __future__ import annotations


class Solution:
    def solution(self, number: int) -> int:
        """
        Problem: Count Digits in a Number
        A2Z Step: Step 1 (Learn the basics)
        Pattern: Math (digit extraction)
        Difficulty: easy
        LeetCode: N/A
        Time: O(log10(n))  Space: O(1)
        Key insight: Repeated integer division by 10 removes one digit per step.
        """
        number = abs(number)
        if number == 0:
            return 1

        digits_count = 0
        while number > 0:
            digits_count += 1
            number //= 10
        return digits_count
