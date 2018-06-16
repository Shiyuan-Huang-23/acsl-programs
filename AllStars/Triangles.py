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
            m1 = (((yb + yc) / 2) - ya) / (((xb + xc) / 2) - xa)
            b1 = ya - (m1 * xa)
            m2 = (((yb + ya) / 2) - yc) / (((xb + xa) / 2) - xc)
            b2 = yc - (m2 * xc)
            x = (b2 - b1) / (m1 - m2)
            y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
            print("CENTROID, " + decFormat(x) + ", " + decFormat(y))
            # incenter
            x = (a * xa + b * xb + c * xc) / (a + b + c)
            y = (a * ya + b * yb + c * yc) / (a + b + c)
            print("INCENTER, " + decFormat(x) + ", " + decFormat(y))
            # circumcenter
            m1 = -(xb - xc) / (yb - yc)
            b1 = ((yb + yc) / 2) - (m1 * ((xb + xc) / 2))
            mx = -(xb - xa) / (yb - ya)
            b2 = ((ya + yb) / 2) - (m2 * ((xa + xb) / 2))
            x = (b2 - b1) / (m1 - m2)
            y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
            print("CIRCUMCENTER, " + decFormat(x) + ", " + decFormat(y))
            # orthocenter
            # area
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("AREA, " + decFormat(area))

def decFormat(x):
    return "{0:.2f}".format(x)

main()
