# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.preOrderTraversal(root, root.val)

    def preOrderTraversal(self, node, value):
        if node is None:
            return True

        return node.val == value and self.preOrderTraversal(node.left, value) and self.preOrderTraversal(node.right, value)
