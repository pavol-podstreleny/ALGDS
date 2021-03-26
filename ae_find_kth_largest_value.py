# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:

    def __init__(self, visited, value):
        self.visited = visited
        self.value = value


def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reversedInOrderTraversal(tree, k, treeInfo)
    return treeInfo.value


def reversedInOrderTraversal(tree, k, treeInfo):

    if tree is None or k == treeInfo.visited:
        return

    reversedInOrderTraversal(tree.right, k, treeInfo)
    if k > treeInfo.visited:
        treeInfo.visited += 1
        treeInfo.value = tree.value
        reversedInOrderTraversal(tree.left, k, treeInfo)
