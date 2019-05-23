with open("input.txt") as f:
  myList = [line.rstrip() for line in f]
  for i in range(len(myList)):
    currIn = myList[i]
    perm = sorted(list(currIn))
    counter = 1
    while "".join(perm) != currIn:
      counter += 1
      first = -1
      firstChr = ""
      maximum = 0
      second = -1
      for j in range(len(perm) - 1, 0, -1):
        if j - 1 < len(perm) and j - 1 > -1:
          if ord(perm[j-1]) < ord(perm[j]):
            first = j - 1
            firstChr = perm[j-1]
            maximum = ord(perm[j])
            break
      second = first + 1
      for j in range(first + 1, len(perm)):
        temp = ord(perm[j])
        if temp > ord(firstChr) and temp <= maximum:
          maximum = temp
          second = j
      temp = perm[first]
      perm[first] = perm[second]
      perm[second] = temp
      if first + 1 < len(perm):
        tail = perm[first + 1:][::-1]
        perm = perm[:first + 1] + tail
    print(counter)

# abc
# acsl
# motor
# mom
# nashua
# moot
# radius
# radii
# tattle
# rarara
