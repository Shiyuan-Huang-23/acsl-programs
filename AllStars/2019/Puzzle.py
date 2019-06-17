# prints a 2D array
def display(grid):
    for i in grid:
        print(i)

# converts from hex to binary
def hexToBin(h):
    hList = list(h)
    binStr = ""
    for i in hList:
        decimal = int(i, 16)
        binary = bin(decimal)[2:]
        binary = ("0" * (4 - len(binary))) + binary
        binStr += binary
    return binStr

with open("as9-sample.txt") as f:
    myList = [line.rstrip() for line in f]
    for i in range(len(myList)):
        currIn = myList[i].split(" ")
        # set up grid
        n = int(currIn[0])
        grid = []
        # set up pieces
        p = int(currIn[1])
        currIn = currIn[2:]
        pieces = []
        for j in range(p):
            currPiece = []
            currHex = list(currIn[j])
            for k in currHex:
                currPiece.append(list(map(int, list(hexToBin(k)))))
            pieces.append(currPiece)
        currIn = currIn[p:]
        # fill in grid
        for j in currIn:
            grid.append(list(map(int, list(hexToBin(list(j))))))
        display(grid)

# 8 5 0E4 EA0 AEA 017 0F9 DF DF CF EB E3 EB F8 FD
# 8 5 720 EA0 575 170 0F9 FF FF F9 FD FD 01 A8 03
# 12 5 E40 075 AEA 170 F90 FFF FFF 1FF 8FF 07F 0CF A6F 1EF A0F 0FF ABF 03F
