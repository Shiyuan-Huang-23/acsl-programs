import math

def main():
    with open("Sticklinks.txt") as f:
        myInput = [line.rstrip() for line in f]
        grid = []
        for i in range(len(myInput)):
            currInput = myInput[i]
            if i == 0:
                currInput = currInput.split(", ")
                for j in range(len(currInput)):
                    grid.append(list(currInput[len(currInput) - j - 1]))
                for row in grid:
                    print(row)
                print(getCoords(grid, 3, 0))
                print(getAdj(grid, 4, 0))

def getAdj(grid, r, c):
    coords = []
    coords.append([r - 1, c - 1])
    coords.append([r - 1, c])
    coords.append([r - 1, c + 1])
    coords.append([r, c - 1])
    coords.append([r, c + 1])
    coords.append([r + 1, c - 1])
    coords.append([r + 1, c])
    coords.append([r + 1, c + 1])
    while True:
        deleted = False
        for i in range(len(coords)):
            if coords[i][0] < 0 or coords[i][0] > len(grid) - 1 or coords[i][1] < 0 or coords[i][1] > len(grid[0]) - 1:
                del coords[i]
                deleted = True
                break
        if deleted == False:
            break
    return coords

def getCoords(grid, r, c):
    return [len(grid) - r, c + 1]

main()

# Sample Input
# DOJOS, NMKNR, EFCLB, GYMEQ, AHIYP
# MONEY
# AGE
# DONKEY
