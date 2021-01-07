# O(n^2) time | O(1) space
def insertionSort(numbers):

    for i in range(len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1],numbers[j]
            j -= 1

    return numbers


print(insertionSort([8,5,2,9,5,6,3]))
