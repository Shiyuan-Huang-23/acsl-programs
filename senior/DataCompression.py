def main():
    for i in range(5):
        inputStr = input().split(" ")
        j = 0
        while j < len(inputStr):
            if len(inputStr[j]) > 1 and findPunctuation(inputStr[j]):
                punctuation = inputStr[j][len(inputStr[j]) - 1]
                inputStr[j] = inputStr[j][:len(inputStr[j]) - 1]
                inputStr.insert(j + 1, punctuation)
            j += 1
        wordbank = []
        for j in range(len(inputStr)):
            if findPunctuation(inputStr[j]) == False:
                word = inputStr[j]
                if word not in wordbank:
                    if word in inputStr[j + 1:]:
                        wordbank.append(word)
        j = 0
        while j < len(inputStr):
            if inputStr[j] != " ":
                if (j + 1) < len(inputStr) and (findPunctuation(inputStr[j + 1]) == False or inputStr[j + 1] == "-"):
                    inputStr.insert(j + 1, " ")
            j += 1
        # print(inputStr)
        for j in range(len(inputStr)):
            if inputStr[j] in wordbank:
                inputStr[j] = str(wordbank.index(inputStr[j]) + 1)
        # print(inputStr)
        print("".join(inputStr))

def findPunctuation(string):
    char = ord(string[len(string) - 1])
    if char < 65 or (char > 90 and char < 97) or char > 122:
        return True
    else:
        return False

if __name__ == "__main__": main()

# Sample Input
# YES I CAN! YES I CAN! YES I CAN!
# SHE LOVES YOU! YEAH! YEAH! YEAH!
# SEA SHELLS SEA SHELLS BY THE SEA SHORE

# Test Inputs
# WE FORM OUR HABITS, THEN OUR HABITS FORM US.
# WE DON'T SEE THINGS AS THEY ARE, WE SEE THINGS AS WE ARE.
# KNOWS HOW WILL ALWAYS HAVE A JOB. KNOWS WHY WILL ALWAYS BE HIS BOSS.
# NO TIME TO DO IT RIGHT, BUT TIME TO DO IT OVER.
# THE PLACE TO BE HAPPY IS HERE; THE TIME TO BE HAPPY IS NOW.
