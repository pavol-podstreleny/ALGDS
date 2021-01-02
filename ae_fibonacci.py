# O(N) time | O(1) space
def getNthFibonacci(n):

    if n == 1:
        return 0
    if n == 2:
        return 1

    numbers = [0,1]

    for i in range(3,n+1):
        actualNumber = numbers[0] + numbers[1]
        numbers[0], numbers[1] = numbers[1], actualNumber
    
    return numbers[1]


print(getNthFibonacci(2))
print(getNthFibonacci(6))
    

