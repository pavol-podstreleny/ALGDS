class TreeInfo:
    def __init__(self):
        self.parents = []
        self.depth = []


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        info = TreeInfo()
        self.dfs(root, None, 0, x, y, info)
        return info.parents[0] != info.parents[1] and info.depth[0] == info.depth[1]

    def dfs(self, node, parent, depth, x, y, info):
        if node is None:
            return

        if node.val == x or node.val == y:
            info.parents.append(parent)
            info.depth.append(depth)

        self.dfs(node.left, node, depth+1, x, y, info)
        self.dfs(node.right, node, depth+1, x, y, info)
        return
