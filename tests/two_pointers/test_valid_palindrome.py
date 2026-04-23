from two_pointers.valid_palindrome import Solution


def test_valid_palindrome() -> None:
    solution = Solution()
    assert solution.is_palindrome("A man, a plan, a canal: Panama") is True
    assert solution.is_palindrome("race a car") is False
