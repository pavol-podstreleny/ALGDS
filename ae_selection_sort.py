# O(n^2) time | O(1) space
def selectionSort(numbers):

    for i in range(len(numbers)):
        smallestIdx = findSmallestIdx(i,numbers)
        numbers[i],numbers[smallestIdx] = numbers[smallestIdx], numbers[i]
    
    return numbers


def findSmallestIdx(index,numbers):

    smallest = numbers[index]
    smallestIndex = index
    for i in range(index,len(numbers)):
        
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallestIndex = i
    
    return smallestIndex

print(selectionSort([8,5,2,9,5,6,3]))



