def main():
    for i in range(5):
        strA = input("Enter the first string: ")
        strB = input("Enter the second string: ")

        # diff A to B
        arrA = strA.split(" ")
        copyB = strB
        commonStr1 = ""
        for a in arrA:
            if a in copyB:
                wordIndex = copyB.index(a)
                copyB = copyB[:wordIndex] + copyB[wordIndex + len(a):]
                commonStr1 += a + " "
        commonStr1 = commonStr1[:len(commonStr1) - 1]

        # diff B to A
        arrB = strB.split(" ")
        copyA = strA
        commonStr2 = ""
        for b in arrB:
            if b in copyA:
                wordIndex = copyA.index(b)
                copyA = copyA[:wordIndex] + copyA[wordIndex + len(b):]
                commonStr2 += b + " "
        commonStr2 = commonStr2[:len(commonStr2) - 1]

        # implement second algorithm
        finalStr = ""
        for c in commonStr1:
            if c != " ":
                if c in commonStr2:
                    finalStr += c
                    commonStr2 = commonStr2[commonStr2.index(c) + 1:]
        if len(finalStr) == 0:
            print("NONE")
        else:
            print(finalStr)

main()

'''
The quick brown fox did jump over a log
The brown rabbit quickly did outjump the fox

How many pickled peppers did Peter Piper pick
Peter Piper picked a peck of pickled peppers

The AllStar Contest is in Wayne Hills NJ
Hills are where there are contestants from NJ

Fuzzy Wuzzy was a bear Fuzzy Wuzzy had no hair
Fuzzy Wuzzy was not fuzzy was he

Super cali frigi listic expi alli docious
frigid call superman allies expired list
'''
