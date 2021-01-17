# O(N) time | O(1) space
def moveElementToEnd(array, toMove):

    leftPointer = 0
    rightPointer = len(array) - 1

    while leftPointer < rightPointer:
        rightNumber = array[rightPointer]
        leftNumber = array[leftPointer]

        if rightNumber == toMove:
            rightPointer -= 1
            continue
        
        if leftNumber != toMove:
            leftPointer += 1
            continue
            
        array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
        leftPointer += 1
        rightPointer -= 1

    return array

print(moveElementToEnd([2,1,2,2,2,3,4,2],2))
        

