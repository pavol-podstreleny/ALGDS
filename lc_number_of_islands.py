class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visitedMatrix = [[False for item in row] for row in grid]

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visitedMatrix[i][j]:
                    result = self.visitPoint(grid, visitedMatrix, i, j)
                    if result > 0:
                        counter += 1

        return counter

    def visitPoint(self, grid, visitedMatrix, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0

        if visitedMatrix[i][j]:
            return 0

        visitedMatrix[i][j] = True

        if grid[i][j] == "1":
            leftSum = self.visitPoint(grid, visitedMatrix, i, j-1)
            rightSum = self.visitPoint(grid, visitedMatrix, i, j+1)
            bottomSum = self.visitPoint(grid, visitedMatrix, i+1, j)
            topSum = self.visitPoint(grid, visitedMatrix, i-1, j)
            return 1 + leftSum + rightSum + bottomSum + topSum

        return 0
