# O(N) time | O(1) space
def hasSingleCycle(array):
    totalSum = 0
    for i in range(len(array)):
        totalSum += array[i]
        if totalSum == 0 and i != len(array) - 1:
            return False
	
    return totalSum % len(array) == 0


