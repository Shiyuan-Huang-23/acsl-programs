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
                            grid[6 - c][j] = int(currInput[j][c])
                elif i == 1:
                    grid = placeDisk(grid, ord(currInput[j][0]) - 65, int(currInput[j][1]))
                    # print("Placed Disks")
                    # for row in grid:
                    #     print(row)
                    counter = [0]
                    result = applyRules(grid, counter)
                    grid = result[0]
                    counter = result[1]
                    # print("Applied Rules")
                    # for row in grid:
                    #     print(row)
                    print(counter[0])

def placeDisk(grid, c, num):
    for r in range(6, -1, -1):
        if grid[r][c] == 0:
            grid[r][c] = [num, "dr"] # "d" means this disk was dropped
            break
    return grid

def applyRules(grid, counter):
    for r in range(6, -1, -1):
        for c in range(0, 6, 1):
            try:
                # search for disks marked ["dropped"]
                if "dr" in grid[r][c]:
                    # check rows and columns to see if they match the dropped disk
                    height = 7 - r
                    horizontal = 1
                    horizontalLeft = 0
                    for i in range(c - 1, -1, -1):
                        if grid[r][i] != 0:
                            horizontalLeft += 1
                        else:
                            break
                    horizontalRight = 0
                    for i in range(c + 1, 7, 1):
                        if grid[r][i] != 0:
                            horizontalRight += 1
                        else:
                            break
                    delDisk = False
                    # print("Height: " + str(height))
                    # if height matches disk number, delete all disks of that number vertically
                    if height == grid[r][c][0]:
                        delDisk = True
                        for i in range(6, r - 1, -1):
                            if grid[i][c] == grid[r][c][0]:
                                grid[i][c] = 0
                                counter[0] += 1
                    # print("Horizontal: " + str(horizontal + horizontalLeft + horizontalRight))
                    # if width matches disk number, delete all disks of that number horizontally
                    if horizontal + horizontalLeft + horizontalRight == grid[r][c][0]:
                        delDisk = True
                        for i in range(c - horizontalLeft, c + horizontalRight + 1, 1):
                            if grid[r][i] == grid[r][c][0]:
                                grid[r][i] = 0
                                counter[0] += 1
                    # delete the original dropped disk
                    if delDisk:
                        grid[r][c] = 0
                        counter[0] += 1
                    else:
                        grid[r][c] = grid[r][c][0]
                    # move disks downward if there is a space under them, marking them as dropped
                    dropped = False
                    for r in range(5, -1, -1):
                        for c in range(0, 7, 1):
                            if grid[r][c] != 0 and grid[r + 1][c] == 0:
                                dropped = True
                                temp = r + 1
                                while temp < 7 and grid[temp][c] == 0:
                                    temp += 1
                                grid[temp - 1][c] = [grid[r][c], "dr"]
                                grid[r][c] = 0
                    # if any disks have been dropped, reapply rules
                    if dropped:
                        result = applyRules(grid, counter)
                        grid = result[0]
                        counter = result[1]
                    return [grid, counter]
            except:
                continue
    return [grid, counter]

# mark disks as dropped from bottom to top, moving them downward as much as possible during the looping
# once all disks have been moved to the right location, continue to apply drop rules until there are no more drops

main()

# Sample Input
# 436, 454, 2, 0, 67, 0, 0
# C3, B4, A3, A1, D5, B2, B2, A4, B5, D5

# Test Input
# 35, 447, 3462, 565, 0, 0, 0
# A3, A4, A4, E5, D2, A4, E4, E5, F5, C2
