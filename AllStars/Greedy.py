def main():
    with open("GreedyIn.txt") as f:
        myList = [line.rstrip() for line in f]
        paths = myList[1].split(", ")
        for i in range(2, len(myList)):
            currMin = 0
            for j in range(len(paths)):
                currMin += int(paths[j][2])
            print(findShortest(paths, myList[i][0], myList[i][1]))
            # findShortest(paths, myList[i][0], myList[i][1], currMin)

def findShortest(paths, start, end):
    curr = list()
    if len(paths) == 0:
        return False
    else:
        for i in range(len(paths)):
            if start in paths[i]:
                if paths[i].index(start) == 0:
                    otherNode = paths[i][1]
                elif paths[i].index(start) == 1:
                    otherNode = paths[i][0]
                if otherNode == end:
                    return paths[i]
                removed = paths.pop(i)
                result = findShortest(paths, otherNode, end)
                print(result)
                if result != False:
                    temp = list()
                    temp.append(removed)
                    temp.append(result)
                    if temp not in curr:
                        curr.append(temp)
                paths.append(removed)
        if len(curr) > 0:
            return curr
        return False

# def findShortest(paths, start, end, currMin):
#     currLen = list()
#     if len(paths) == 0:
#         return False
#     else:
#         for i in range(len(paths)):
#             currLength = 0
#             # print(paths)
#             if start in paths[i]:
#                 if paths[i].index(start) == 0:
#                     otherNode = paths[i][1]
#                 elif paths[i].index(start) == 1:
#                     otherNode = paths[i][0]
#                 if otherNode == end:
#                     currLen.append(int(paths[i][2]) + currLength)
#                 removed = paths.pop(i)
#                 # print(paths)
#                 result = findShortest(paths, otherNode, end, currMin)
#                 if result != False:
#                     currLen.append(result)
#                 paths.append(removed)
#         if len(currLen) > 0:
#             return currLen
#         return False


if __name__ == "__main__": main()
