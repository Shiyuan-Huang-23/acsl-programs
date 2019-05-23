def gate(l, arr):
    zeroCount = count("0", arr)
    oneCount = count("1", arr)

    if l == "A":
        if zeroCount == 3:
            return "1"
        else:
            return "0"
    elif l == "B":
        if oneCount <= 1:
            return "1"
        else:
            return "0"
    elif l == "C":
        if oneCount == 3:
            return "1"
        else:
            return "0"
    elif l == "D":
        if oneCount <= 2:
            return "1"
        else:
            return "0"

def count(t, arr):
    n = 0
    for i in arr:
        if i == t:
            n += 1
    return n

with open("input.txt") as f:
    myList = [line.rstrip() for line in f]
    for i in range(len(myList)):
        currIn = myList[i].split(", ")
        receivers = []
        for j in range(int(currIn[0])):
          first = currIn[j * 2 + 1]
          inputArr = bin(int(first[1]))[2:]
          inputArr = list(((3 - len(inputArr)) * "0") + inputArr)
          output = gate(first[0], inputArr)
          second = list(currIn[(j + 1) * 2])
          for k in second:
            found = False
            for l in range(len(receivers)):
              if receivers[l][0] == k:
                found = True
                receivers[l][1].append(output)
                continue
            if found == False:
              receivers.append([k, [output]])
        receivers = sorted(receivers)
        # if len(receivers) == 1:
        #   print("".join(receivers[1]))
        if len(receivers) == 1:
          print("".join(receivers[0][1]))
        for j in range(len(receivers)):
            receivers[j] = gate(receivers[j][0], receivers[j][1])
        if len(receivers) == 3:
          
          print("".join(receivers))
          print(gate(currIn[-1], receivers))
        else:
          print(receivers[0])

# 4, A7, B, B3, BCD, C5, BCD, D0, CD, C
# 3, A7, D, B3, D, C5, D, D
# 3, A0, B, B4, B, C6, B, B
# 3, A7, ACD, B6, ACD, C5, ACD, B
# 4, A0, AC, B1, AB, C2, ABC, D3, BC, A
