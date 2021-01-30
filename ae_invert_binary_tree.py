# O(n) time: n-> number of nodes in tree | O(d) space -> d is height of the tree
def invertBinaryTree(tree):
    if tree is None:
        return
    
    actualTree = tree
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def preOrderTraversal(tree):
    if tree is None:
        return

    print(tree.value)
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node1 = BinaryTree(1)
node3 = BinaryTree(3)
node2 = BinaryTree(2)
node7 = BinaryTree(7)
node6 = BinaryTree(6)
node5 = BinaryTree(5)
node4 = BinaryTree(4)
node9 = BinaryTree(9)
node8 = BinaryTree(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node8
node4.right = node9
node1.right = node3
node3.left = node6
node3.right = node7

invertBinaryTree(node1)
preOrderTraversal(node1)