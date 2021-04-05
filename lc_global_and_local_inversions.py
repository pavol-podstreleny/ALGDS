class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:

        maxValue = 0
        for i in range(len(A) - 2):
            maxValue = max(maxValue, A[i])

            if maxValue > A[i + 2]:
                return False

        return True
