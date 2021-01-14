# O(N^2) time | O(N) space 
def threeNumbersSum(numbers,targetSum):

        # Sort the numbers O(N Log N)
        numbers.sort()
        result = []

        for i in range(len(numbers)-2):
            stableNumber = numbers[i]

            leftPointer = i + 1
            rightPointer = len(numbers) - 1

            while leftPointer < rightPointer:
                leftNumber = numbers[leftPointer]
                rightNuber = numbers[rightPointer]

                totalSum = leftNumber + rightNuber + stableNumber

                if totalSum == targetSum:
                    result.append([stableNumber,leftNumber,rightNuber])
                    leftPointer += 1
                    rightPointer -= 1
                elif totalSum > targetSum:
                    rightPointer -= 1
                else:
                    leftPointer += 1
            
        return result


print(threeNumbersSum([12,3,1,2,-6,5,-8,6],0))
                


