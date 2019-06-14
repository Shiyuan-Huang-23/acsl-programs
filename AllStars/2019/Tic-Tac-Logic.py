# prints a 2D grid
def displayGrid(grid):
  for i in grid:
    print(i)

# undoes run-length encoding of input
def parseInput(currIn):
  inStr = ""
  temp = ""
  for j in currIn:
    if j in ["O", "X"]:
      if temp != "":
        inStr += " " * int(temp)
        temp = ""
      inStr += j
    else:
      temp += j
  if temp != "":
    inStr += " " * int(temp)  
  return inStr

# places pieces on grid based on decoded input
def placePieces(inStr, grid):
  for i in range(len(grid)):
    for j in range(len(grid)):
      piece = inStr[0]
      grid[i][j] = piece
      inStr = inStr[1:]
  return grid

# gets a column of the grid based on the column number
def getCol(grid, colNum):
  col = []
  for i in range(len(grid)):
    col.append(grid[i][colNum])
  return col

# checks if a row is filled
def isFilled(row):
  for i in row:
    if i == " ":
      return False
  return True

# checks if there are more than two consecutive placePieces
def checkConsecutive(row, key):
  cnt = 0
  for i in row:
    if i == key:
      cnt += 1
    else:
      cnt = 0
    if cnt > 2:
      return False
  return True

# checks if a given row follows the rules
def checkRow(grid, rowNum):
  row = grid[rowNum]
  # checks if there are too many Xs or Os
  oCnt = 0
  xCnt = 0
  for i in row:
    if i == "X":
      xCnt += 1
    elif i == "O":
      oCnt += 1
  half = int(len(row) / 2)
  if xCnt > half or oCnt > half:
    return False
  if (checkConsecutive(row, "X") and checkConsecutive(row, "O")) == False:
    return False
  # check uniqueness of row
  if isFilled(row):
    for i in range(rowNum):
      if grid[i] == grid[rowNum]:
        return False
  return True

# checks if a given column follows the rules
def checkCol(grid, colNum):
  col = getCol(grid, colNum)
  # checks if there are too many Xs or Os
  oCnt = 0
  xCnt = 0
  for i in col:
    if i == "X":
      xCnt += 1
    elif i == "O":
      oCnt += 1
  half = int(len(col) / 2)
  if xCnt > half or oCnt > half:
    return False
  if (checkConsecutive(col, "X") and checkConsecutive(col, "O")) == False:
    return False
  # check uniqueness of row
  if isFilled(col):
    for i in range(colNum):
      if getCol(grid, i) == getCol(grid, colNum):
        return False
  return True
    
# fills the grid recursively
def fillGrid(grid):
  for i in range(len(grid)):
    if (checkRow(grid, i) and checkCol(grid, i)) == False:
      return False
  filled = True
  for i in range(len(grid)):
    if isFilled(grid[i]) == False:
      filled = False
      break
  if filled == True:
    return grid
  for i in range(len(grid)):
    if isFilled(grid[i]) == False:
      for j in range(len(grid[i])):
        if grid[i][j] == " ":
          grid[i][j] = "X"
          answer = fillGrid(grid)
          if answer != False:
            return answer
          else:
            grid[i][j] = "O"
            answer = fillGrid(grid)
            if answer != False:
              return answer
            else:
              grid[i][j] = " "
              return False

with open("as6-sample.txt") as f:
  myList = [line.rstrip() for line in f]
  for i in range(len(myList)):
    currIn = myList[i].split(" ")
    n = int(currIn[0])
    grid = [[""] * n for j in range(n)]
    inStr = parseInput(currIn[1])
    grid = placePieces(inStr, grid)
    grid = fillGrid(grid)
    binStr = ""
    for j in range(len(grid)):
      if grid[j][j] == "X":
        binStr += "1"
      else:
        binStr += "0"
    decimal = int(binStr, 2)
    hexOutput = (hex(decimal)[2:]).upper()
    print(hexOutput)

# 6 2OX1O9X2OX1X4O8O
# 8 2O3O2X9O2XXX3X5O3O5XX1X1X9X1X2
# 10 X3O2O4OO9O2O4X3X12X2O5X5X1OO3O9O3XX1O1O2XX2O3
