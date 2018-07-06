import math

def main():
    with open("BridgeBidding.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            points = countPoints(currInput[:-1])

def countPoints(hand):
    points = 0
    for suit in hand:
        for card in suit:
            if card == "A":
                points += 4
            elif card == "K":
                points += 3
            elif card == "Q":
                points += 2
            elif card == "J":
                points += 1
            else:
                break
    return points

main()

# Sample Input
# AKxx, Qxx, AJxxx, x, 1C
# AKxxx, Qxx, Axxx, x, 1H
# Axx, Qxxx, Axxx, Jx, 1H
# xxxx, Qxx, Jxxx, xx, 1S
# Axx, KQ, Kx, QJxxxx, 1H
