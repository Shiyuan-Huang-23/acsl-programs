import re

def main():
    strings = input("Enter the 10 strings separated by commas and spaces: ").split(", ")
    for i in range(5):
        pattern = input("Enter the search string: ")
        if "?" in pattern:
            pattern = pattern.replace("?", ".")
        if "*" in pattern:
            pattern = pattern.replace("*", ".*")
        matches = []
        for i in range(len(strings)):
            match = re.fullmatch(pattern, strings[i])
            if match:
                matches.append(strings[i])
        if len(matches) > 0:
            print(", ".join(matches))
        else:
            print("No Match")

if __name__ == "__main__": main()

# Sample Input
# 2BELLS, T4LLS, FALLS, DOL3LS, DUL7LS, DOLLIES, BELLY, BELLIES, TELLY, DELL
# *LLS
# [2-5]BELLS
# *L?LS
# *BELL*
# *L[1-8]*

# Test Input
# PEACH, TEACH, EACH, PREA4CH, REACH, PREA2CHER, TEACHER, ACHE, ARCHER, RESEARCH
# *A?CH
# *ACH*
# *A[2-4]*
# ?EACH*
# *C*
