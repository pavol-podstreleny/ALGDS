# O(N) time | O(h) space where h => height of callstack
class Node:

    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

        # Add value
        array.append(self.name)

        for children in self.children:
            children.depthFirstSearch(array)
    
        return array


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeI = Node("I")
nodeJ = Node("J")
nodeG = Node("G")
nodeH = Node("H")
nodeK = Node("K")

nodeA.children.extend([nodeB,nodeC,nodeD])
nodeB.children.extend([nodeE,nodeF])
nodeF.children.extend([nodeI,nodeJ])
nodeD.children.extend([nodeG,nodeH])
nodeG.children.extend([nodeK])

print(nodeA.depthFirstSearch([]))


