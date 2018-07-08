import math

def main():
    suits = ["S", "H", "D", "C"]
    with open("BridgeBidding.txt") as f:
        myInput = [line.rstrip() for line in f]
        num = 1
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            points = countPoints(currInput[:-1])
            bid = ""
            if points >= 13:
                if len(currInput[0]) >= 5:
                    bid = "1S"
                elif len(currInput[1]) >= 5:
                    bid = "1H"
                elif len(currInput[2]) >= 3:
                    bid = "1D"
                elif len(currInput[3]) >= 3:
                    bid = "1C"
            else:
                bid = "PASS"
            print(str(num) + ". " + bid)
            num += 1
            openBid = currInput[4]
            suit = openBid[1]
            bid = ""
            if points >= 10:
                if suit == "S" and len(currInput[0]) >= 3:
                    bid = "3S"
                elif suit == "H" and len(currInput[1]) >= 3:
                    bid = "3H"
                elif suit == "D" and len(currInput[2]) >= 4:
                    bid = "3D"
                elif suit == "C" and len(currInput[3]) >= 4:
                    bid = "3C"
                if points >= 15:
                    for s in range(len(suits)):
                        if s != suits.index(suit):
                            if len(currInput[s]) >= 6:
                                bid = "3" + suits[s]
                                break
                if bid == "":
                    for s in range(len(suits)):
                        if s != suits.index(suit):
                            if s == 0 and len(currInput[s]) >= 5:
                                bid = "2S"
                                break
                            elif s == 1 and len(currInput[s]) >= 5:
                                bid = "2H"
                                break
                            elif s == 2 and len(currInput[s]) >= 4:
                                bid = "2D"
                                break
                            elif s == 3 and len(currInput[s]) >= 4:
                                bid = "2C"
                                break
                if bid == "":
                    bid = "2 NO TRUMP"
            elif points >= 6 and points <= 9:
                if suit == "S" and len(currInput[0]) >= 3:
                    bid = "2S"
                elif suit == "H" and len(currInput[1]) >= 3:
                    bid = "2H"
                elif suit == "D" and len(currInput[2]) >= 4:
                    bid = "2D"
                elif suit == "C" and len(currInput[3]) >= 4:
                    bid = "2C"
                if bid == "":
                    for s in range(len(suits)):
                        if s < suits.index(suit) and len(currInput[s]) >= 4:
                            bid = "1" + suits[s]
                            break
                if bid == "":
                    bid = "1 NO TRUMP"
            elif points < 6:
                bid = "PASS"
            print(str(num) + ". " + bid)
            num += 1

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

# Test Input
# Axx, Qxx, AJxxx, xx, 1H
# AKxxx, Qxx, Axxx, x, 1C
# Axx, Jxxx, Axxx, Jx, 1H
# Axxx, Qxx, Jxxx, Jx, 1S
# AKQxxx, KQxx, Jx, x, 1D
