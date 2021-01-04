# O(n) time | O(p) space where p number of [] depths => callstack
def product_sum(numbers, multiplier=1):

    totalSum = 0

    for number in numbers:
        if type(number) is list:
            totalSum += product_sum(number,multiplier + 1)
        else:
            totalSum += number
    
    return multiplier * totalSum


print(product_sum([5,2,[7,-1],3,[6,[-13,8],4]]))
