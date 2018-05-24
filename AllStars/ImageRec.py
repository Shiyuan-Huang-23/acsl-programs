def main():
    with open("ImageRec.txt") as f:
        myList = [line.rstrip() for line in f]
        for i in range(len(myList)):
            currIn = myList[i].split(", ")
            for row in range(int(currIn[0])):
                temp = [0] * int(currIn[1])
            gridContent = bin(int(currIn[2], 16))[2:]
            # add leading zeros
            gridContent = ("0" * ((4 * len(currIn[2])) - len(gridContent))) + gridContent
            grid = list()
            for row in range(int(currIn[0])):
                temp = list(gridContent[0:int(currIn[1])])
                gridContent = gridContent[int(currIn[1]):]
                grid.append(temp)
            for row in range(int(len(grid) / 2)):
                b = len(grid) - row - 1
                temp = grid[row]
                grid[row] = grid[b]
                grid[b] = temp
            # for row in grid:
            #     print(row)
            # print(check(cut(grid, 2, 0, 3, 2), 0))
            z = list()
            o = list()
            for a in range(len(grid)):
                for b in range(len(grid[0])):
                    for c in range(a, len(grid)):
                        for d in range(b, len(grid[0])):
                            if(check(cut(grid, a, b, c, d), 0)):
                                temp = [c - a + 1, d - b + 1]
                                z.append(temp)
                            elif(check(cut(grid, a, b, c, d), 1)):
                                temp = [c - a + 1, d - b + 1]
                                o.append(temp)
            # print(z)
            # print(o)
            printMax(o)
            printMax(z)

def cut(arr, a, b, c, d):
    arr = arr[a:c + 1]
    for i in range(len(arr)):
        arr[i] = arr[i][b:d + 1]
    return arr

def check(arr, n):
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if int(arr[r][c]) != n:
                return False
    return True

def printMax(arr):
    if len(arr) == 0:
        print("NONE")
        return
    m = 0
    md = "NONE"
    for i in range(len(arr)):
        temp = arr[i][0] * arr[i][1]
        if temp > m:
            md = str(arr[i][0]) + " X " + str(arr[i][1])
            m = temp
    print(md)

main()

# 4, 3, FCF
# 6, 4, 30333F
# 3, 4, 5A5
# 6, 2, 03C
# 4, 5, 60CE0

# 1, 4, F
# 1, 4, 0
# 4, 2, AB
# 2, 6, A7E
# 2, 10, 7F3A8
