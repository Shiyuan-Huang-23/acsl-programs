import math
import re

def main():
    with open("RegularExpressions.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            print("Pattern: " + currInput[0])
            s = re.compile(currInput[0])
            print("String: " + currInput[1])
            m = s.match(currInput[1])
            print(m)
            # may need to cut down regular expression to find max number of characters that can be generated
            # use | in place of union


main()

# https://docs.python.org/3.5/howto/regex.html

# Sample Input
# 1*110*, 10110
# (10)*1*, 1010100
# (01)*U(1*0), 0101110
