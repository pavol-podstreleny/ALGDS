# O(n log n) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):

    redShirtHeights.sort()
    blueShirtHeights.sort()

    isBigger = True
    isSmaller = True

    for red, blue in zip(redShirtHeights, blueShirtHeights):
        isBigger = isBigger and red > blue
        isSmaller = isSmaller and red < blue

    return isBigger or isSmaller


print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
