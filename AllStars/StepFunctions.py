def main():
    oneX = ["A", "B", "C", "D", "I"]
    # the main problem is the x-coords
    # create a separate array that keeps track of the x-coords and their spaces away from the beginning
    with open("StepFunctions.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            arr = myInput[i].split(", ")
            graph = list()
            index = 1
            for i in range(int(arr[0])):
                seg = list()
                # y height
                seg.append(arr[index])
                # direction
                direc = arr[index + 1]
                if direc == "A":
                    seg.append("<***O")
                elif direc == "B":
                    seg.append("O***>")
                elif direc == "C":
                    seg.append("@***>")
                elif direc == "D":
                    seg.append("<***@")
                elif direc == "E":
                    seg.append("O***O")
                elif direc == "F":
                    seg.append("@***@")
                elif direc == "G":
                    seg.append("O***@")
                elif direc == "H":
                    seg.append("@***O")
                elif direc == "I":
                    seg.append("@")
                # x place
                seg.append(arr[index + 2])
                if direc in oneX:
                    index += 3
                else:
                    # second x place if it's a segment
                    seg.append(arr[index + 3])
                    index += 4
                graph.append(seg)
            for seg in graph:
                print(seg)
            # sorts graph segments so they are in descending order by y-values
            graph.sort(reverse = True)
            # modify this so extra spaces are added if there are extra conditions, including single digits "I"
            # grab all x-values to determine which segment is leftest and which is rightest
            # suppose that the x-values are 2, 4, 6, 8
            # the leftmost will be the segment with only 2 or both 2 and 4
            # the nextmost will be the segment with only 4
            # add spaces based on how leftmost they are, + 1 extra space
            # these extra spaces should take into account the lengths of the segments on their lefts
            xVals = list()
            for seg in graph:
                xVals.append(seg[2:])
            print(xVals)
            xVals.sort()
            print(xVals)
            currLen = 0
            for j in range(len(xVals)):
                temp = list()
                for seg in graph:
                    if seg[2:] == xVals[j]:
                        temp.append(seg)
                if len(temp) == 1:
                    for seg in graph:
                        if seg[2:] == xVals[j]:
                            if j == 0:
                                seg[1] = " " + seg[1]
                            else:
                                seg[1] = (" " * currLen) + seg[1]
                            currLen = len(seg[1]) - 1
                            seg.append(True)
                else:
                    found = False
                    for line in temp:
                        if "<" in line[1]:
                            for s in graph:
                                if s == line:
                                    s.append(True)
                                    print(s)
                                    break
                            if j == 0:
                                seg[1] = " " + seg[1]
                            else:
                                seg[1] = (" " * currLen) + seg[1]
                            currLen = len(seg[1]) - 1
                            found = True
                    if not found:
                        for line in temp:
                            if line[1] == "@":
                                if j == 0:
                                    seg[1] = " " + seg[1]
                                else:
                                    seg[1] = (" " * currLen) + seg[1]
                                currLen = len(seg[1]) - 1
                                found = True
                    if not found:
                        for line in temp:
                            if ">" in line[1]:
                                if j == 0:
                                    seg[1] = " " + seg[1]
                                else:
                                    seg[1] = (" " * currLen) + seg[1]
                                currLen = len(seg[1]) - 1
                    # seg.append(True)


            for seg in graph:
                # prints y-value
                print(seg[0], end = "")
                print(seg[1])
            # modify this so it will print correctly even if there are multiple conditions
            # modify this so it will not print places where there are no overlaps or no undefineds
            print("******" + graph[0][2])

if __name__ == "__main__": main()

# Sample Input
# 2, 0, A, 2, 1, C, 2
# 2, 0, B, 1, 1, A, 1
# 2, 0, B, 2, 1, D, 2
# 3, 1, A, 0, 2, I, 0, 3, B, 0
# 2, 1, F, 0, 3, 0, B, 3
