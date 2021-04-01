def multiStringSearch(bigString, smallStrings):

    characterMap = dict()

    for index, character in enumerate(bigString):
        if character in characterMap:
            characterMap[character].add(index)
        else:
            characterMap[character] = set()
            characterMap[character].add(index)

    result = []
    for word in smallStrings:
        isSubstring = True
        prevIndexSet = None

        for character in word:
            if character not in characterMap:
                isSubstring = False
                break
            else:
                indexSet = characterMap[character]
                if prevIndexSet is None:
                    prevIndexSet = indexSet
                    continue
                isNextIndex = False

                finalSet = set()
                for prevIndex in prevIndexSet:
                    if (prevIndex + 1) in indexSet:
                        isNextIndex = True
                        finalSet.add(prevIndex+1)

                if not isNextIndex:
                    isSubstring = False
                    break
                prevIndexSet = finalSet

        result.append(isSubstring)

    return result
