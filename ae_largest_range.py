# O(N) time | O(N) space
def largestRange(array):

    numbers = dict()

    for number in array:
        numbers[number] = False

    totalLength = 0
    result = [array[0], array[0]]

    for i in range(len(array)):
        number = array[i]
        if numbers[number]:
            continue

        if numbers[number] != True:
            numbers[number] = True

            leftNumber = number - 1
            rightNumber = number + 1

            leftMost = number
            rightMost = number

            while leftNumber in numbers or rightNumber in numbers:
                if leftNumber in numbers:
                    leftMost = leftNumber
                    leftNumber -= 1
                if rightNumber in numbers:
                    rightMost = rightNumber
                    rightNumber += 1

            if abs(rightNumber-1 - leftNumber+1) > totalLength:
                totalLength = abs(rightNumber-1 - leftNumber+1)
                result[0] = leftNumber + 1
                result[1] = rightNumber - 1

    return result
