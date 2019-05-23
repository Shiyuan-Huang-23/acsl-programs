def coord(l, coords):
  return coords[ord(l) - 65]

def intersect(eq1, eq2):
  m1 = eq1[0]
  b1 = eq1[1]
  m2 = eq2[0]
  b2 = eq2[1]
  return ((b2 - b1) / (m1-m2))

def area(smallTriangle):
  distances = []
  smallTriangle.append(smallTriangle[0])
  for i in range(3):
    distances.append(distance(smallTriangle[i], smallTriangle[i + 1]))
  s = sum(distances) / 2
  a = (s * (s - distances[0]) * (s - distances[1]) * (s - distances[2])) ** 0.5
  return a

def distance(coord1, coord2):
  return ((((coord1[0] - coord2[0]) ** 2) + ((coord1[1] - coord2[1])**2)) ** 0.5)

with open("input.txt") as f:
    myList = [line.rstrip() for line in f]
    coords = []
    currIn = []
    for i in range(len(myList)):
      if i == 0:
        currIn = list(map(int, myList[i].split(", ")))
        for j in range(currIn[0]):
          coords.append([currIn[j * 2 + 1], currIn[(j + 1) * 2]])
        # print("Coords: " + str(coords))
      else:
        currIn = myList[i].split(", ")
        triangle = list(currIn[0])
        line = list(currIn[1])
        for j in range(len(triangle)):
          triangle[j] = coord(triangle[j], coords)
        for j in range(len(line)):
          line[j] = coord(line[j], coords) 
        # print("Triangle coords: " + str(triangle))
        # print("Line coords: " + str(line))
        lineEq = []
        lineEq.append((line[0][1] - line[1][1]) / (line[0][0] - line[1][0]))
        lineEq.append(line[0][1] - (lineEq[0] * line[0][0]))
        greater = []
        less = []
        for j in range(len(triangle)):
          x = triangle[j][0]
          y = triangle[j][1]
          if y > lineEq[0] * x + lineEq[1]:
            greater.append(triangle[j])
          else:
            less.append(triangle[j])
        one = []
        two = []
        if len(greater) == 2:
          two = greater
        else:
          one = greater
        if len(less) == 2:
          two = less
        else:
          one = less
        triangleEq = []
        m = (two[0][1] - one[0][1]) / (two[0][0] - one[0][0])
        b = one[0][1] - (m * one[0][0])
        triangleEq.append([m, b])
        m = (two[1][1] - one[0][1]) / (two[1][0] - one[0][0])
        b = one[0][1] - (m * one[0][0])
        triangleEq.append([m, b])
        smallTriangle = []
        smallTriangle.append(one[0])
        x = intersect(lineEq, triangleEq[0])
        y = lineEq[0] * x + lineEq[1]
        smallTriangle.append([x, y])
        x = intersect(lineEq, triangleEq[1])
        y = lineEq[0] * x + lineEq[1]
        smallTriangle.append([x, y])
        # print("Small Triangle Coords: " + str(smallTriangle))
        print("{0:.3f}".format(area(smallTriangle)))
  
# 6, 0, 0, 5, 5, 10, 0, 1, 6, 7, -3, 8, 6
# ABC, DE
# CBA, DE
# ABC, FE
# DEB, AF
# EDB, AC
# DAC, EB
# BEF, CD
# BEC, AF
# ADC, EF
# ABE, CD
