from collections import deque


def sunsetViews(buildings, direction):

    queue = deque([])

    longestBuilding = float("-inf")
    iterOver = range(0, len(buildings))
    if direction == "EAST":
        iterOver = reversed(iterOver)

    for i in iterOver:
        if buildings[i] > longestBuilding:
            if direction == "EAST":
                queue.appendleft(i)
            else:
                queue.append(i)
            longestBuilding = buildings[i]

    return list(queue)
