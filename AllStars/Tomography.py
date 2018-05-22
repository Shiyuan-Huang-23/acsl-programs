def main():
    with open("TomographyIn.txt") as f:
        inArr = [line.rstrip() for line in f]
        for i in range(len(inArr)):
            currIn = inArr[i].split(", ")
            numRows = len(currIn[0])
            numCols = len(currIn[1])
            print(str(numRows) + " " + str(numCols))
            arr = [[1, 0], [0, 0]]
            print(check(arr, "10", "10"))
            arr = list()
            for j in range(numRows):
                curr = [None] * numCols
                arr.append(curr)
            print(recur(arr, currIn[0], currIn[1]))

def recur(arr, rowSum, colSum):
    if not complete(arr):
        for j in range(len(arr)):
            for k in range(len(arr[0])):
                for i in range(2):
                    arr[j][k] = i
                    result = recur(arr, rowSum, colSum)
                    if result != False:
                        return result
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
