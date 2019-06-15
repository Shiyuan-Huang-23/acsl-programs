import re
import math

# gets the value of the loc field
def getValue(line, variables, varValues):
    if line[2] in variables:
        value = varValues[variables.index(line[2])]
    else:
        value = int(line[2][1:])
    return value

# conducts numeric operations
def operation(line, acc, variables, varValues):
    opcode = line[1]
    value = getValue(line, variables, varValues)
    if opcode == "ADD":
        acc += value
    elif opcode == "SUB":
        acc -= value
    elif opcode == "MULT":
        acc *= value
    elif opcode == "DIV":
        acc /= value
        if acc >= 0:
            acc = int(math.floor(acc))
        else:
            acc = int(math.ceil(acc))
    return acc

# returns the index to which a program should branch TimeoutError
def branch(line, acc, program):
    branch = False
    opcode = line[1]
    if opcode == "BU":
        branch = True
    elif opcode == "BG" and acc > 0:
        branch = True
    elif opcode == "BE" and acc == 0:
        branch = True
    elif opcode == "BL" and acc < 0:
        branch = True
    if branch == False:
        return (program.index(line) + 1)
    else:
        loc = line[2]
        for i in range(len(program)):
            if program[i][0] == loc:
                return i

# interprets the program
def interpret(program, readInput):
    acc = None
    variables = []
    varValues = []
    i = 0
    while i < len(program):
        line = program[i]
        i += 1
        opcode = line[1]
        if opcode in ["ADD", "SUB", "MULT", "DIV"]:
            acc = operation(line, acc, variables, varValues)
        elif opcode in ["BG", "BE", "BL", "BU"]:
            i = branch(line, acc, program)
        elif opcode == "LOAD":
            acc = getValue(line, variables, varValues)
        elif opcode in ["STORE", "READ"]:
            if line[2] not in variables:
                variables.append(line[2])
                if opcode == "STORE":
                    varValues.append(acc)
                elif opcode == "READ":
                    varValues.append(readInput[0])
                    readInput = readInput[1:]
            else:
                index = variables.index(line[2])
                varValues[index] = acc
        elif opcode == "DC":
            variables.append(line[0])
            varValues.append(int(line[2]))
        elif opcode == "END":
            break
    return acc

with open("as7-sample.txt") as f:
        # take input and separate the programs
        tempList = [line.rstrip() for line in f]
        myList = []
        while "" in tempList:
            myList.append(tempList[:tempList.index("")])
            tempList = tempList[tempList.index("") + 1:]
        myList.append(tempList)
        for i in range(len(myList)):
            program = myList[i]
            # handles integer input in first line
            readInput = list(map(int, program[0].split(" ")))
            program = program[1:]
            # splits each line so the opcode is at index 1
            for j in range(len(program)):
                program[j] = re.split(r"\s+", program[j])
            print(interpret(program, readInput))
