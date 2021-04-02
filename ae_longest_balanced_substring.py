# O(n) time | O(1) space
def longestBalancedSubstring(string):

    maxLength = 0
    openningBracketsCounter = 0
    closingBracketsCounter = 0

    for character in string:
        if character == "(":
            openningBracketsCounter += 1
        else:
            closingBracketsCounter += 1

        if closingBracketsCounter == openningBracketsCounter:
            maxLength = max(maxLength, openningBracketsCounter * 2)
        elif closingBracketsCounter > openningBracketsCounter:
            openningBracketsCounter = 0
            closingBracketsCounter = 0

    openningBracketsCounter = 0
    closingBracketsCounter = 0
    for i in reversed(range(len(string))):
        character = string[i]
        if character == "(":
            openningBracketsCounter += 1
        else:
            closingBracketsCounter += 1

        if openningBracketsCounter == closingBracketsCounter:
            maxLength = max(maxLength, openningBracketsCounter * 2)
        elif closingBracketsCounter < openningBracketsCounter:
            openningBracketsCounter = 0
            closingBracketsCounter = 0

    return maxLength
