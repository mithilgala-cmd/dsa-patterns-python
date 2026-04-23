from hashing.valid_anagram import Solution


def test_valid_anagram() -> None:
    solution = Solution()
    assert solution.is_anagram("anagram", "nagaram") is True
    assert solution.is_anagram("rat", "car") is False
