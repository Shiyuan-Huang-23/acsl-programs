def main():
    pattern = [0, 1, 2, 2, 1, 0]
    for i in range(1):
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
