# O(m) time | O(1) space | m => number of items in sequence
def validateSubSequence(sequence,subsequence):

    subPointer = 0

    for number in sequence:
        if number == subsequence[subPointer]:
            subPointer += 1
        
        if subPointer == len(subsequence):
            return True
    
    return False


print(validateSubSequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]))
