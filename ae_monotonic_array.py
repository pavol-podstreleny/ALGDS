# O(N) time | O(1) space
def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True

    if len(array) == 0:
        return True
	
	prevNumber = array[0]
	
	for number in array:
		isIncreasing = isIncreasing and number <= prevNumber
		isDecreasing = isDecreasing and number >= prevNumber
		prevNumber = number
	
    return isIncreasing or isDecreasing



print(isMonotonic([-1,-5,-10,-1100,-1100,-1101,-1102,-9001]))