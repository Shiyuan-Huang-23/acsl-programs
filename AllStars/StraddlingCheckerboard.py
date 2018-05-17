def main():
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for j in range(5):
        arr = input().split(", ")
        table = list()
        for i in range(3):
            temp = [0] * 10
            table.append(temp)
        hashes = list()
        for x in range(10):
            table[0][x] = arr[0][x: x + 1]
            if arr[0][x: x + 1] == "#":
                hashes.append((10 + int(arr[2]) + x) % 10)
        hashes.sort()
        row = 1
        col = 0
        for a in alpha:
            if not inTable(a, table):
                table[row][col] = a
                col += 1
                if col == 10:
                    col = 0
                    row += 1
        table[2][8] = "."
        table[2][9] = "/"
        output = ""
        encrypt = list(arr[1])
        # print(encrypt)
        for i in range(len(encrypt)):
            for r in range(3):
                for c in range(10):
                    if table[r][c] == encrypt[i]:
                        if r > 0:
                            output += str(hashes[r - 1])
                            output += " "
                        output += str((10 + int(arr[2]) + c) % 10)
                        output += " "
        # print(hashes)
        # print(table)
        print(output)

def inTable(a, table):
    for i in range(10):
        if table[0][i] == a:
            return True
    return False

if __name__ == "__main__": main()
