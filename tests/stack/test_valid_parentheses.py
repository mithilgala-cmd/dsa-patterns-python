from stack.valid_parentheses import Solution


def test_valid_parentheses() -> None:
    solution = Solution()
    assert solution.is_valid("()[]{}") is True
    assert solution.is_valid("(]") is False
    assert solution.is_valid("([)]") is False
