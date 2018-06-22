import math

def main():
    with open("ChainFactor.txt") as f:
        myInput = [line.rstrip() for line in f]
        grid = [[0] * 7 for i in range(7)]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            if i == 0:
                for j in range(len(currInput)):
                    if currInput[j] != "0":
                        for c in range(len(currInput[j])):
                            grid[6 - c][j] = currInput[j][c]
        for row in grid:
            print(row)

main()
# 436, 454, 2, 0, 67, 0, 0
# C3, B4, A3, A1, D5, B2, B2, A4, B5, D5
