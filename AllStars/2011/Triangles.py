import math

# check if first slope is undefined
# if it is undefined, set x = xa or xb or xc, set y = value when x is plugged into equation 2
# check if second slope is undefined
# if it is undefined, use same procedure as above

def main():
    with open("Triangles.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            for j in range(len(currInput)):
                currInput[j] = float(currInput[j])
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
            undefined = False
            try:
                m1 = (((yb + yc) / 2) - ya) / (((xb + xc) / 2) - xa)
            except:
                undefined = [True, 1]
            try:
                m2 = (((yb + ya) / 2) - yc) / (((xb + xa) / 2) - xc)
            except:
                undefined = [True, 2]
            if undefined == False:
                b1 = ya - (m1 * xa)
                b2 = yc - (m2 * xc)
                x = (b2 - b1) / (m1 - m2)
                y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
            elif undefined == [True, 1]:
                x = xa
                b2 = yc - (m2 * xc)
                y = m2 * x + b2
            elif undefined == [True, 2]:
                x = xc
                b1 = ya - (m1 * xa)
                y = m1 * x + b1
            print("CENTROID, " + decFormat(x) + ", " + decFormat(y))
            # incenter
            x = (a * xa + b * xb + c * xc) / (a + b + c)
            y = (a * ya + b * yb + c * yc) / (a + b + c)
            print("INCENTER, " + decFormat(x) + ", " + decFormat(y))
            # circumcenter
            undefined = False
            try:
                m1 = -((xc - xb) / (yc - yb))
            except:
                undefined = [True, 1]
            try:
                m2 = -((xb - xa) / (yb - ya))
            except:
                undefined = [True, 2]
            if undefined == False:
                b1 = ((yb + yc) / 2) - (m1 * ((xb + xc) / 2))
                b2 = ((ya + yb) / 2) - (m2 * ((xa + xb) / 2))
                x = (b2 - b1) / (m1 - m2)
                y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
            elif undefined == [True, 1]:
                x = ((xb + xc) / 2)
                b2 = ((ya + yb) / 2) - (m2 * ((xa + xb) / 2))
                y = m2 * x + b2
            elif undefined == [True, 2]:
                x = ((xa + xb) / 2)
                b1 = ((yb + yc) / 2) - (m1 * ((xb + xc) / 2))
                y = m1 * x + b1
            print("CIRCUMCENTER, " + decFormat(x) + ", " + decFormat(y))
            # orthocenter
            undefined = False
            try:
                m1 = -((xc - xb) / (yc - yb))
            except:
                undefined = [True, 1]
            try:
                m2 = -((xb - xa) / (yb - ya))
            except:
                undefined = [True, 2]
            if undefined == False:
                b1 = ya - (m1 * xa)
                b2 = yc - (m2 * xc)
                x = (b2 - b1) / (m1 - m2)
                y = ((m2 * b1) - (m1 * b2)) / (m2 - m1)
            elif undefined == [True, 1]:
                x = xa
                b2 = yc - (m2 * xc)
                y = m2 * x + b2
            elif undefined == [True, 2]:
                x = xc
                b1 = ya - (m1 * xa)
                y = m1 * x + b1
            print("ORTHOCENTER, " + decFormat(x) + ", " + decFormat(y))
            # area
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("AREA, " + decFormat(area))

def decFormat(x):
    return "{0:.2f}".format(x)

main()

# Sample Input
# -2, 4, 4, 2, 0, -6

# Test Input
# -2, 7, 7, 4, 1, -2
# -4, 0, 4, 0, 0, 6.93
