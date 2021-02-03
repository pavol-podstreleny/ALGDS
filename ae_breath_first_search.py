from collections import deque 

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(N) time | O(v) space where v is number of verteces
    def breadthFirstSearch(self, array):
        queue = deque([self])
        
        while len(queue) != 0:
            actualItem = queue.popleft()
            array.append(actualItem.name)

            for item in actualItem.children:
                queue.append(item)
        
        return array
    

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeI = Node("I")
nodeJ = Node("J")
nodeK = Node("K")

nodeA.children.append(nodeB)
nodeA.children.append(nodeC)
nodeA.children.append(nodeD)
nodeB.children.append(nodeE)
nodeB.children.append(nodeF)
nodeD.children.append(nodeG)
nodeD.children.append(nodeH)
nodeG.children.append(nodeK)
nodeF.children.append(nodeI)
nodeF.children.append(nodeJ)

print(nodeA.breadthFirstSearch([]))




        

