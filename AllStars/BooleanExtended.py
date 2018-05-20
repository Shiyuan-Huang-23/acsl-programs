functions = ["!", "#", "$", "&", "%"]
functionInputs = [2, 3, 3, 3, 4]

def main():
    for i in range(10):
        expr = input()
        # determine all possible inputs
        letters = list()
        for j in expr:
            if j not in functions and j not in letters:
                letters.append(j)
        inputs = calcInputs(len(letters))
        # plug inputs into initial expression
        numTrue = 0
        for j in range(len(inputs)):
            arr = list(expr)
            for k in range(len(arr)):
                if arr[k] in letters:
                    arr[k] = inputs[j][letters.index(arr[k])]
            # if j == 3:
            #     print(evaluate(arr))
            if evaluate(arr)[0] == 1:
                numTrue += 1
        print(numTrue)

def calcInputs(n):
    output = list()
    for i in range(2 ** n):
        output.append(list())
    for i in range(n):
        for j in range(len(output)):
            output[j].append((j // (2 ** (n - i - 1))) % 2)
    return output

def evaluate(arr):
    i = 0
    while i < len(arr) and len(arr) > 1:
        if arr[i] in functions:
            function = functions.index(arr[i])
            startIndex = i - functionInputs[function]
            curr = arr[startIndex : i + 1]
            del arr[startIndex : i + 1]
            result = 0
            if function == 0:
                if curr[0] == curr[1]:
                    result = 1
            elif function == 1:
                count = 0
                for j in range(3):
                    if curr[j] == 1:
                        count += 1
                if count >= 2:
                    result = 1
            elif function == 2:
                count = 0
                for j in range(3):
                    if curr[j] == 0:
                        count += 1
                if count >= 2:
                    result = 1
            elif function == 3:
                count = 0
                for j in range(3):
                    if curr[j] == 1:
                        count += 1
                if count % 2 == 1:
                    result = 1
            elif function == 4:
                count = 0
                for j in range(4):
                    if curr[j] == 0:
                        count += 1
                if count % 2 == 1:
                    result = 1
            arr.insert(startIndex, result)
            i = 0
        i += 1
    return arr
    # go left to right
    # stop at each function
    # find start index for function
    # slice the correct # of inputs + function from arr
    # evaluate each function
    # place function result back at start index

if __name__ == "__main__": main()


# ABC#ABC$ABC&#
# ABC#ABC$!
# ABCD%AB!!
# DAB!A#

# AB!
# 2
# ABC$
# 4
# AAA#
# 1
# CAAB$!
# 4
# ABB!CD&!
# 8
# ABC!ABC!#!
# 4
# ABB#ADD$!
# 4
# AAAAA%DD!!!
# 2
# ABC$ABD&!BCD#ABCD%$
# 8
# C
# 1
