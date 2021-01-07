# O(n^2) time | O(1) space
def bubble_sort(numbers):

    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1],numbers[j]
                swapped = True
        
        if not swapped:
            break
    
    return numbers



print(bubble_sort([8,5,2,9,5,6,3]))



