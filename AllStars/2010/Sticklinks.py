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
                # print(getCoords(grid, 3, 0))
                # print(getAdj(grid, 4, 0))
            else:
                result = findWord(grid, currInput, None)
                if len(result) > 0:
                    for n in result:
                        print(n[0], end = "")
                        print("," + str(n[1]) + "  ", end = "")
                    print()
                else:
                    print("NOT THERE")

def findWord(grid, word, coords):
    result = []
    if coords == None:
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == word[0]:
                    result.append(getCoords(grid, r, c))
                    if len(word) > 1:
                        recur = findWord(grid, word[1:], [r, c])
                        if len(recur) > 0:
                            result += recur
                            if len(result) == len(word):
                                return result
                        else:
                            result = []
                    else:
                        if len(result) == len(word):
                            return result
    else:
        r = coords[0]
        c = coords[1]
        searchArea = getAdj(grid, r, c)
        for n in searchArea:
            if grid[n[0]][n[1]] == word[0]:
                result.append(getCoords(grid, n[0], n[1]))
                if len(word) > 1:
                    recur = findWord(grid, word[1:], [n[0], n[1]])
                    if len(recur) > 0:
                        result += recur
                        if len(result) == len(word):
                            return result
                    else:
                        result = []
                else:
                    if len(result) == len(word):
                            return result
    return result

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

# Test Input
# ATLATS, TSDIZO, VHATES, YLEIRN, OENLOT, CALEVS
# HATES
# LOTS
# RETAILS
# LIONS
# STORE
# SLATS
# HAIR
# COAL
# LEADS
# STAID
