def caesar_cipher_encryptor(string,key):

    result = []
    key %= 26

    for character in string:
        difference = ord(character) - ord('a')
        totalDifference = (difference + key) % 26
        result.append(chr(ord('a') + totalDifference))
       
    return "".join(result)
  
        
print(caesar_cipher_encryptor("xyz",2))









    



