def solveThis(m, n, p):
    result = ""
    if m == 1:
        result = "1"
    if m == 2:
        result = "11"
    if len(result) == 0:
        start = "11"
        for j in range(int(m) - 2):
            newStr = ""
            num = 1
            for i in range(1, len(start)):
                if start[i : i + 1] == start[i - 1 : i]:
                    num += 1
                    if i == len(start) - 1:
                        newStr += str(num)
                        newStr += start[i : i + 1]
                else:
                    newStr += str(num)
                    newStr += start[i - 1 : i]
                    num = 1
                    if i == len(start) - 1:
                        newStr += "1"
                        newStr += start[i : i + 1]
            start = newStr
        result = newStr
    print(result[n - 1 : n + p])

def main():
    with open("LookAndSay.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currIn = myInput[i].split(" ")
            solveThis(int(currIn[0]), int(currIn[1]), int(currIn[2]))

main()

# 2 2 0
# 3 1 1
# 4 2 2
# 5 4 2
# 6 1 2
# 7 2 4
# 8 4 4
# 9 7 3
# 10 10 5
# 11 15 6
