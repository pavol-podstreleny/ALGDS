# O(n) time | O(n) space
def sortedSquaredArray(array):
    sorted_array = list()

    # Check if array contains negative numbers
    firstNumber, lastNumber = array[0], array[-1]

    if firstNumber >= 0:
        # we have just positive numbers
        for number in array:
            sorted_array.append(number ** 2)

        return sorted_array

    if lastNumber < 0:
        # We have just negative numbers
        for number in reversed(array):
            sorted_array.append(number ** 2)

        return sorted_array

    # We have both negative and positive
    positiveIndex = findFirstPositive(array)
    negativePointer = positiveIndex - 1
    positivePointer = positiveIndex

    while negativePointer >= 0 and positivePointer < len(array):
        if array[negativePointer] ** 2 <= array[positivePointer] ** 2:
            sorted_array.append(array[negativePointer] ** 2)
            negativePointer -= 1
        else:
            sorted_array.append(array[positivePointer] ** 2)
            positivePointer += 1

    while negativePointer != -1:
        sorted_array.append(array[negativePointer] ** 2)
        negativePointer -= 1

    while positivePointer != len(array):
        sorted_array.append(array[positivePointer] ** 2)
        positivePointer += 1

    return sorted_array


def findFirstPositive(array):
    for i in range(len(array)):
        if array[i] >= 0:
            return i

    return None


print(sortedSquaredArray([1, 2, 3, 4, 5]))
print(sortedSquaredArray([-5, -4, -3, -2]))
print(sortedSquaredArray([-5, -3, -1, 0, 1, 2, 3, 4, 5]))
