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
            letterArr = list(''.join(inArr))
            letterArr.sort()
            letterDict = dict()
            for j in range(len(letterArr)):
                if letterArr[j] not in letterDict:
                    letterDict[letterArr[j]] = 1
                else:
                    letterDict[letterArr[j]] += 1
            maxNum = 0
            maxLetter = ""
            for j, k in letterDict.items():
                if k > maxNum:
                    maxNum = k
                    maxLetter = j
            print(maxLetter + " " + str(maxNum))

            for j in letterDict:
                letterDict[j] = 0
            for j in range(len(inArr)):
                word = list(inArr[j])
                for k in letterDict:
                    if k in word:
                        letterDict[k] += 1
            maxNum = 0
            maxLetter = ""
            for j, k in letterDict.items():
                if k > maxNum:
                    maxNum = k
                    maxLetter = j
            print(maxLetter + " " + str(maxNum))
            allLetters = list()
            for j in letterDict:
                allLetters.append(j)
            allLetters.sort(reverse = True)
            print("".join(allLetters))
            repeatedLetters = list()
            for j in range(len(inArr)):
                word = list(inArr[j])
                temp = dict()
                for k in word:
                    if k not in temp:
                        temp[k] = 1
                    else:
                        repeatedLetters.append(k)
            repeatedLetters = list(set(repeatedLetters))
            repeatedLetters.sort()
            print("".join(repeatedLetters))
            letterDict = dict()
            for j in range(len(letterArr)):
                if letterArr[j] not in letterDict:
                    letterDict[letterArr[j]] = 1
                else:
                    letterDict[letterArr[j]] += 1

            sortedValues = sorted(list(set(sorted(letterDict.values(), reverse = True))), reverse = True)
            for j in sortedValues:
                if j > 1:
                    for k, m in letterDict.items():
                        if m == j:
                            print(k, end = "")
            print("")


main()

# Sample Input
# The All-Star Contest will be held in Orlando, Florida.
# After we win, we are going to Disney World.

# Test Input
# The Wizarding World of Harry Potter at Universal Studios.
# Oh what a tangled web we weave when we first practice to deceive.
