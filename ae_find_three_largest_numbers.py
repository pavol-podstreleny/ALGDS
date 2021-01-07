def findThreeLargestNumbers(numbers):

    largestNumbers = [None,None,None]

    for number in numbers:

        if largestNumbers[2] is None or largestNumbers[2] < number:
            swap(largestNumbers,2,number)
        elif largestNumbers[1] is None or largestNumbers[1] < number:
            swap(largestNumbers,1,number)
        elif largestNumbers[0] is None or largestNumbers[0] < number:
            swap(largestNumbers,0,number)

    return largestNumbers


def swap(largestNumbers,index,value):

    counter = 0
    while counter < index:
        largestNumbers[counter] = largestNumbers[counter + 1]
        counter += 1

    largestNumbers[index] = value



print(findThreeLargestNumbers([141,1,17,-7,-17,-27,18,541,8,7,7]))