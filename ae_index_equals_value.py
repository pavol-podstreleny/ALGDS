# O(log n ) | O(1) space
def indexEqualsValue(array):

    leftPointer = 0
    rightPointer = len(array) - 1
    smallestIndex = -1

    while leftPointer <= rightPointer:
        middleIndex = (leftPointer + rightPointer) // 2

        if middleIndex == array[middleIndex] and middleIndex == 0:
            return 0

        if middleIndex == array[middleIndex] and middleIndex != 0:
            smallestIndex = middleIndex
            rightPointer = middleIndex - 1

        if middleIndex > array[middleIndex]:
            leftPointer = middleIndex + 1
        else:
            rightPointer = middleIndex - 1

    if smallestIndex != -1:
        return smallestIndex

    return -1
