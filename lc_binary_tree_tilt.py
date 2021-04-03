class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:

    def __init__(self, value=0):
        self.value = value


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        info = TreeInfo()
        self.postOrderTraversal(root, info)
        return info.value

    def postOrderTraversal(self, node, info):
        if node is None:
            return 0

        leftTree = self.postOrderTraversal(node.left, info)
        rightTree = self.postOrderTraversal(node.right, info)
        value = node.val
        node.value = abs(leftTree - rightTree)
        info.value += node.value
        return leftTree + rightTree + value
