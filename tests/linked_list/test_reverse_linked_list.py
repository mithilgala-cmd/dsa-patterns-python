from linked_list.reverse_linked_list import ListNode, Solution


def build_list(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    values: list[int] = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


def test_reverse_linked_list() -> None:
    solution = Solution()
    original = build_list([1, 2, 3, 4, 5])
    reversed_head = solution.reverse_list(original)
    assert to_list(reversed_head) == [5, 4, 3, 2, 1]
