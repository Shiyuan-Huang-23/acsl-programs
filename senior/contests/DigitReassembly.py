def main():
    for i in range(5):
        # take input
        currIn = input("Enter the numbers: ")
        number = currIn.split(" ")[0]
        n = int(currIn.split(" ")[1])
        sumArr = []
        while len(number) >= n:
            sumArr.append(int(number[:n]))
            number = number[n:]
        if len(number) > 0:
            pad = n - len(number)
            number += ("0" * pad)
            sumArr.append(int(number))
            number = ""
        print(sum(sumArr))

if __name__ == "__main__": main()

# Sample Input
# 13256709 3
# 3587612098 1
# 265472 5
# 3126854901231 4
# 25768437216701562 7

# Sample Output
# 789
# 49
# 46547
# 12798
# 15413544

# My Sample Input
# 132 4
# 505505505505505505505505505505 6

# My Sample Output
# 1320
# 2527525
