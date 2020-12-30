# https://www.algoexpert.io/questions/Two%20Number%20Sum

# O(N) time | O(N) space => N number of items in array
def twoNumberSum(numbers,targetSum):

    numberSet = set()

    for number in numbers:

        if targetSum - number in numberSet:
            return [number,targetSum - number]
        else:
            numberSet.add(number)
    
    return []

# O(N log N) time | O(1) space
def twoNumberSumSort(numbers,targetSum):
    numbers.sort()

    leftPointer = 0
    rightPointer = len(numbers) - 1


    while leftPointer < rightPointer:
        totalSum = numbers[leftPointer] + numbers[rightPointer]
        if totalSum == targetSum:
            return [numbers[leftPointer],numbers[rightPointer]]
        elif totalSum < targetSum:
            leftPointer += 1
        else:
            rightPointer -= 1
    
    return []


print(twoNumberSumSort([],10))
print(twoNumberSumSort([3,5,-4,8,11,1,-1,6],10))
print(twoNumberSum([3,5,-4,8,11,1,-1,6],10))
