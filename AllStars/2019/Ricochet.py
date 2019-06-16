# provides the required output given table dimensions and coords
def formatOutput(w, h, endX, endY):
	output = -1
	if endX in [0, w] and endY in [0, h]:
		if endX > endY:
			output = endX
		else:
			output = endY
	elif endX in [0, w]:
		output = endY
	elif endY in [0, h]:
		output = endX
	if output - int(output) >= 0.5:
		output = int(output) + 1
	else: 
		output = int(output)
	return output

# returns the coordinates of the next wall hit and the new vectors
def ricochet(w, h, startX, startY, xVector, yVector):
	# find new vectors
	# if hit corner, vectors switch
	if startX in [0, w] and startY in [0, h]:
		temp = xVector
		xVector = yVector
		yVector = temp
	# if hit left or right, xVector negates
	elif startX in [0, w]:
		xVector *= -1
	# if hit top or bottom, yVector negates
	elif startY in [0, h]:
		yVector *= -1

	# find next place ball will hit a wall
	xTargets = [0, w]
	someNumX = -1
	for i in range(len(xTargets)):
		target = xTargets[i]
		someNumX = (target - startX) / xVector
		if someNumX > 0:
			break
	yTargets = [0, h]
	someNumY = -1
	for i in range(len(yTargets)):
		target = yTargets[i]
		someNumY = (target - startY) / yVector
		if someNumY > 0:
			break
	if someNumX < someNumY:
		endX = startX + (someNumX * xVector)
		endY = startY + (someNumX * yVector)
	else:
		endX = startX + (someNumY * xVector)
		endY = startY + (someNumY * yVector)
	return [endX, endY, xVector, yVector]

with open("as8-sample.txt") as f:
	myList = [line.rstrip() for line in f]
	for i in range(len(myList)):
		# assign variables to input
		currIn = list(map(int, myList[i].split(" ")))
		w = currIn[0]
		h = currIn[1]
		startX = currIn[2]
		startY = currIn[3]
		endX = currIn[4]
		endY = currIn[5]
		k = currIn[6]
		
		if k == 0:
			print(formatOutput(w, h, startX, startY))
		elif k == 1:
			print(formatOutput(w, h, endX, endY))
		else:
			xVector = endX - startX
			yVector = endY - startY
			# handles undefined or zero slopes
			if xVector == 0 or yVector == 0:
				print(formatOutput(w, h, endX, endY))
			else:
				for j in range(k - 1):
					startX = endX
					startY = endY
					arr = ricochet(w, h, startX, startY, xVector, yVector)
					endX = arr[0]
					endY = arr[1]
					xVector = arr[2]
					yVector = arr[3]
				print(formatOutput(w, h, endX, endY))


# 20 15 11 7 17 15 2
# 20 15 15 12 20 0 2
# 10 6 5 3 8 6 4
