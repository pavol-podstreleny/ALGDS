# O(n*m) | O(n*m)
def riverSizes(matrix):

    totalVisited = len(matrix) * len(matrix[0])
    visitedMatrix = []
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(False)

        visitedMatrix.append(row)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visitedMatrix[i][j]:
                river = visitPoint(matrix, visitedMatrix, i, j)
                if river > 0:
                    result.append(river)

    return result


def visitPoint(matrix, visitedMatrix, i, j):
    # Check if we are in right coordinates
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0

    if visitedMatrix[i][j]:
        return 0

    visitedMatrix[i][j] = True

    if matrix[i][j] == 1:
        bottomSum = visitPoint(matrix, visitedMatrix, i+1, j)
        upSum = visitPoint(matrix, visitedMatrix, i-1, j)
        leftSum = visitPoint(matrix, visitedMatrix, i, j-1)
        rightSum = visitPoint(matrix, visitedMatrix, i, j+1)
        return 1 + bottomSum + leftSum + rightSum + upSum
    return 0
