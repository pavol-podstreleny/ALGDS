# O(N) time | O(N) space complexity
def arrayOfProducts(array):

    forward_multiplication = list(range(len(array)))
    backward_multiplication = list(range(len(array)))

    forward_multiplication[0] = 1
    backward_multiplication[-1] = 1

    for i in range(len(array)-1):
        forward_multiplication[i+1] = forward_multiplication[i] * array[i]
    
    for i in range(len(array)-1,0,-1):
        backward_multiplication[i-1] = backward_multiplication[i] * array[i]
    
    result = []

    for i in range(len(forward_multiplication)):
        result.append(forward_multiplication[i] * backward_multiplication[i])
    
    return result

print(arrayOfProducts([5,1,4,2]))

