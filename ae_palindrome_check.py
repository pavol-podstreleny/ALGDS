# O(N) time | O(1) space
def palindrome_check(word):

    leftPointer = 0
    rightPointer = len(word) - 1

    while leftPointer < rightPointer:
        if word[leftPointer] != word[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1
    
    return True


print(palindrome_check("abcdcba"))