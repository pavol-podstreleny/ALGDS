class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        self.dfs(root, [], result)
        return result

    def dfs(self, node, actualArray, result):
        if node is None:
            return

        actualArray.append(str(node.val))
        if node.left is None and node.right is None:
            result.append("->".join(actualArray))

        self.dfs(node.left, actualArray, result)
        self.dfs(node.right, actualArray, result)
        actualArray.pop()
        return
