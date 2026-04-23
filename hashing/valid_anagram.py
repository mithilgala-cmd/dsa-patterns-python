from __future__ import annotations


class Solution:
    def is_anagram(self, left: str, right: str) -> bool:
        if len(left) != len(right):
            return False

        counts: dict[str, int] = {}
        for char in left:
            counts[char] = counts.get(char, 0) + 1

        for char in right:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]

        return not counts
