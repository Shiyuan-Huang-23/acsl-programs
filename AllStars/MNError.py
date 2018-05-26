def main():
    with open("MNError.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currIn = myInput[i].split(", ")
            mask = list(currIn[0])
            for j in range(len(mask)):
                mask[j] = int(mask[j])

def weight(mask, on, num):
    if len(mask) == 0:
        return False
    if len(mask) == 1 and num != mask[0]:
        return False
    currNum = [0] * len(mask)
    for i in range(len(mask)):
        currNum[i] = 1
        num -= mask[i]
        on -= 1
        if weight(mask[1:], on, num) != False:
        num += mask[i]
        on += 1
        currNum[i] = 0

main()

# 01236, 2, 8
# 01247, 2, 5
# 0012345, 2, 9
# 001234, 3, 6
# 12345, 2, 4
# 01236, 2, 0
# 01247, 2, 7
# 0012345, 2, 1
# 001234, 3, 3
# 12345, 2, 0
