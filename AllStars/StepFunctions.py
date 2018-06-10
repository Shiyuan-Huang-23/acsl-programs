def main():
    # array of letters that only give one number as input, for example x < t, x >= t, x = t
    oneX = ["A", "B", "C", "D", "I"]
    # the main problem is the x-coords
    # create a separate array that keeps track of the x-coords and their spaces away from the beginning
    with open("StepFunctions.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            arr = myInput[i].split(", ")
            graph = list()
            index = 1
            for j in range(int(arr[0])):
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

            # all x-values that need to be printed
            xVals = list()
            for seg in graph:
                if seg[2] not in xVals:
                    xVals.append(seg[2])
                if len(seg) == 4:
                    if seg[3] not in xVals:
                        xVals.append(seg[3])
            xVals.sort()
            print(xVals)

            # first look at ones that go to the left of the x value (A, D)
            # then do the ones directly above x-value (I)
            # then ones to the right (B, C, E, F, G, H)
            # make sure there are no repeats
            numSegSpaces = 1
            numXSpaces = 0
            xString = ""
            for j in range(len(xVals)):
                xCoord = xVals[j]
                # if this is the first x-coord, also look at left
                if j == 0:
                    temp = segInd(graph, xCoord, ["<***O", "<***@"])
                    if temp != -1:
                        graph[temp][1] = " " * numSegSpaces + graph[temp][1]
                        numSegSpaces += (len(graph[temp][1]) - 2)
                        numXSpaces = 6
                        xString = " " * numXSpaces + str(xCoord)
                temp = segInd(graph, xCoord, ["@"])
                if temp != -1:
                    graph[temp][1] = " " * numSegSpaces + graph[temp][1]
                    if xCoord not in xString:
                        xString += " " * (len(graph[temp][1]) + 1 - len(xString)) + str(xCoord)
                temp = segInd(graph, xCoord, ["O***>", "@***>", "O***O", "@***@", "O***@", "@***O"])
                if temp != -1:
                    graph[temp][1] = " " * numSegSpaces + graph[temp][1]
                    numSegSpaces += len(graph[temp][1]) - 1
                    if xCoord not in xString:
                        xString += " " * (len(graph[temp][1]) + 1 - len(xString)) + str(xCoord)
            for seg in graph:
                print(seg[0] + seg[1])

            # print(graph)
            # print(xString)
            # print(graph[0][1])
            # print(graph[1][1])
            print(xString)

                # look at directly above and to the right

            # currLen = 0
            # for j in range(len(xVals)):
            #     temp = list()
            #     for seg in graph:
            #         if seg[2:] == xVals[j]:
            #             temp.append(seg)
            #     if len(temp) == 1:
            #         for seg in graph:
            #             if seg[2:] == xVals[j]:
            #                 if j == 0:
            #                     seg[1] = " " + seg[1]
            #                 else:
            #                     seg[1] = (" " * currLen) + seg[1]
            #                 currLen = len(seg[1]) - 1
            #                 seg.append(True)
            #     else:
            #         found = False
            #         for line in temp:
            #             if "<" in line[1]:
            #                 for s in graph:
            #                     if s == line:
            #                         s.append(True)
            #                         print(s)
            #                         break
            #                 if j == 0:
            #                     seg[1] = " " + seg[1]
            #                 else:
            #                     seg[1] = (" " * currLen) + seg[1]
            #                 currLen = len(seg[1]) - 1
            #                 found = True
            #         if not found:
            #             for line in temp:
            #                 if line[1] == "@":
            #                     if j == 0:
            #                         seg[1] = " " + seg[1]
            #                     else:
            #                         seg[1] = (" " * currLen) + seg[1]
            #                     currLen = len(seg[1]) - 1
            #                     found = True
            #         if not found:
            #             for line in temp:
            #                 if ">" in line[1]:
            #                     if j == 0:
            #                         seg[1] = " " + seg[1]
            #                     else:
            #                         seg[1] = (" " * currLen) + seg[1]
            #                     currLen = len(seg[1]) - 1
            #         # seg.append(True)


            # for seg in graph:
            #     # prints y-value
            #     print(seg[0], end = "")
            #     print(seg[1])
            # # modify this so it will print correctly even if there are multiple conditions
            # # modify this so it will not print places where there are no overlaps or no undefineds
            # print("******" + graph[0][2])

# returns the index of the segment that contains the correct x-coord and the correct direction, -1 if not found
def segInd(graph, xCoord, direction):
    for i in range(len(graph)):
        seg = graph[i]
        if seg[2] == xCoord and seg[1] in direction:
            return i
    return -1

if __name__ == "__main__": main()

# Sample Input
# 2, 0, A, 2, 1, C, 2
# 2, 0, B, 1, 1, A, 1
# 2, 0, B, 2, 1, D, 2
# 3, 1, A, 0, 2, I, 0, 3, B, 0
# 2, 1, F, 0, 3, 0, B, 3
