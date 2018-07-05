import math

def main():
    with open("BridgeBidding.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")

main()

# Sample Input
# AKxx, Qxx, AJxxx, x, 1C
# AKxxx, Qxx, Axxx, x, 1H
# Axx, Qxxx, Axxx, Jx, 1H
# xxxx, Qxx, Jxxx, xx, 1S
# Axx, KQ, Kx, QJxxxx, 1H
