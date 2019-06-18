# prints a 2D array
def display(grid):
    for i in grid:
        for j in i:
            if j == 1:
                print(" ", end = "")
            else:
                print(j, end = "")
        print()
        #print(i)

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

# returns coordinates of bottom-most, left-most location
def botLeft(grid, target):
    w = len(grid[0])
    h = len(grid)
    output = [-1, -1]
    for r in range(h - 1, -1, -1):
        for c in range(w):
            if grid[r][c] == target:
                return [r, c]
    return output

# tries to place a given piece in a certain location
# returns False if piece cannot be placed
# returns the grid with the placed piece otherwise
def place(grid, piece, grid_r, grid_c):
    # starting from the bottom left of the piece, tries to place the piece in the grid
    # finds the bottom-most row of the piece
    temp = botLeft(piece, 1)
    piece_r = temp[0]
    piece_c = temp[1]
    # width and height of the piece
    piece_w = len(piece[0])
    gridCopy = [row[:] for row in grid]
    for r in range(piece_r, -1, -1):
        if r == piece_r:
            for c in range(piece_c, piece_w):
                if piece[r][c] == 1:
                    temp_r = grid_r - (piece_r - r)
                    temp_c = grid_c + (c - piece_c)
                    # checks if coords are invalid
                    if temp_r < 0 or temp_r >= len(grid) or temp_c < 0 or temp_c >= len(grid[0]):
                        return False
                    if gridCopy[temp_r][temp_c] == 0:
                        gridCopy[temp_r][temp_c] = 1
                    else:
                        return False
        else:
            for c in range(piece_w):
                if piece[r][c] == 1:
                    temp_r = grid_r - (piece_r - r)
                    temp_c = grid_c + (c - piece_c)
                    # checks if coords are invalid
                    if temp_r < 0 or temp_r >= len(grid) or temp_c < 0 or temp_c >= len(grid[0]):
                        return False
                    if gridCopy[temp_r][temp_c] == 0:
                        gridCopy[temp_r][temp_c] = 1
                    else:
                        return False
    return gridCopy

# completes one 90 degree clockwise rotation
def rotate(piece):
    height = len(piece)
    width = len(piece[0])
    newPiece = [[0] * height for i in range(width)]
    for r in range(height):
        for c in range(width):
            newPiece[c][height - 1 - r] = piece[r][c]
    return newPiece

# places the puzzle pieces on the grid
# returns the minimum number of degree rotations
def placePieces(grid, pieces):
    pieceIndex = 0
    w = len(grid[0])
    h = len(grid)
    rotation = 0
    curr_rotation = 0
    piecesSkipped = 0
    while True:
        if piecesSkipped > len(pieces):
            return rotation
        curr_done = False
        currPiece = pieces[pieceIndex]
        for i in range(curr_rotation):
            currPiece = rotate(currPiece)
        for r in range(h - 1, -1, -1):
            for c in range(w):
                if grid[r][c] == 0 and curr_done == False:
                    # find bottom-most, left-most open grid location
                    # try to place the first piece there
                    result = place(grid, currPiece, r, c)
                    # at any point, if there is success, place the piece and move onto the next alphabet piece, remember to start with A again
                    if result != False:
                        display(result)
                        print("Successfully placed piece", pieceIndex)
                        print("Coords: " + str(r) + " " + str(c))
                        display(currPiece)
                        grid = result
                        pieceIndex += 1
                        rotation += curr_rotation
                        if pieceIndex == len(pieces):
                            pieceIndex = 0
                        piecesSkipped = 0
                        curr_done = True
        # if there is still not success, rotate the piece and repeat the aforementioned steps
        if curr_done == False:
            curr_rotation += 1
            if curr_rotation == 4:
                pieceIndex += 1
                if pieceIndex == len(pieces):
                    pieceIndex = 0
                curr_rotation = 0
                piecesSkipped += 1
            # stop if you cycle through pieces A - E without being able to place any pieces, or if there are no blank pieces on the grid

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
            display(currPiece)
            print("piece", j)
        currIn = currIn[p:]
        # fill in grid
        for j in currIn:
            grid.append(list(map(int, list(hexToBin(list(j))))))
        display(grid)
        print()
        # place pieces
        print(placePieces(grid, pieces))

# 8 5 0E4 EA0 AEA 017 0F9 DF DF CF EB E3 EB F8 FD
# 8 5 720 EA0 575 170 0F9 FF FF F9 FD FD 01 A8 03
# 12 5 E40 075 AEA 170 F90 FFF FFF 1FF 8FF 07F 0CF A6F 1EF A0F 0FF ABF 03F
