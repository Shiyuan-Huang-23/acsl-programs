def factors(n):
    result = list()
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def nar(grid, a, b, c, d):
    grid = grid[a:c]
    for i in range(len(grid)):
        grid[i] = grid[i][b:d]
    return grid

def check(grid, tile):
    broken = False
    for a in range(int(len(grid) / len(tile))):
        for b in range(int(len(grid[0]) / len(tile[0]))):
            temp = nar(grid, a * len(tile), b * len(tile[0]), a * len(tile) + len(tile), b * len(tile[0]) + len(tile[0]))
            for r in range(len(temp)):
                for c in range(len(temp[0])):
                    if temp[r][c] != tile[r][c]:
                        broken = True
                        break
    return not broken

def main():
    with open("Subpattern.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            grid = list()
            currIn = myInput[i].split(" ")
            for j in range(2, len(currIn)):
                tempStr = bin(int(currIn[j], 16))[2:]
                tempStr = "0" * (4 * len(currIn[j]) - len(tempStr)) + tempStr
                tempStr = tempStr[:int(currIn[1])]
                grid.append(list(tempStr))
            factrow = factors(int(currIn[0]))
            factcol = factors(int(currIn[1]))
            dim = list()
            for a in range(len(factrow)):
                for b in range(len(factcol)):
                    tile = nar(grid, 0, 0, factrow[a], factcol[b])
                    if check(grid, tile):
                        dim.append([factrow[a], factcol[b]])
            minArea = len(grid) * len(grid[0]) + 1
            minDim = ""
            for j in range(len(dim)):
                if dim[j][0] * dim[j][1] < minArea:
                    minArea = dim[j][0] * dim[j][1]
                    minDim = str(dim[j][0]) + " " + str(dim[j][1])
            print(minDim)

main()

# 8 8 FF AA 55 00 FF AA 55 00
# 4 4 F F F F
# 4 4 1 1 1 1
# 3 4 A A A
# 4 8 CC AA CC AA
# 4 6 22 B1 22 B1
# 6 4 3 A F 3 A F
# 6 6 B1 D2 21 B1 D2 21
# 6 8 AA AA AA AA AA AA
# 5 5 00 00 00 00 00
