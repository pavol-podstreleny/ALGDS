
from collections import deque


def reverseWordsInString(string):
    if len(string) == 0:
        return string

    wordsQueue = findSeparateWords(string)
    return "".join(wordsQueue)


def findSeparateWords(string):

    charList = list()
    queue = deque([])

    charList.append(string[0])
    prevChar = string[0]

    for i in range(1, len(string)):
        actualChar = string[i]
        if prevChar == " " and actualChar == " ":
            charList.append(" ")
        elif prevChar == " " and actualChar != " " or prevChar != " " and actualChar == " ":
            queue.appendleft("".join(charList))
            charList = list()
            charList.append(actualChar)
            prevChar = actualChar
        else:
            charList.append(string[i])
            prevChar = actualChar

    if len(charList) != 0:
        queue.appendleft("".join(charList))

    return queue


print(reverseWordsInString("Algoexpert is best!"))
