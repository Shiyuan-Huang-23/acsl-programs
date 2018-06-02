def main():
    with open("BinPackingIn.txt") as f:
        myList = [line.rstrip('\n') for line in f]
        for i in range(2):
            arr = myList[i].split(", ")
            for j in range(len(arr)):
                arr[j] = int(arr[j])
            barr = arr[0:]
            bins = [[0]]
            for n in arr:
                found = False
                for i in range(len(bins)):
                    if bins[i][0] + n <= 10:
                        bins[i][0] += n
                        found = True
                        break
                if not found:
                    bins.append([n])
            printBins(bins)
            bins = [[0]]
            arr.sort()
            for n in arr:
                found = False
                for i in range(len(bins)):
                    if bins[i][0] + n <= 10:
                        bins[i][0] += n
                        found = True
                        break
                if not found:
                    bins.append([n])
            printBins(bins)
            bins = [[0]]
            arr.sort(reverse = True)
            for n in arr:
                found = False
                for i in range(len(bins)):
                    if bins[i][0] + n <= 10:
                        bins[i][0] += n
                        found = True
                        break
                if not found:
                    bins.append([n])
            printBins(bins)
            bins = [[0]]
            for n in barr:
                currMax = -1
                index = 0
                for i in range(len(bins)):
                    if bins[i][0] + n <= 10:
                        if bins[i][0] > currMax:
                            index = i
                            currMax = bins[i][0]
                if bins[index][0] + n <= 10:
                    bins[index][0] += n
                else:
                    bins.append([n])
            printBins(bins)
            bins = [[0]]
            for n in barr:
                currMin = 10
                index = 0
                for i in range(len(bins)):
                    if bins[i][0] + n <= 10:
                        if bins[i][0] < currMin:
                            index = i
                            currMin = bins[i][0]
                if bins[index][0] + n <= 10:
                    bins[index][0] += n
                else:
                    bins.append([n])
            printBins(bins)
            # print(bins)
def printBins(bins):
    for n in range(len(bins)):
        if n != len(bins) - 1:
            print(str(bins[n][0]) + ", ", end = "")
        else:
            print(str(bins[n][0]))

# Sample Input            
# 1, 3, 5, 3, 6, 2, 1, 2, 4, 6, 3, 7, 0

# Test Input
# 2, 9, 4, 7, 1, 3, 2, 6, 8, 1, 4, 2, 5, 3, 4, 0
# 1, 4, 2, 8, 2, 1, 6, 3, 4, 5, 2, 2, 7, 3, 1, 5, 2, 0


__author__ = 'BHS-programing'

if __name__ == "__main__": main()
