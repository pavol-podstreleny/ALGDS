# O(n) time | O(s) space where s is number of winning teams
def tournamentWinner(competitions, results):

    teamsDict = dict()

    for i in range(len(results)):
        winnerIndex = abs(results[i] - 1)

        teamName = competitions[i][winnerIndex]

        if teamName in teamsDict:
            teamsDict[teamName] += 1
        else:
            teamsDict[teamName] = 1

    maxWins = 0
    teamName = "Unknown"

    for key, value in teamsDict.items():
        if value > maxWins:
            maxWins = value
            teamName = key

    return teamName


print(tournamentWinner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
], [0, 0, 1]))
