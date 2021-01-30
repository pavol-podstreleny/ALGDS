# O(n) where n is number of notes | O(N log N) average O(n) worst
def inOrderTraverse(tree, array):
    if tree is None:
        return
    
    inOrderTraverse(tree.left,array)
    array.append(tree.value)
    inOrderTraverse(tree.right,array)
    return array


def preOrderTraverse(tree, array):
    if tree is None:
        return
    
    array.append(tree.value)
    preOrderTraverse(tree.left,array)
    preOrderTraverse(tree.right,array)
    return array

def postOrderTraverse(tree, array):
    if tree is None:
        return
    
    postOrderTraverse(tree.left,array)
    postOrderTraverse(tree.right,array)
    array.append(tree.value)
    return array

class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

node10 = Node(10)
node5 = Node(5)
node15 = Node(15)
node2 = Node(2)
node5b = Node(5)
node1 = Node(1)
node22 = Node(22)

node10.left = node5
node5.left = node2
node5.right = node5b
node2.left = node1
node10.right = node15
node15.right = node22

print(inOrderTraverse(node10,[]))
print(preOrderTraverse(node10,[]))
print(postOrderTraverse(node10,[]))