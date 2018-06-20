import math

def main():
    with open("StraddlingCheckerboard.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            alpha = []
            for c in range(65, 91, 1):
                alpha.append(chr(c))
            keyword = currInput[0]
            table = []
            for w in keyword:
                table.append(w)
            for a in alpha:
                if a not in table:
                    table.append(a)
            table.append(".")
            table.append("/")
            rowNum = []
            colNum = []
            for n in range(10):
                rowNum.append((n + int(currInput[2])) % 10)
                if table[n] == '#':
                    colNum.append(rowNum[len(rowNum) - 1])
            colNum.sort()
            encrypt = [None] * 3
            encrypt[0] = table[0 : 10]
            encrypt[1] = table[10 : 20]
            encrypt[2] = table[20: ]
            for c in currInput[1]:
                indices = findIndex(c, encrypt)
                if indices[0] != 0:
                    print(str(colNum[indices[0] - 1]) + " ", end = "")
                print(str(rowNum[indices[1]]) + " ", end = "")
            print()

def findIndex(c, encrypt):
    for i in range(len(encrypt)):
        for j in range(len(encrypt[0])):
            if encrypt[i][j] == c:
                return [i , j]

main()

# Sample Input
# MATH#CODE#, RIDGES, 2
# ##COMPUTER, COMPSCI, 3
# CLO#TH#ING, BYTES, 5
# BEAR#H#UGS, DECODE, 8
# BIFOC#AL#S, RECURSIVE, 1
