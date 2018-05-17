def main():
    for i in range(1):
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

        while True:
            changed = False
            for a in range(len(rankArr)):
                for b in range(len(rankArr)):
                    if a != b and rankArr[a][0] == rankArr[b][0]:
                        if highest(arr[a]) >  highest(arr[b]):
                            if b < a:
                                temp = rankArr[a]
                                rankArr[a] = rankArr[b]
                                rankArr[b] = temp
                                changed = True
                                print(rankArr)
                                break
                        elif highest(arr[b]) > highest(arr[a]):
                            if b > a:
                                temp = rankArr[a]
                                rankArr[a] = rankArr[b]
                                rankArr[b] = temp
                                changed = True
                                print(rankArr)
                                break
                if changed:
                    break
            if not changed:
                break
        for a in rankArr:
            print(a[1], end = "")
        print(rankArr)

def highest(num):
    numList = list(num)
    for a in range(len(numList)):
        numList[a] = int(numList[a])
    return max(numList)

if __name__ == "__main__": main()

# 6466, 6661, 4144, 4113
