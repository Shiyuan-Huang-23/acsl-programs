def main():
    with open("Triangles.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")

main()
