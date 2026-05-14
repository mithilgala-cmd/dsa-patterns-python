from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


class Solution:
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        """
        Reverse a singly linked list.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        previous: ListNode | None = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
