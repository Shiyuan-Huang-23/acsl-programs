grid = None
rowStart = None
colStart = None

def main():
    # define the pieces
    PA = [["X", "A", "X"]]
    PB = [["X"], ["B"], ["X"]]
    PC = [["X", 0], ["C", "X"]]
    PD = [["X", "D"], [0, "D"], [0, "X"]]
    PE = [["X", "E", 0], [0, "E", "X"]]
    PIECES = [PA, PB, PC, PD, PE]

    for i in range(5):
        # accept input
        inArr = input("Enter the input: ").split(" ")
        for j in range(len(inArr)):
            inArr[j] = int(inArr[j])
        # WHAT WOULD HAPPEN IF THERE WERE ONLY ONE ROW
        # set up grid
        global grid
        grid = [[0] * inArr[1] for j in range(inArr[0])]
        for j in range(4, len(inArr)):
            blocked = inArr[j]
            r = (inArr[j] - 1) // inArr[1]
            c = (inArr[j] - 1) % inArr[1]
            grid[r][c] = -1
        # decide if pieces are going to the right or left
        increment = None
        if (inArr[2] - 1) % inArr[1] == 0:
            increment = 1
        else:
            increment = -1
        # get coordinates of starting cell number
        global rowStart
        global colStart
        rowStart = (inArr[2] - 1) // inArr[1]
        colStart = (inArr[2] - 1) % inArr[1]
        # gameplay
        output = ""
        lastOutput = ""
        lastOutputCount = 0
        done = False
        pieceNum = 0
        while not done:
            # get current piece in alphabetical order
            piece = PIECES[pieceNum]
            # check if the piece is valid
            valid = False
            # c is the column that either the leftmost circle piece or the rightmost circle piece has to be in
            # r is the row that the circle piece has to be in
            # when PB is the piece that this piece has to connect to, there will be 2 different row coordinates, and we will need to iterate
            if type(rowStart) is list:
                for j in range(len(rowStart)):
                    valid = isValid(piece, increment, rowStart[j], colStart)
                    if valid == True:
                        break
            else:
                valid = isValid(piece, increment, rowStart, colStart)
            # if the piece is valid, do these actions
            if valid:
                # if the new coord is off the grid, then we are done
                if colStart == -1 or colStart == len(grid[0]):
                    done = True
                # update the rowStart with new coords (1 to the right or left of the circle piece)
                # make a list for the row if PB
                rowStart = -1
                if increment == 1:
                    temp_c = colStart - 1
                else:
                    temp_c = colStart + 1
                for row in range(len(grid)):
                    if grid[row][temp_c] == "X":
                        if rowStart == -1:
                            rowStart = row
                        else:
                            # handle PB
                            temp = [rowStart]
                            temp.append(row)
                            rowStart = temp
                # add piece to output string
                output += chr(pieceNum + 65)
                lastOutput = output
                lastOutputCount = 0
            else:
                lastOutputCount += 1
                if lastOutputCount > 6:
                    output = "IMPOSSIBLE"
                    break
            # move on to next piece
            pieceNum = (pieceNum + 1) % 5
        print(output)

def isValid(piece, increment, r, c):
    valid = False
    # search for the leftmost or rightmost circle piece
    # figure out where the upper left of the piece would need to go on the grid for this to work
    # there would be 2 for PB, in which case iteration would be needed
    grid_r = -1
    grid_c = -1
    temp_c = -1
    if increment == 1:
        grid_c = c
        temp_c = 0
    else:
        grid_c = c - len(piece[0]) + 1
        temp_c = len(piece[0]) - 1
    for row in range(len(piece)):
        if piece[row][temp_c] == "X":
            if grid_r == -1:
                grid_r = r - row
            else:
                # handle PB
                temp = [grid_r]
                temp.append(r - row)
                grid_r = temp
    # if PB is involved, both r c combinations must be tried
    if type(grid_r) is list:
        for j in range(len(grid_r)):
            valid = isValidHelper(piece, increment, grid_r[j], grid_c)
            if valid == True:
                break
    else:
        valid = isValidHelper(piece, increment, grid_r, grid_c)
    return valid

def isValidHelper(piece, increment, r, c):
    valid = False
    # place the piece down on gridCopy block by block
    global grid
    gridCopy = [row[:] for row in grid]
    width = len(piece[0])
    height = len(piece)
    for col in range(width):
        for row in range(height):
            # if there is an exception and it goes off the grid, it's wrong
            if (r + row) < 0 or (r + row) >= len(gridCopy):
                return False
            if (c + col) < 0 or (c + col) >= len(gridCopy[0]):
                return False
            # if "X" or a letter goes on top of anything that's not 0, it's wrong
            if (piece[row][col] in ["X", "A", "B", "C", "D", "E"]) and gridCopy[r + row][c + col] != 0:
                return False
            # make sure 0s don't overwrite -1 blocks
            if piece[row][col] != 0:
                gridCopy[r + row][c + col] = piece[row][col]
    # after the piece has been placed, check the following
    if increment == 1:
        col = c - 1
    else:
        col = c + width - 1
    # if it's on the opposite side, make sure that side has only 0s and "X"s and -1 not any other letters
    if col < 0 or col >= len(gridCopy[0]):
        if col < 0:
            temp_c = 0
        else:
            temp_c = len(gridCopy[0]) - 1
        for row in range(len(gridCopy)):
            if gridCopy[row][temp_c] not in ["X", 0, -1]:
                return False
    # on the starting side, make sure that side has only 0s and "X"s and -1 not any other letters
    for row in range(len(gridCopy)):
        if gridCopy[row][0] not in ["X", 0, -1]:
            return False
        if gridCopy[row][len(gridCopy[0]) - 1] not in ["X", 0, -1]:
            return False
    # make sure there are no non-circle tiles touching
    for row in range(len(gridCopy)):
        if (col + 1) > -1 and (col + 1) < len(gridCopy[0]):
            first = gridCopy[row][col]
            second = gridCopy[row][col + 1]
            if first in ["A", "B", "C", "D", "E"] and second in ["A", "B", "C", "D", "E"]:
                return False
    # update global grid
    # display(gridCopy)
    # dashLength = 3 * len(gridCopy[0])
    # print(dashLength * "_")
    grid = gridCopy
    # update global colStart (1 to the right or left of the circle piece)
    global colStart
    if increment == 1:
        colStart = c + width
    else:
        colStart = c - 1
    return True

def display(grid):
    for row in grid:
        for c in row:
            print(((3 - len(str(c))) * " ") + str(c), end = "")
        print()

main()

'''
6 10 11 2 48 49
5 10 40 1 27
6 14 70 4 66 33 7 56
9 12 108 5 69 106 77 91 55
6 13 78 1 49
'''
