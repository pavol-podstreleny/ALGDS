# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):

    stackOne = list()
    node = linkedListOne
    transformLinkedListIntoStack(stackOne, node)

    stackTwo = list()
    node = linkedListTwo
    transformLinkedListIntoStack(stackTwo, node)

    numberOne = transformStackIntoNumber(stackOne)
    numberTwo = transformStackIntoNumber(stackTwo)

    finalNumber = numberOne + numberTwo
    return transformNumberIntoLinkedList(finalNumber)


def transformNumberIntoLinkedList(number):

    headNode = LinkedList(0)

    if number == 0:
        return headNode

    node = headNode

    while number != 0:
        numberWithoutRemainder = (number // 10) * 10
        remainder = number - numberWithoutRemainder
        actualNode = LinkedList(remainder)
        node.next = actualNode
        node = actualNode
        number = number // 10

    return headNode.next


def transformStackIntoNumber(stack):
    transferedNumber = 0
    while len(stack) != 0:
        actualLength = len(stack) - 1
        actualNumber = stack.pop()
        transferedNumber += (actualNumber * 10 ** actualLength)

    return transferedNumber


def transformLinkedListIntoStack(stack, node):
    while node:
        stack.append(node.value)
        node = node.next
