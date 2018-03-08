ENCLOSURES = ["{", "[", "(", ")", "]", "}"]
OPERATIONS = ["+", "-", "*", "/"]

def main():
    for i in range(5):
        # handle input
        expression = input("Enter the mathematical expression without any spaces: ")
        missingSymbol = ""
        symbolIndex = 0
        enclosureIndices = list()
        # update ENCLOSURES to reflect the enclosures in the expression
        if "{" not in expression and "}" not in expression:
            global ENCLOSURES
            ENCLOSURES.remove("{")
            ENCLOSURES.remove("}")
        if "[" not in expression and "]" not in expression:
            ENCLOSURES.remove("[")
            ENCLOSURES.remove("]")
        if "(" not in expression and ")" not in expression:
            ENCLOSURES.remove("(")
            ENCLOSURES.remove(")")
        # fill enclosureIndices with the indices of the symbols in ENCLOSURES
        for j in range(len(ENCLOSURES)):
            if ENCLOSURES[j] in expression:
                enclosureIndices.append(expression.index(ENCLOSURES[j]))
            else:
                enclosureIndices.append(-1)
                missingSymbol = ENCLOSURES[j]
                symbolIndex = j

        possibleIndices = list()
        # handles all left enclosures
        if missingSymbol in ["{", "[", "("]:
            # startIndex = index of the opposite, or the right enclosure
            startIndex = expression.index(ENCLOSURES[len(ENCLOSURES) - 1 - symbolIndex])
            # endIndex = rightmost of the left enclosures surrounding (to the left and right of) the opposite
            # if no enclosures are surrounding the opposite, as in the case of }, then endIndex = -1
            endIndex = -1
            oppositeIndex = enclosureIndices[len(ENCLOSURES) - 1 - symbolIndex]
            for j in range(int(len(enclosureIndices) / 2)):
                if j != symbolIndex:
                    leftEncloseIndex = enclosureIndices[j]
                    rightEncloseIndex = enclosureIndices[len(ENCLOSURES) - 1 - j]
                    # check to see the enclosures are surrounding the opposite
                    if oppositeIndex > leftEncloseIndex and oppositeIndex < rightEncloseIndex:
                        # check to see if this is the rightmost of the left enclosures
                        if leftEncloseIndex > endIndex:
                            endIndex = leftEncloseIndex

            operationsIndex = list()
            for j in range(startIndex, endIndex, -1):
                if expression[j] in OPERATIONS:
                    operationsIndex.append(j)

            for j in range(startIndex, endIndex, -1):
                # this is a valid location if (the endIndex is directly to the left or there's an operation to the left)
                if (j - 1) == endIndex or (j - 1) in operationsIndex:
                    # and there's at least one operator between this location and the startIndex
                    if j < operationsIndex[0]:
                        # and inserting the symbol in this location won't break up any other enclosures like this ([)]
                        # this only happens when the enclosures do not surround the opposite and the location is between those indices
                        inBetweenError = False
                        for k in range(int(len(enclosureIndices) / 2)):
                            if k != symbolIndex:
                                leftEncloseIndex = enclosureIndices[k]
                                rightEncloseIndex = enclosureIndices[len(ENCLOSURES) - 1 - k]
                                # check to see if the enclosures do not surround the opposite
                                if oppositeIndex < leftEncloseIndex or oppositeIndex > rightEncloseIndex:
                                    if j > leftEncloseIndex and j < rightEncloseIndex:
                                        inBetweenError = True
                        # and inserting the symbol in this location wouldn't result in confusing precedence like [{}]
                        # this is done by making sure the endIndex is greater than any pairs of enclosures of lower precedence
                        precedenceError = False
                        for k in range(int(len(enclosureIndices) / 2)):
                            if k < symbolIndex:
                                leftEncloseIndex = enclosureIndices[k]
                                rightEncloseIndex = enclosureIndices[len(enclosureIndices) - k - 1]
                                if j - 1 < leftEncloseIndex and j - 1 < rightEncloseIndex and oppositeIndex > rightEncloseIndex:
                                    precedenceError = True
                        if not inBetweenError and not precedenceError:
                            possibleIndices.append(j + 1)
        # handles all right enclosures
        else:
            # startIndex = index of opposite
            startIndex = expression.index(ENCLOSURES[len(ENCLOSURES) - 1 - symbolIndex])
            # endIndex = leftmost of the right enclosures surrounding (to the left and right of) the opposite
            # if no enclosures are surrounding the opposite, as in the case of {, then endIndex = expression.length()
            endIndex = len(expression)
            oppositeIndex = enclosureIndices[len(ENCLOSURES) - 1 - symbolIndex]
            for j in range(int(len(enclosureIndices) / 2)):
                if j != len(ENCLOSURES) - 1 - symbolIndex:
                    leftEncloseIndex = enclosureIndices[j]
                    rightEncloseIndex = enclosureIndices[len(ENCLOSURES) - 1 - j]
                    # check to see the enclosures are surrounding the opposite
                    if oppositeIndex > leftEncloseIndex and oppositeIndex < rightEncloseIndex:
                        # check to see if this is the leftmost of the right enclosures
                        if rightEncloseIndex < endIndex:
                            endIndex = rightEncloseIndex

            operationsIndex = list()
            for j in range(startIndex, endIndex, 1):
                if expression[j] in OPERATIONS:
                    operationsIndex.append(j)

            for j in range(startIndex, endIndex, 1):
                if (j + 1) == endIndex or (j + 1) in operationsIndex:
                    if j > operationsIndex[0]:
                        inBetweenError = False
                        for k in range(int(len(enclosureIndices) / 2)):
                            if k != len(ENCLOSURES) - 1 - symbolIndex:
                                leftEncloseIndex = enclosureIndices[k]
                                rightEncloseIndex = enclosureIndices[len(ENCLOSURES) - 1 - k]
                                # check to see if the enclosures do not surround the opposite
                                if oppositeIndex < leftEncloseIndex or oppositeIndex > rightEncloseIndex:
                                    if j > leftEncloseIndex and j < rightEncloseIndex:
                                        inBetweenError = True
                        # and inserting the symbol in this location wouldn't result in confusing precedence like [{}]
                        # this is done by making sure the endIndex is less than any pairs of enclosures of lower precedence
                        precedenceError = False
                        for k in range(int(len(enclosureIndices) / 2)):
                            if k < len(ENCLOSURES) - 1 - symbolIndex:
                                leftEncloseIndex = enclosureIndices[k]
                                rightEncloseIndex = enclosureIndices[len(enclosureIndices) - k - 1]
                                if j + 1 > leftEncloseIndex and j + 1 > rightEncloseIndex and oppositeIndex < leftEncloseIndex:
                                    precedenceError = True
                        if not inBetweenError and not precedenceError:
                            possibleIndices.append(j + 2)

        possibleIndices.sort()
        print(', '.join(str(j) for j in possibleIndices))
        ENCLOSURES = ["{", "[", "(", ")", "]", "}"]


if __name__ == "__main__": main()
