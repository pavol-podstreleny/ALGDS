# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))


def validateBSTHelper(tree, mininum, maximum):

    if tree is None:
        return True

    if tree.value >= mininum and tree.value < maximum:
        return validateBSTHelper(tree.left, mininum, tree.value) and validateBSTHelper(tree.right, tree.value, maximum)
    else:
        return False
