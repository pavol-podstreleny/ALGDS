class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0 and len(haystack) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)-len(needle)+1):
            index = 0
            for j in range(i, len(haystack)):
                if index == len(needle):
                    return j - len(needle)
                if haystack[j] == needle[index]:
                    index += 1
                else:
                    break

            if len(needle) == index:
                return len(haystack)-len(needle)

        return -1
