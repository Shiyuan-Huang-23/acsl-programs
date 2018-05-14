def main():
    pattern = [0, 1, 2, 2, 1, 0]
    for i in range(10):
        arr = input().split(", ")
        n = int(arr[1])
        result = ""
        index = 0
        while 3 ** index <= n:
            digit = pattern[(int((n - 1) / (3 ** index))) % 6]
            result = str(digit) + result
            index += 1
        while int(arr[0]) > len(result):
            result = "0" + result
        print(result)

if __name__ == "__main__": main()

# 1, 2
# 2, 7
# 3, 22
# 4, 75
# 5, 127

# 1
# 20
# 212
# 2202
# 11200

# 1, 1
# 2, 4
# 5, 150
# 3, 20
# 4, 60
# 3, 23
# 5, 135
# 4, 48
# 5, 100
# 3, 15

# 0
# 12
# 10110
# 201
# 2010
# 211
# 11222
# 1020
# 12022
# 112
