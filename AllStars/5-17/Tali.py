def main():
    for i in range(10):
        rank = [{'1': 1, '3': 1, '4': 1, '6': 1}, {'6': 4}, {'6': 3, '4': 1}, {'6': 3, '3': 1}, {'6': 2, '4': 2}, {'6': 3, '1': 1}, {'6': 2, '4': 1, '3': 1}, {'6': 2, '3': 2}, {'6': 2, '4': 1, '1': 1}, {'6': 2, '3': 1, '1': 1}]
        arr = input(). split(", ")
        rankArr = [0] * 4
        rankLetters = ['A', 'B', 'C', 'D']
        tempArr = list()
        for a in range(len(arr)):
            temp = {}
            for c in arr[a]:
                if c in temp:
                    temp[c] += 1
                else:
                    temp[c] = 1
            for j in range(len(rank)):
                if rank[j] == temp:
                    rankArr[a] = [j, rankLetters[a]]
        for a in range(len(rankArr)):
            if rankArr[a] == 0:
                temp = list(arr[a])
                for b in range(len(temp)):
                    temp[b] = int(temp[b])
                rankArr[a] = [24 - sum(temp) + 11, rankLetters[a]]
        rankArr.sort()

        for a in range(len(rankArr)):
            for b in range(len(rankArr)):
                if a != b and rankArr[a][0] == rankArr[b][0]:
                    if highest(arr[rankLetters.index(rankArr[a][1])]) >  highest(arr[rankLetters.index(rankArr[b][1])]):
                        if b < a:
                            temp = rankArr[a]
                            rankArr[a] = rankArr[b]
                            rankArr[b] = temp
                    elif highest(arr[rankLetters.index(rankArr[b][1])]) > highest(arr[rankLetters.index(rankArr[a][1])]):
                        if b > a:
                            temp = rankArr[a]
                            rankArr[a] = rankArr[b]
                            rankArr[b] = temp

        for a in rankArr:
            print(a[1], end = "")
        print()

def highest(num):
    numList = list(num)
    for a in range(len(numList)):
        numList[a] = int(numList[a])
    return max(numList)

if __name__ == "__main__": main()

# Sample Input
# 6466, 6661, 4144, 4113
# 6431, 1443, 4331, 6643
# 6666, 6666, 6666, 1331
# 3434, 1166, 3313, 1144
# 6616, 4666, 4646, 6611

# Test Input
# 1643, 6663, 6643, 6631
# 6666, 4366, 3144, 1111
# 3166, 3366, 4646, 6646
# 1414, 1134, 1311, 4366
# 1343, 4144, 1616, 3131
# 1166, 3434, 3333, 3144
# 3133, 1414, 4444, 3434
# 1441, 6611, 4141, 1144
# 4666, 6466, 6643, 6664
# 1414, 3133, 4411, 1333
