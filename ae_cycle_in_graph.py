def cycleInGraph(edges):
    # Write your code here.
    colors = [0 for _ in edges]

    for i in range(len(edges)):
        if dfs(i, colors, edges):
            return True

    return False


def dfs(i, colors, edges):
    if colors[i] == 1:
        return True

    if colors[i] == 2:
        return False

    if colors[i] == 0:
        colors[i] = 1

    for edgeIndex in edges[i]:
        if dfs(edgeIndex, colors, edges):
            return True

    colors[i] = 2
    return False


print(cycleInGraph([
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [0]
]))
