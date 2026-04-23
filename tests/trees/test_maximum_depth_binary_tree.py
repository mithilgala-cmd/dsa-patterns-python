from trees.maximum_depth_binary_tree import Solution, TreeNode


def test_maximum_depth_binary_tree() -> None:
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.max_depth(root) == 3
