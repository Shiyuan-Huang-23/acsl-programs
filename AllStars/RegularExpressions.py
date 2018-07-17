def main():
    with open("RegularExpressions.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            print(match(currInput[0], currInput[1]))

def match(regex, text):
    # longest substring of the text that can be matched
    matched = ""
    textIndex = 0
    done = False
    for i in range(len(regex)):
        # no Kleene star
        if textIndex > len(text) - 1:
            break
        if regex[i] == text[textIndex]:
            matched += regex[i]
            textIndex += 1
            if i == len(regex) - 1:
                done = True
        else:
            break
    if matched == text and done:
        return "YES"
    else:
        return textIndex
    return [regex, text]
main()

# import re

# def main():
#     number = 1
#     with open("RegularExpressions.txt") as f:
#         myInput = [line.rstrip() for line in f]
#         for i in range(len(myInput)):
#             currInput = myInput[i].split(", ")
#             # print("Pattern: " + currInput[0])
#             pattern = list(currInput[0])
#             finished = False
#             while not finished:
#                 finished = True
#                 for j in range(len(pattern)):
#                     if pattern[j] == " ":
#                         del pattern[j]
#                         finished = False
#                         break
#                     elif pattern[j] == "U":
#                         pattern[j] = "|"
#             currInput[0] = "".join(pattern)
#             s = re.compile(currInput[0])
#             # print("String: " + currInput[1])
#             m = s.match(currInput[1])
#             # print(m)
#             if m != None and m.group() == currInput[1]:
#                 print(str(number) + ". Yes")
#                 number += 1
#             else:
#                 if m != None and m.start() == 0:
#                     print(str(number) + ". No, ", end = "")
#                     number += 1
#                     temp = currInput[0][:-1]
#                     index = []
#                     index.append(m.end())
#                     while len(temp) > 0:
#                         try:
#                             s = re.compile(temp)
#                             m = s.match(currInput[1])
#                             if m != None and m.start() == 0:
#                                 index.append(m.end())
#                             temp = temp[:-1]
#                         except:
#                             temp = temp[:-1]
#                     s = re.compile(currInput[0])
#                     print(s)
#                     m = s.match(currInput[1])
#                     temp = currInput[1][:-1]
#                     while len(temp) > 0:
#                         m = s.match(temp)
#                         if m != None and m.start() == 0:
#                             print(m)
#                             index.append(m.end())
#                         temp = temp[:-1]
#                     print(max(index))
#                 else:
#                     print(str(number) + ". No, ", end = "")
#                     number += 1
#                     temp = currInput[0][:-1]
#                     index = []
#                     while len(temp) > 0:
#                         s = re.compile(temp)
#                         m = s.match(currInput[1])
#                         if m != None and m.start() == 0:
#                             index.append(m.end())
#                         temp = temp[:-1]
#                     s = re.compile(currInput[0])
#                     m = s.match(currInput[1])
#                     temp = currInput[1][:-1]
#                     while len(temp) > 0:
#                         m = s.match(temp)
#                         if m != None and m.start() == 0:
#                             index.append(m.end())
#                         temp = temp[:-1]
#                     print(max(index))
#             # may need to cut down regular expression to find max number of characters that can be generated
#             # s = re.compile("(01)*|(1*0)")
#             # m = s.match("10")



# main()

# Works
# s = re.compile("1(1|0)*")
# m = s.match("10100000111")

# Does not work
# s = re.compile("(01)*|(1*0)") # doesn't match second condition
# m = s.match("11110")

# https://docs.python.org/3.5/howto/regex.html

# Sample Input
# 1*110*, 10110
# (10)*1*, 1010100
# (01)*U(1*0), 0101110

# Test Input
# 10*1, 101
# 1*0*, 110001
# (0*101*)*, 0010110101
# 11*10*, 110110
# 0*1, 0000011
# 1*0*1, 1110001001
# (1*0)*0, 1111001100
# (010*)*, 0101000110001 # incorrect end index
# (01*) U (0*1), 10110 # how the hell is this one actually right?
# ((00*1) U (101) U1*)*, 1010111111111010 # how the hell is THIS one actually right??????
