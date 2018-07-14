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
            print(str(number) + ".")
            number += 1
            for row in table:
                print(row)
            print(regex(table, False))

def regex(table, orCond):
    result = ""
    if not orCond:
        for row in table:
            state = row[0]
            aRule = row[1]
            bRule = row[2]
            if aRule == state:
                result += "a*"
            elif bRule == state:
                result += "b*"
            if aRule == state + 1:
                result += "a"
            elif bRule == state + 1:
                result += "b"
    else:
        result = ""
        r = 0
        for j in range(len(table)):
            row = table[j]
            state = row[0]
            aRule = row[1]
            bRule = row[2]
            if aRule == state:
                result += "a*"
            elif bRule == state:
                result += "b*"
            if aRule == state + 1:
                result += "a"
            elif bRule == state + 1:
                result += "b"
            if aRule != state and aRule != 0 and aRule != state + 1:
                result = [result] * 2
                r = j
                break
            if bRule != state and bRule != 0 and bRule != state + 1:
                result = [result] * 2
                r = j
                break
        aRow = 0
        bRow = 0
        aRule = table[aRow][1]
        bRule = table[bRow][2]
        while aRule != 0 or bRule != 0:
            if aRule == state:
                result[0] += "a*"
                if aRow == bRow:
                    result[1] += "a*"
            if bRule == state:
                result[1] += "b*"
                if aRow == bRow:
                    result[0] += "b*"


    return result

main()

# Sample Input
# 3, 20, 32, 00
# 4, 21, 03, 40, 00
# 4, 12, 32, 04, 00
