def binary_search(numbers,target):

    leftPointer = 0
    rightPointer = len(numbers) -1

    while leftPointer <= rightPointer:
        middle = (leftPointer + rightPointer) // 2

        if numbers[middle] == target:
            return middle

        if numbers[middle] > target:
            rightPointer = middle - 1
        else:
            leftPointer = middle + 1

    return - 1



print(binary_search([0,1,21,33,45,61,71,72,73],33))
