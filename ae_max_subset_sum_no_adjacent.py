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
