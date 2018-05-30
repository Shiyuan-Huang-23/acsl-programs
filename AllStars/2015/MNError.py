def main():
    with open("MNError.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currIn = myInput[i].split(", ")
            mask = list(currIn[0])
            for j in range(len(mask)):
                mask[j] = int(mask[j])
            result = weight(mask, int(currIn[1]), int(currIn[2]), [0] * len(mask))
            if result == False:
                print("NONE")
            else:
                for j in range(len(result)):
                    for k in range(len(result[j])):
                        result[j][k] = str(result[j][k])
                    print("".join(result[j]), end = "")
                    if j != len(result) - 1:
                        print(", ", end = "")
                print()


def weight(mask, bitsOn, target, bits):
    output = []
    if bitsOn == 0:
        if target == 0:
            # print("It worked " + str(bits))
            return [bits]
        else:
            return False
    if bitsOn > len(mask):
        return False
    for i in range(len(mask)):
        bits[i] = 1
        # print("Assigned a 1 " + str(bits))
        result = weight(mask[i + 1:], bitsOn - 1, target - mask[i], bits[i + 1:])
        if result != False:
            if len(result) == 0:
                output.append(bits[: i + 1])
                # print("Appended to output " + str(output))
            else:
                for j in range(len(result)):
                    output.append(bits[:i + 1] + result[j])
                    # print("Appended to output " + str(output))
        # else:
        #     print("Didn't work, moving on " + str(bits))
        bits[i] = 0
    if len(output) == 0:
        return False
    else:
        return output

main()

# Sample Input
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

# Test Input
# 001248, 3, 7
# 001245, 3, 8
# 001236, 2, 2
# 001226, 3, 9
# 12345, 2, 5
# 001248, 3, 0
# 001245, 3, 5
# 001236, 2, 6
# 001226, 3, 0
# 012345, 2, 5
