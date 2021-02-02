class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):

    node = linkedList

    while node and node.next:
        nextNode = node.next
        while nextNode and node.value == nextNode.value:
            nextNode = nextNode.next
        

        node.next = nextNode
        node = node.next
    
    return linkedList
        
    

def printList(node):
    while node:
        print(node.value)
        node = node.next
    


node1 = LinkedList(1)
node1a = LinkedList(1)
node3 = LinkedList(3)
node4 = LinkedList(4)
node4a = LinkedList(4)
node4b  = LinkedList(4)
node5 = LinkedList(5)
node6 = LinkedList(6)
node6a = LinkedList(6)

node1.next = node1a
node1a.next = node3
node3.next = node4
node4.next = node4a
node4a.next = node4b
node4b.next = node5
node5.next = node6
node6.next = node6a

printList(removeDuplicatesFromLinkedList(node1))





