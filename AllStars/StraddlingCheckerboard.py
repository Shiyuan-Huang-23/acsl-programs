import math

def main():
    with open("StraddlingCheckerboard.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")

main()

# Sample Input
# MATH#CODE#, RIDGES, 2
# ##COMPUTER, COMPSCI, 3
# CLO#TH#ING, BYTES, 5
# BEAR#H#UGS, DECODE, 8
# BIFOC#AL#S, RECURSIVE, 1
