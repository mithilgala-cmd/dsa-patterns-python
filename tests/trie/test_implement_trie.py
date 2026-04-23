from trie.implement_trie import Trie


def test_implement_trie() -> None:
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
