from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


class Solution:
    def max_depth(self, root: TreeNode | None) -> int:
        """
        Return the maximum depth of a binary tree.
        
        Time Complexity: O(n) - Visit each node once
        Space Complexity: O(h) - Recursive stack depth (h = height)
        """
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
