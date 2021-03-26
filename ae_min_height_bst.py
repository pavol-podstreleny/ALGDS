def minHeightBst(array):
    return minHeightBstHelper(array, None, True)


def minHeightBst(array):
    return minHeightBstHelper(array)


def minHeightBstHelper(array):
    if len(array) == 0:
        return

    middle = (0 + len(array)-1) // 2
    node = BST(array[middle])
    node.left = minHeightBstHelper(array[:middle])
    node.right = minHeightBstHelper(array[middle+1:])

    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
