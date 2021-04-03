# O(n) time | O(1) space
def firstNonRepeatingCharacter(string):

    characterMap = dict()

    for index, character in enumerate(string):
        if character in characterMap:
            characterMap[character][1] = False
        else:
            characterMap[character] = [index, True]

    minIndex = float('inf')
    for _, value in characterMap.items():
        if value[1]:
            if value[0] < minIndex:
                minIndex = value[0]

    if minIndex == float("inf"):
        return -1
    return minIndex
