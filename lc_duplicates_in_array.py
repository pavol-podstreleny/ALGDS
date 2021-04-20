class Solution:
    # O(n) time | O(n) space
    def containsDuplicate(self, nums: List[int]) -> bool:

        duplicatesMap = set()

        for number in nums:
            if number in duplicatesMap:
                return True
            else:
                duplicatesMap.add(number)

        return False
