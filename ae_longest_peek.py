# O (N) time | O(p) space where p is number of peeks
def longestPeak(array):

    peeks = findPotentialPeeksIdx(array)

    maxValue = 0
    for index in peeks:
        peekLength = numberOfPointsLowerThanPeek(index,array)
        if peekLength > maxValue:
            maxValue = peekLength
    
    return maxValue


def numberOfPointsLowerThanPeek(peekIndex,array):
    counter = 1
    leftIndex = peekIndex - 1
    rightIndex = peekIndex + 1
    prevLeft = array[peekIndex]
    prevRight = array[peekIndex]

    while leftIndex >= 0:
        if prevLeft > array[leftIndex]:
            counter += 1
            prevLeft = array[leftIndex]
            leftIndex -= 1
            
        else:
            break
    
    while rightIndex < len(array):
        if prevRight > array[rightIndex]:
            counter += 1
            prevRight = array[rightIndex]
            rightIndex += 1
        else:
            break
    
    return counter



def findPotentialPeeksIdx(array):
    
    peeks = []

    for i in range(1,len(array)-1):
        prev = array[i-1]
        actual = array[i]
        nextOne = array[i+1]

        if prev < actual and actual > nextOne:
            peeks.append(i)
    
    return peeks


print(longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))
print(longestPeak([1,4,10,2]))
    
