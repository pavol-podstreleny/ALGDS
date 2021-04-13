class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        result = [[1], [1, 1]]

        for i in range(2, rowIndex+1):
            actualList = [1]
            previousList = result[i-1]

            for i in range(len(previousList)-1):
                actualItem = previousList[i]
                nextItem = previousList[i+1]

                actualList.append(actualItem + nextItem)

            actualList.append(1)
            result.append(actualList)

        return result[rowIndex]
