def kadanesAlgorithm(array):
    max_sum = array[0]
    current_sum = array[0]

    for i in range(1, len(array)):
        number = array[i]
        if current_sum + number < number:
            current_sum = number
        else:
            current_sum += number

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
