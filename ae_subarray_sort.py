# O(N) time | O(n) space
def subarraySort(array):

    biggestNumber = float("-inf")
    outOrderMap = dict()

    for i in range(len(array)):
        number = array[i]
        if number >= biggestNumber:
            biggestNumber = number
        else:
            outOrderMap[i] = number

    if len(outOrderMap) == 0:
        return [-1, -1]

    # Find smallest number from outOrderMap
    smallestNumber = float("inf")
    largestIndex = -1
    for index, value in outOrderMap.items():
        if value < smallestNumber:
            smallestNumber = value
        if index > largestIndex:
            largestIndex = index

    for i in range(len(array)):
        if array[i] > smallestNumber:
            return [i, largestIndex]

    return None
