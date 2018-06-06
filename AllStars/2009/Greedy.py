def main():
    with open("Greedy.txt") as f:
        myList = [line.rstrip() for line in f]
        for i in range(2, len(myList)):
            paths = myList[1].split(", ")
            paths.sort()
            # print(str(paths) + ": " + myList[i][0] + ", " + myList[i][1])
            pathLists = findShortest(paths, myList[i][0], myList[i][1])
            # print(pathLists)
            lengths = list()
            for j in range(len(pathLists)):
                temp = 0
                for k in range(len(pathLists[j])):
                    temp += int(pathLists[j][k][2])
                lengths.append(temp)
            print(min(lengths))

def findShortest(paths, start, end):
    curr = list()
    if len(paths) == 0:
        # print("No more paths")
        return False
    else:
        for i in range(len(paths)):
            if start in paths[i]:
                # print("Start: " + start + " Path: " + paths[i])
                if paths[i].index(start) == 0:
                    otherNode = paths[i][1]
                elif paths[i].index(start) == 1:
                    otherNode = paths[i][0]
                if otherNode == end:
                    temp = list()
                    temp.append(paths[i])
                    curr.append(temp)
                else:
                    removed = paths.pop(i)
                    # print("Called findShortest(" + str(paths) + otherNode + ", " + end + ")")
                    result = findShortest(paths, otherNode, end)
                    if result != False:
                        for j in range(len(result)):
                            temp = list()
                            temp.append(removed)
                            for k in range(len(result[j])):
                                temp.append(result[j][k])
                            if temp not in curr:
                                curr.append(temp)
                    paths.append(removed)
                    paths.sort()
        if len(curr) > 0:
            # print(curr)
            return curr
        # print("Dead end")
        return False

if __name__ == "__main__": main()

# Sample Input
# 7
# AB8, CD6, EF7, AC4, CE2, BD3, DF5
# AE
# AD
# AF
# CF
# BE

# Test Input
# 13
# AD7, AB8, AC4, BC5, BD3, CD6, CE2, CF4, DF5, DE5, EF7, EG2, GF4
# AB
# AE
# AF
# BE
# BF
# CF
# AG
# BG
# CG
# DG
