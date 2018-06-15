import math

def main():
    with open("Triangles.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            for j in range(len(currInput)):
                currInput[j] = int(currInput[j])
            xa = currInput[0]
            ya = currInput[1]
            xb = currInput[2]
            yb = currInput[3]
            xc = currInput[4]
            yc = currInput[5]
            # sides
            a = math.sqrt(((xc - xb) ** 2) + ((yc - yb) ** 2))
            b = math.sqrt(((xc - xa) ** 2) + ((yc - ya) ** 2))
            c = math.sqrt(((xb - xa) ** 2) + ((yb - ya) ** 2))
            # centroid
            # incenter
            x = (a * xa + b * xb + c * xc) / (a + b + c)
            y = (a * ya + b * yb + c * yc) / (a + b + c)
            print("INCENTER, " + decFormat(x) + ", " + decFormat(y))
            # circumcenter
            # orthocenter
            # area

def decFormat(x):
    return "{0:.2f}".format(x)

main()
