# O(N) time | O(N) space where N is number of characters in string
def runningLengthEncoding(string):

    prevCharacter = string[0]
    counter = 1
    encodedString = []

    for i in range(1,len(string)):
        actualCharacter = string[i]

        if prevCharacter == actualCharacter:
            counter += 1

            if counter == 10:
                insertEncodedSubstring(9,prevCharacter,encodedString)
                counter = 1
        
        else:
            insertEncodedSubstring(counter,prevCharacter,encodedString)
            prevCharacter = actualCharacter
            counter = 1
        
    
    if counter > 0:
        insertEncodedSubstring(counter,prevCharacter,encodedString)
    
    return "".join(encodedString)

def insertEncodedSubstring(counter,character, result):
    result.append(str(counter))
    result.append(character)

print(runningLengthEncoding("AAA"))
print(runningLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))

                

