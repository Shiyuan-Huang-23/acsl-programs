def main():
    with open("ACSLBall.txt") as f:
        playerScores = dict()
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
        print(sumScores(playerScores) / len(myInput))
        print(playerScores)

def sumScores(playerScores):
    total = 0
    for i, j in playerScores.items():
        total += 1 * j[0][0] + 2 * j[0][1] + 3 * j[0][2] + 4 * j[0][3]
    return total

main()
