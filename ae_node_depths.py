class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

# O(n) time | O(h) space where h is height => callstack
def node_depths(head,depth=0):

    if head.left is None and head.right is None:
        return depth
    
    if head.left and head.right:
        return depth + node_depths(head.left,depth + 1) + node_depths(head.right,depth+1)

    if head.left:
        return depth + node_depths(head.left,depth+1)
    if head.right:
        return depth + node_depths(head.right,depth+1)
    
node1 = Node(1)
node2 = Node(2)
node4 = Node(4)
node5 = Node(5)
node8 = Node(8)
node9 = Node(9)
node3 = Node(3)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9

print(node_depths(node1))





