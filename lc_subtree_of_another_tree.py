class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:

    def __init__(self):
        self.founded = False
        self.areSame = True


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        potentialNodes = []
        self.findSubTree(s, t.val, potentialNodes)
        if len(potentialNodes) > 0:
            isTrue = False
            for node in potentialNodes:
                isTrue = isTrue or self.dfs(node, t)
            return isTrue

        return False

    def dfs(self, a, b):
        if a is None and b is None:
            return True

        if (a is not None) and (b is None) or (a is None) and (b is not None):
            return False

        leftSide = self.dfs(a.left, b.left)
        rightSide = self.dfs(a.right, b.right)

        return a.val == b.val and leftSide and rightSide

    def findSubTree(self, node, val, result):
        if node is None:
            return

        if node.val == val:
            result.append(node)

        self.findSubTree(node.left, val, result)
        self.findSubTree(node.right, val, result)
