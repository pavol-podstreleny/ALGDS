# O(1) space and time
def validIPAddresses(string):
    if len(string) > 12 or len(string) < 4:
        return []

    validIps = []

    for i in range(1, min(len(string), 4)):

        if not isValid(string[:i]):
            continue

        for j in range(i+1, i + min(len(string) - i, 4)):

            if not isValid(string[i:j]):
                continue

            for x in range(j+1, j + min(len(string) - j, 4)):
                if not isValid(string[j:x]):
                    continue

                if not isValid(string[x:]):
                    continue

                validIps.append(
                    string[:i]+"."+string[i:j]+"."+string[j:x]+"."+string[x:])

    return validIps


def isValid(data):
    number = int(data)
    if number > 255 or number < 0:
        return False

    return len(data) == len(str(number))
