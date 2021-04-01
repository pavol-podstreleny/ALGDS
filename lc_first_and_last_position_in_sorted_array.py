class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        leftIndex = 0
        rightIndex = len(nums) - 1
        result = [float("inf"), float("-inf")]

        self.searchTarget(nums, target, leftIndex, rightIndex, result)

        if result[0] == float('inf') and result[1] == float("-inf"):
            return [-1, -1]

        return result

    def searchTarget(self, nums, target, leftIndex, rightIndex, result):

        if leftIndex > rightIndex or (leftIndex < 0) or (rightIndex > len(nums) - 1):
            return

        middleIndex = (leftIndex + rightIndex) // 2

        if nums[middleIndex] == target:
            if middleIndex > result[1]:
                result[1] = middleIndex
            if middleIndex < result[0]:
                result[0] = middleIndex

            self.searchTarget(nums, target, leftIndex, middleIndex-1, result)
            self.searchTarget(nums, target, middleIndex +
                              1, rightIndex, result)

        if nums[middleIndex] > target:
            self.searchTarget(nums, target, leftIndex, middleIndex-1, result)
        else:
            self.searchTarget(nums, target, middleIndex+1, rightIndex, result)
