# O(n * d) | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]

    return ways[-1]


class Counter:

    def __init__(self, value=0):
        self.value = value


def numberOfWaysToMakeChangeRecursive(n, denoms):
    counter = Counter(0)
    numberOfWaysToMakeChangeHelper(n, denoms, 0, 0, counter)
    return counter.value


def numberOfWaysToMakeChangeHelper(n, denoms, index, value, counter):
    if value == n:
        counter.value += 1
    elif value > n:
        return
    else:
        for i in range(index, len(denoms)):
            if value + denoms[i] <= n:
                numberOfWaysToMakeChangeHelper(
                    n, denoms, i, value+denoms[i], counter)
