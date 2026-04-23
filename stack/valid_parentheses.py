from __future__ import annotations


class Solution:
    def is_valid(self, text: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []

        for char in text:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return not stack
