# generate check digit for a 7-digit number
def checkDigit(num):
    while True:
        # split the number into an integer array
        numArr = list(str(num))
        for i in range(len(numArr)):
            numArr[i] = int(numArr[i])
        # multiply each digit by the proper factor and divide by 123
        factor = 2
        for i in range(len(numArr) - 1, -1, -1):
            numArr[i] *= factor
            factor += 1
        num = sum(numArr) % 123
        # determine whether to continue
        if num == 17:
            return None
        if num < 10:
            return num

def findAnswer(currIn):
    # find check digits for all numbers
    digitArr = [0] * 10
    for j in range(int(currIn[0]), int(currIn[0]) + int(currIn[1]) + 1):
        currDigit = checkDigit(j)
        if currDigit != None:
            digitArr[currDigit] += 1
    # determine the most frequent digit(s)
    most = []
    maximum = 0
    for k in range(len(digitArr)):
        if digitArr[k] > maximum:
            maximum = digitArr[k]
            most = [k]
        elif digitArr[k] == maximum and maximum > 0:
            most.append(k)
    if len(most) > 0:
        for i in range(len(most)):
            most[i] = str(most[i])
        print(" and ".join(most))
    else:
        print("No valid check digits")

def main():
    # take input
    # for i in range(1):
    #     currIn = input("Enter the comma-separated input here: ").split(", ")
    with open("CheckDigit.txt") as f:
        inArr = [line.rstrip() for line in f]
        for i in range(len(inArr)):
            currIn = inArr[i].split(", ")
            findAnswer(currIn)

if __name__ == "__main__": main()

# Sample Input
# 1234567, 1
# 1999999, 30
# 1231000, 20
# 34, 1


