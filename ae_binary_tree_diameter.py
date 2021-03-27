# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space where n is number of nodes and h is height of the tree
def binaryTreeDiameter(tree):
    result = [0]
    binaryTreeDiameterHelper(tree, result)
    return result[0]


def binaryTreeDiameterHelper(node, maximum):
    if node is None:
        return 0

    leftSum = binaryTreeDiameterHelper(node.left, maximum)
    rightSum = binaryTreeDiameterHelper(node.right, maximum)
    totalSum = leftSum + rightSum

    if totalSum > maximum[0]:
        maximum[0] = totalSum
    return max(leftSum, rightSum) + 1
