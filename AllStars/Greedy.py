def main():
    with open("GreedyIn.txt") as f:
        myList = [line.rstrip() for line in f]
        paths = myList[1].split(", ")
        for i in range(2, len(myList)):
            currMin = 0
            for j in range(len(paths)):
                currMin += int(paths[j][2])
            findshortest(paths, myList[i][0], myList[i][1], currMin)

def findShortest(paths, start, end, currMin):
    if len(paths) == 0:
        return False

if __name__ == "__main__": main()
