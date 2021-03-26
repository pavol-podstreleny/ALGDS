def minHeightBst(array):
    return minHeightBstHelper(array, None, True)


def minHeightBstHelper(array, head, isLeft):
    if len(array) == 0:
        return

    if len(array) == 1:
        node = BST(array[0])
        if head is None:
            return node
        if isLeft:
            head.left = node
        else:
            head.right = node

        return node

    left = 0
    right = len(array) - 1
    middle = (left + right) // 2
    node = BST(array[middle])

    node.left = minHeightBstHelper(array[:middle], node, True)
    node.right = minHeightBstHelper(array[middle+1:], node, False)

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
