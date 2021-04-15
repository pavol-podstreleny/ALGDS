class Solution:
    # O(N) time | O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        leftPointer = 0
        rightPointer = len(numbers) - 1

        result = [-1, -1]
        while leftPointer < rightPointer:
            leftNumber = numbers[leftPointer]
            rightNumber = numbers[rightPointer]
            total = leftNumber + rightNumber

            if total == target:
                result = [leftPointer+1, rightPointer+1]
                break
            elif total > target:
                rightPointer -= 1
            else:
                leftPointer += 1

        return result
