# O(N) time | O(N) space where N is number of items in array
def spiral_traversal(array):

    A = [0,0]
    B = [0,len(array[0])-1]
    C = [len(array)-1,len(array[0])-1]
    D = [len(array)-1,0]

    result = []

    while A[1] <= B[1] and B[0] <= C[0] and C[1] >= D[1] and D[0] >= A[0]:
        for i in range(A[1],B[1]):
            result.append(array[A[0]][i])

        for i in range(B[0],C[0]+1):
            result.append(array[i][B[1]])

        if A[0] == D[0] or D[1] == C[1]:
            return result
        
        for i in range(C[1]-1,D[1],-1):
            result.append(array[C[0]][i])


        for i in range(D[0],A[0],-1):
            result.append(array[i][A[0]])

        A = [A[0] + 1,A[1] + 1]
        B = [B[0] + 1, B[1] - 1]
        C = [C[0] - 1, C[1] - 1]
        D = [D[0] -1, D[1] + 1]

    return result

print(spiral_traversal([
    [1,2,4],
    [5,8,9],
    [10,12,14],
    [18,2,3]
]))

print(spiral_traversal([
    [1],
    [2],
    [3],
    [4]
]))

print(spiral_traversal([
    [1,2],
    [3,4],
    [5,6]
]))
