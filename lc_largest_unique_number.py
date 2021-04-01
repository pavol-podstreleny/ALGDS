# O(n) time | O(n) space
def largestIntegerOccuringOnce(array):

    numberMap = dict()

    for number in array:
        if number in numberMap:
            numberMap[number] = False
        else:
            numberMap[number] = True

    largestKey = -1
    for key, value in numberMap.items():
        if value and key > largestKey:
            largestKey = key

    return largestKey


print(largestIntegerOccuringOnce([5, 7, 3, 9, 4, 9, 8, 3, 1]))
print(largestIntegerOccuringOnce([9, 9, 8, 8]))
