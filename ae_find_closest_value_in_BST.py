class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree,target):
    result = [float('inf')]
    findClosestValueInBST(tree,target,result)
    return result[0]

# O(log N) average time | O(N) worst case -> not balanced BST 
def findClosestValueInBST(tree, target, closest):

    if abs(closest[0] - target) > abs(tree.value - target):
        closest[0] = tree.value

    if tree.value > target:
        if tree.left:
            findClosestValueInBST(tree.left,target,closest)
    elif tree.value == target:
        closest[0] = tree.value
    else:
        if tree.right:
            findClosestValueInBST(tree.right,target,closest)

node10 = Node(10)
node5 = Node(5)
node2 = Node(2)
node1 = Node(1)
node5b = Node(5)
node15 = Node(15)
node13 = Node(13)
node22 = Node(22)
node14 = Node(14)

node10.left = node5
node10.right = node15
node5.left = node2
node5.right = node5b
node15.left = node13
node15.right = node22
node2.left = node1
node13.right = node14

print(findClosestValueInBst(node10,12))