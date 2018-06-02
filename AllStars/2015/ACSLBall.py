def main():
    with open("ACSLBall.txt") as f:
        playerScores = dict()
        teamXScores = dict()
        teamYScores = dict()
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currIn = myInput[i].split(", ")
            scoreArr = list(currIn[1])
            for j in range(len(scoreArr)):
                if j == len(scoreArr) - 1:
                    scoreArr[j] = int(scoreArr[j], 16)
                else:
                    scoreArr[j] = int(scoreArr[j])
            playerScores[currIn[0]] = [scoreArr[: len(scoreArr) - 1], scoreArr[len(scoreArr) - 1]]
            if i < 5:
                teamXScores[currIn[0]] = [scoreArr[: len(scoreArr) - 1], scoreArr[len(scoreArr) - 1]]
            else:
                teamYScores[currIn[0]] = [scoreArr[: len(scoreArr) - 1], scoreArr[len(scoreArr) - 1]]
        print(sumScores(playerScores) / len(myInput))
        print(medianScores(playerScores))
        print(highScorer(teamXScores, False) + ", " + highScorer(teamYScores, False))
        print(highScorer(playerScores, True))
        teamScores = [sumScores(teamXScores), sumScores(teamYScores)]
        teamScores.sort(reverse = True)
        print(str(teamScores[0]) + ", " + str(teamScores[1]))
        print(minScorer(playerScores))
        print(highestPer(teamXScores, True))
        print(highestPer(teamYScores, False))
        print(highestZone(playerScores, 2))
        print(highestZone(playerScores, 1))
        # print(teamXScores)
        # print(teamYScores)
        # print(playerScores)

def sumScores(playerScores):
    total = 0
    for i, j in playerScores.items():
        total += 1 * j[0][0] + 2 * j[0][1] + 3 * j[0][2] + 4 * j[0][3]
    return total

def medianScores(playerScores):
    allScores = []
    for i, j in playerScores.items():
        score = 1 * j[0][0] + 2 * j[0][1] + 3 * j[0][2] + 4 * j[0][3]
        allScores.append(score)
    allScores.sort()
    if len(allScores) % 2 == 0:
        return (allScores[int(len(allScores) / 2) - 1] + allScores[int(len(allScores) / 2)]) / 2
    else:
        return allScores[int(len(allScores) / 2)]

def highScorer(playerScores, two):
    maxScore = 0
    maxPlayer = ""
    for i, j in playerScores.items():
        score = 1 * j[0][0] + 2 * j[0][1] + 3 * j[0][2] + 4 * j[0][3]
        if score > maxScore:
            maxScore = score
            maxPlayer = i
    if two == False:
        return maxPlayer
    else:
        maxScore2 = 0
        maxPlayer2 = ""
        for i, j in playerScores.items():
            score = 1 * j[0][0] + 2 * j[0][1] + 3 * j[0][2] + 4 * j[0][3]
            if score > maxScore2 and i != maxPlayer:
                maxScore2 = score
                maxPlayer2 = i
        return maxPlayer + ", " + maxPlayer2

def minScorer(playerScores):
    minScore = 15 * 4 + 1
    minPlayer = []
    for i, j in playerScores.items():
        score = 1 * j[0][0] + 2 * j[0][1] + 3 * j[0][2] + 4 * j[0][3]
        if score < minScore:
            minPlayer = []
            minPlayer.append(i)
            minScore = score
        elif score == minScore:
            minPlayer.append(i)
    return ", ".join(minPlayer)

def highestPer(playerScores, high):
    highest = 0.0
    lowest = 1.0
    player = []
    for i, j in playerScores.items():
        percentage = sum(j[0]) / j[1]
        if high:
            if percentage > highest:
                player = []
                player.append(i)
                highest = percentage
            elif percentage == highest:
                player.append(i)
        else:
            if percentage < lowest:
                player = []
                player.append(i)
                lowest = percentage
            elif percentage == lowest:
                player.append(i)
    return ", ".join(player)

def highestZone(playerScores, zone):
    highest = 0
    player = []
    for i, j in playerScores.items():
        if zone == 2:
            score = j[0][1]
        elif zone == 1:
            score = j[0][0]
        if score > highest:
            player = []
            player.append(i)
            highest = score
        elif score == highest:
            player.append(i)
    return ", ".join(player)


main()

# Sample Input
# Alex, 11006
# Brett, 11118
# Chuck, 01119
# Dave, 2331D
# Ed, 2421F
# Fred, 10119
# Greg, 2322E
# Henry, 0214B
# Ivan, 1202E
# Jim, 2310A

# Test Input
# A, 20004
# B, 1130B
# C, 3141E
# D, 1111C
# E, 2223F
# F, 1412B
# G, 3222D
# H, 5322E
# I, 12118
# J, 01106
