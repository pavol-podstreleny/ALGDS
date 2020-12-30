class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(tree):
    results = []
    branchSumRec(tree,results,0)
    return results

def branchSumRec(tree,result,accumulator):

    if tree.left is None and tree.right is None:
        result.append(tree.value + accumulator)

    if tree.left:
        branchSumRec(tree.left,result, accumulator + tree.value)
    if tree.right:
        branchSumRec(tree.right,result, accumulator + tree.value)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left =node6
node3.right = node7
node4.left = node8
node4.right = node9
node5.left = node10


print(branchSum(node1))