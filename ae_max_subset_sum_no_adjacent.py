# O(N) | O(1) space
def maxSubsetSumNoAdjacent(array):
    return max(calculateMaxSubset(array, 0), calculateMaxSubset(array, 1))


def calculateMaxSubset(array, i):
    if i >= len(array):
        return 0

    leftSum = calculateMaxSubset(array, i+2)
    rightSum = calculateMaxSubset(array, i+3)
    maxSum = max(leftSum, rightSum)
    return array[i] + maxSum


def maxSubsetSumNoAdjacentDynamic(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    first = array[0]
    second = max(first, array[1])

    for i in range(2, len(array)):
        current = max(second, first+array[i])
        first = second
        second = current

    return second
