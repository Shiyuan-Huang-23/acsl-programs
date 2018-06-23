import math

def main():
    with open("ChainFactor.txt") as f:
        myInput = [line.rstrip() for line in f]
        grid = [[0] * 7 for i in range(7)]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            for j in range(len(currInput)):
                if i == 0:
                    if currInput[j] != "0":
                        for c in range(len(currInput[j])):
                            grid[6 - c][j] = currInput[j][c]
                elif i == 1:
                    grid = placeDisk(grid, currInput[j])

            for row in grid:
                print(row)

def placeDisk(grid, coords):
    c = ord(coords[0]) - 65
    for r in range(6, -1, -1):
        if grid[r][c] == 0:
            grid[r][c] = int(coords[1])
            return grid

main()
# 436, 454, 2, 0, 67, 0, 0
# C3, B4, A3, A1, D5, B2, B2, A4, B5, D5
