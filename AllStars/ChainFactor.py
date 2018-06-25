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
                    print("Placed Disks")
                    for row in grid:
                        print(row)
                    counter = [0]
                    result = applyRules(grid, counter)
                    grid = result[0]
                    counter = result[1]
                    print("Applied Rules")
                    for row in grid:
                        print(row)

def placeDisk(grid, c, num):
    for r in range(6, -1, -1):
        if grid[r][c] == 0:
            grid[r][c] = [num, "dr"] # "d" means this disk was dropped
            # height = 7 - r
            # horizontal = 1
            break
    # for i in range(c - 1, -1, -1):
    #     if grid[r][i] != 0:
    #         horizontal += 1
    #     else:
    #         break
    # for i in range(c + 1, 7, 1):
    #     if grid[r][i] != 0:
    #         horizontal += 1
    #     else:
    #         break
    # print("Height: " + str(height))
    # print("Horizontal: " + str(horizontal))
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
                    print("Height: " + str(height))
                    print("Horizontal: " + str(horizontal + horizontalLeft + horizontalRight))
                    return [grid, counter]
            except:
                continue
    return [grid, counter]


# if a row or column matches, mark like-numbered disks for deletion
# delete disks starting from bottom row and going up to top row and increment delDisks counter
# mark disks as dropped from bottom to top, moving them downward as much as possible during the looping
# once all disks have been moved to the right location, continue to apply drop rules until there are no more drops

main()
# 436, 454, 2, 0, 67, 0, 0
# C3, B4, A3, A1, D5, B2, B2, A4, B5, D5
