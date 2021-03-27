# O(N^2) | O(1) space
def validStartingCity(distances, fuel, mpg):

    # Itterate through every city
    for i in range(len(distances)):
        isValid = True
        totalDistance = 0
        for j in range(i, i + len(distances)):
            j = j % len(distances)

            actaulFuel = fuel[j]
            actualDistance = distances[j]

            totalDistance += (actaulFuel * mpg)
            totalDistance -= actualDistance

            if totalDistance < 0:
                isValid = False
                break

        if isValid:
            return i

# O(n) time | O(1) space


def validStartingCityOptimal(distances, fuel, mpg):

    minDistance = float("inf")
    totalDistance = 0
    minIndex = 0

    for i in range(1, len(distances) + 1):
        i = i % len(distances)
        prevIndex = i - 1

        totalDistance += (fuel[prevIndex] * mpg) - distances[prevIndex]
        if totalDistance < minDistance:
            minDistance = totalDistance
            minIndex = i

    return minIndex


print(validStartingCityOptimal([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))
