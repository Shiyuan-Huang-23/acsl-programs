def main():
    with open("Tomography.txt") as f:
        inArr = [line.rstrip() for line in f]
        for i in range(len(inArr)):
            currIn = inArr[i].split(", ")
            numRows = len(currIn[0])
            numCols = len(currIn[1])
            # print(str(numRows) + " " + str(numCols))
            arr = [[1, 0], [0, 0]]
            # print(check(arr, "10", "10"))
            arr = list()
            for j in range(numRows):
                curr = [None] * numCols
                arr.append(curr)
            result = recur(arr, currIn[0], currIn[1])
            for row in result:
                for cell in row:
                    print(str(cell) + " ", end = "")
                print()

def recur(arr, rowSum, colSum):
    if not complete(arr):
        for j in range(len(arr)):
            for k in range(len(arr[0])):
                if arr[j][k] == None:
                    for i in range(2):
                        arr[j][k] = i
                        # prevents the recursion from going on for too long
                        # breaks when the current rowSum or current colSum is greater than the target rowSum or colSum
                        preventOverload = False
                        for r in range(len(arr)):
                            s = 0
                            for c in range(len(arr[0])):
                                if arr[r][c] == None:
                                    s += 0
                                else:
                                    s += arr[r][c]
                            if s > int(rowSum[r]):
                                preventOverload = True
                                break
                        for c in range(len(arr[0])):
                            s = 0
                            for r in range(len(arr)):
                                if arr[r][c] == None:
                                    s += 0
                                else:
                                    s += arr[r][c]
                            if s > int(colSum[c]):
                                preventOverload = True
                                break
                        if preventOverload == False:
                            result = recur(arr, rowSum, colSum)
                            if result != False:
                                return result
                    arr[j][k] = None
                    return False
    else:
        if(check(arr, rowSum, colSum)):
            return arr
        else:
            return False

def complete(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == None:
                return False
    return True

def check(arr, rowSum, colSum):
    for i in range(len(arr)):
        if sum(arr[i]) != int(rowSum[i]):
            return False
    for i in range(len(arr[0])):
        s = 0
        for j in range(len(arr)):
            s += arr[j][i]
        if s != int(colSum[i]):
            return False
    return True

if __name__ == "__main__": main()

# Sample Input
# 10, 10
# 20, 11
# 21, 21
# 100, 001
# 300, 111
# 031, 211
# 102, 210
# 111, 300
# 2002, 2200
# 2322, 4410

# Test Input
# 00, 00
# 21, 12
# 232, 313
# 333, 333
# 301, 121
# 231, 312
# 1230, 0321
# 2310, 1023
# 4321, 1234
# 50000, 11111
