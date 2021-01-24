# O(N) time | O(1) space
def firstDuplicateValue(array):

    for i in range(len(array)):

        index = abs(array[i]) - 1

        if array[index] < 0:
            return index + 1
        else:
            array[index] *= - 1
    
    return -1

print(firstDuplicateValue([2,1,5,2,3,3,4]))
print(firstDuplicateValue([2,1,5,3,3,2,4]))