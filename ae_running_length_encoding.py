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
                encodedString.append("9")
                encodedString.append(prevCharacter)
                counter = 1
        
        else:
            encodedString.append(str(counter))
            encodedString.append(prevCharacter)
            prevCharacter = actualCharacter
            counter = 1
        
    
    if counter > 0:
        encodedString.append(str(counter))
        encodedString.append(prevCharacter)
    
    return "".join(encodedString)


print(runningLengthEncoding("AAA"))
print(runningLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))

                

