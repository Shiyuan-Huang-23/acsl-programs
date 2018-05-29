def main():
    with open("ACSLLetters.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currIn = list(myInput[i].upper())
            inArr = [""]
            for j in range(len(currIn)):
                if ord(currIn[j]) >= 65 and ord(currIn[j]) <= 90:
                    inArr[len(inArr) - 1] += currIn[j]
                else:
                    if len(inArr[len(inArr) - 1]) > 0 and j != len(currIn) - 1:
                        inArr.append("")
            print(inArr)

main()
