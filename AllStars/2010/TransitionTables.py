def main():
    with open("TransitionTables.txt") as f:
        myInput = [line.rstrip() for line in f]
        number = 1
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            table = [0] * int(currInput[0])
            for j in range(len(table)):
                table[j] = [j + 1] + list(currInput[j + 1])
                for k in range(len(table[j])):
                    table[j][k] = int(table[j][k])
            print(str(number) + ".", end = "")
            number += 1
            row = [0, 0]
            print(regex(table))

def regex(table):
    result = []
    result.append(regexHelper(table, 1))
    result.append(regexHelper(table, 2))
    if result[0] == result[1]:
        result = result[0]
    else:
        result = " OR ".join(result)

    return result

def regexHelper(table, branch):
    result = ""
    finished = False
    r = 0
    while not finished:
        row = table[r]
        state = row[0]
        for c in range(1, 3, 1):
            rule = row[c]
            if rule == state:
                result += chr(c + 96) + "*"
        branching = False
        poss = []
        for c in range(1, 3, 1):
            if row[c] != 0 and row[c] != state:
                poss.append(row[c])
        if len(poss) == 2:
            branching = True
        for c in range(1, 3, 1):
            rule = row[c]
            if rule != state and rule != 0:
                if branching:
                    if c == branch:
                        result += chr(c + 96)
                else:
                    result += chr(c + 96)

        # do something if one of the rules is not a state or 0
        # if both rules meet this criteria, use the branch to determine which to follow
        possibilities = []
        row = table[r]
        for c in range(1, 3, 1):
            if row[c] != 0 and row[c] != state:
                possibilities.append(row[c])
        if len(possibilities) == 1:
            r = possibilities[0] - 1
        elif len(possibilities) == 2:
            r = possibilities[branch - 1] - 1
        else:
            finished = True
    return result

main()

# Sample Input
# 3, 20, 32, 00
# 4, 21, 03, 40, 00
# 4, 12, 32, 04, 00
# 4, 24, 32, 00, 02
# 5, 20, 43, 50, 05, 00

# Test Input
# 3, 20, 03, 00
# 3, 02, 30, 00
# 3, 12, 32, 00
# 3, 20, 32, 00
# 4, 20, 23, 34, 00
# 3, 32, 03, 00
# 4, 32, 40, 43, 00
# 4, 32, 23, 43, 00
# 5, 25, 23, 40, 00, 04
# 5, 20, 35, 40, 00, 45
