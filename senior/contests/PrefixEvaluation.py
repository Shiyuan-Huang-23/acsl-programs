def main():
    OPERATIONS = ["|", "+", "-", "*", "@", ">"]
    NUMOPS = [1, 2, 2, 2, 3, 3]
    for i in range(5):
        arr = input().split(" ")
        while True:
            broken = False
            for j in range(len(arr)):
                if len(arr[j]) == 0:
                    del arr[j]
                    broken = True
                    break
            if broken == False:
                break
        operands = []
        while len(arr) > 1:
            for j in range(len(arr) - 1, -1, -1):
                if arr[j] in OPERATIONS:
                    numOperands = NUMOPS[OPERATIONS.index(arr[j])]
                    if len(operands) >= numOperands:
                        arr[j] = str(evaluate(arr[j], operands[:numOperands]))
                        for h in range(numOperands):
                            del arr[j + 1]
                        operands = []
                        break
                    else:
                        operands = []
                else:
                    operands.insert(0, arr[j])
            # print(arr)
        print(arr[0])

def evaluate(operation, operands):
    operands = list(map(int, operands))
    if operation == "|":
        return abs(operands[0])
    elif operation == "+":
        return operands[0] + operands[1]
    elif operation == "-":
        return operands[0] - operands[1]
    elif operation == "*":
        return operands[0] * operands[1]
    elif operation == "@":
        if operands[0] > 0:
            return operands[1]
        else:
            return operands[2]
    elif operation == ">":
        return max(operands)

main()

# * + 4 5 - 3 -1
# @ - 8 9 82 46
# @ | - -8 10 82 46
# + > 8 * 2 7 9 6
# | * @ - 1 6 34 12 > - 990 1000 * -2 3 + -51 49
# + 4 * 9 5