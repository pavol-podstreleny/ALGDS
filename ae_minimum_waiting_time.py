# O(N Log N) time | O(1) space
def minimumWaitingTime(queries):

    # Find the largest
    # Remove it from list
    # Sort list
    # Add Values Incrementally

    totalSum = 0
    queries.sort()
    queries = queries[:-1]

    prevValue = 0
    for value in queries:
        prevValue += value
        totalSum += prevValue
    
    return totalSum


print(minimumWaitingTime([3,2,1,2,6]))

    



