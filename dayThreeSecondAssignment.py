#There are 323 lines, each 31 characters across
#Set initial variables
rowNum = 1
colNum = 0
tree = '#'
free = '.'
treesEncountered = 0

#Right 1 Down 1
with open("DayThreeInput.txt") as pathways:
	rowNum = 1
	colNum = 0
	treesEncountered = 0
	for row in pathways:
		print("\n \nYou're at position: ", rowNum, colNum)
		treePositions = [i for i, a in enumerate(row) if a == tree]
		print("There are trees at the following positions: ", treePositions)

		#Check if a tree was encountered
		if colNum in treePositions:
			treesEncountered = treesEncountered + 1
			print("You've hit ", treesEncountered, " trees.")

		colNum = colNum + 1
		rowNum = rowNum + 1
		if colNum > 30:
			colNum = colNum - 31
		r1d1Trees = treesEncountered

#Right 3 down 1
with open("DayThreeInput.txt") as pathways:
	rowNum = 1
	colNum = 0
	treesEncountered = 0
	for row in pathways:
		print("\n \nYou're at position: ", rowNum, colNum)
		treePositions = [i for i, a in enumerate(row) if a == tree]
		print("There are trees at the following positions: ", treePositions)

		#Check if a tree was encountered
		if colNum in treePositions:
			treesEncountered = treesEncountered + 1
			print("You've hit ", treesEncountered, " trees.")

		colNum = colNum + 3
		rowNum = rowNum + 1
		if colNum > 30:
			colNum = colNum - 31
		r3d1Trees = treesEncountered

#Right 5 Down 1
with open("DayThreeInput.txt") as pathways:
	rowNum = 1
	colNum = 0
	treesEncountered = 0
	for row in pathways:
		print("\n \nYou're at position: ", rowNum, colNum)
		treePositions = [i for i, a in enumerate(row) if a == tree]
		print("There are trees at the following positions: ", treePositions)

		#Check if a tree was encountered
		if colNum in treePositions:
			treesEncountered = treesEncountered + 1
			print("You've hit ", treesEncountered, " trees.")

		colNum = colNum + 5
		rowNum = rowNum + 1
		if colNum > 30:
			colNum = colNum - 31
		r5d1Trees = treesEncountered

#Right 7 down 1
with open("DayThreeInput.txt") as pathways:
	rowNum = 1
	colNum = 0
	treesEncountered = 0
	for row in pathways:
		print("\n \nYou're at position: ", rowNum, colNum)
		treePositions = [i for i, a in enumerate(row) if a == tree]
		print("There are trees at the following positions: ", treePositions)

		#Check if a tree was encountered
		if colNum in treePositions:
			treesEncountered = treesEncountered + 1
			print("You've hit ", treesEncountered, " trees.")

		colNum = colNum + 7
		rowNum = rowNum + 1
		if colNum > 30:
			colNum = colNum - 31
		r7d1Trees = treesEncountered

#Hard one, first use of 'continue'
#Right 1 Down 2
with open("DayThreeInput.txt") as pathways:
	rowNum = 1
	colNum = 0
	currentRow = 0
	treesEncountered = 0
	for row in pathways:
		currentRow = currentRow + 1
		if currentRow != rowNum:
			continue
		print("\n \nYou're at position: ", rowNum, colNum)
		treePositions = [i for i, a in enumerate(row) if a == tree]
		print("There are trees at the following positions: ", treePositions)

		#Check if a tree was encountered
		if colNum in treePositions:
			treesEncountered = treesEncountered + 1
			print("You've hit ", treesEncountered, " trees.")

		colNum = colNum + 1
		rowNum = rowNum + 2
		if colNum > 30:
			colNum = colNum - 31
		r1d2Trees = treesEncountered

totalTrees = int(r1d1Trees) * int(r3d1Trees) * int(r5d1Trees) * int(r7d1Trees) * int(r1d2Trees)
print("\nThere were: ", r1d1Trees, " on the first, ", r3d1Trees, " on the second, ", r5d1Trees, " on the third, ", r7d1Trees, " on the fourth, and ", r1d2Trees, " on the last.")
print("\nYou hit ", totalTrees, " trees total.")
