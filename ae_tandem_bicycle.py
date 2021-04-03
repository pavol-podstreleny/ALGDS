# O(N log N) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):

    redShirtSpeeds.sort(reverse=fastest)
    blueShirtSpeeds.sort()

    total = 0

    for red, blue in zip(redShirtSpeeds, blueShirtSpeeds):
        total += max(red, blue)

    return total
