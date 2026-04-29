from __future__ import annotations


class Solution:
    def solution_brute_force(self, first_number: int, second_number: int) -> int:
        """
        Problem: GCD or HCF of Two Numbers
        A2Z Step: Step 1 (Learn the basics)
        Pattern: Math (divisor scan)
        Difficulty: easy
        LeetCode: N/A
        Time: O(min(a, b))  Space: O(1)
        Key insight: Scan all divisors up to min(a, b) and keep the largest common one.
        """
        first_number = abs(first_number)
        second_number = abs(second_number)

        if first_number == 0:
            return second_number
        if second_number == 0:
            return first_number

        limit = min(first_number, second_number)
        greatest_common_divisor = 1

        for divisor in range(1, limit + 1):
            if first_number % divisor == 0 and second_number % divisor == 0:
                greatest_common_divisor = divisor

        return greatest_common_divisor

    def solution(self, first_number: int, second_number: int) -> int:
        """
        Problem: GCD or HCF of Two Numbers
        A2Z Step: Step 1 (Learn the basics)
        Pattern: Math (Euclidean algorithm)
        Difficulty: easy
        LeetCode: 1979 (variant)
        Time: O(log(min(a, b)))  Space: O(1)
        Key insight: gcd(a, b) = gcd(b, a % b) shrinks numbers fast to the final divisor.
        """
        first_number = abs(first_number)
        second_number = abs(second_number)

        while second_number != 0:
            first_number, second_number = second_number, first_number % second_number

        return first_number
