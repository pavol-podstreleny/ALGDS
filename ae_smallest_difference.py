# O(N logN) + O(M log M) time | O(1) space
def smallest_difference(array1,array2):

    array1.sort()
    array2.sort()

    arr1Pointer = 0
    arr2Pointer = 0

    difference = float("inf")
    result = [0,0]

    while arr1Pointer < len(array1) and arr2Pointer < len(array2):
        number1 = array1[arr1Pointer]
        number2 = array2[arr2Pointer]

        if number1 == number2:
            return [number1,number2]
        
        actualDifference = abs(number1 - number2)

        if actualDifference < difference:
            result[0] = number1
            result[1] = number2
            difference = actualDifference
        
        if number1 > number2:
            arr2Pointer += 1
        else:
            arr1Pointer += 1
    
    return result



print(smallest_difference(
    [-1,5,10,20,28,3],
    [26,134,135,15,17]))





