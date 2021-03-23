# O(n + m) | O(k) where k is number of unique characters
def generateDocument(characters, document):

    if len(characters) < len(document):
        return False
    if len(document) == 0:
        return True

    letterMap = dict()

    for character in document:
        if character in letterMap:
            letterMap[character] += 1
        else:
            letterMap[character] = 1

    for character in characters:
        if character in letterMap:
            letterMap[character] -= 1

    for key, value in letterMap.items():
        if value > 0:
            return False

    return True


print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
