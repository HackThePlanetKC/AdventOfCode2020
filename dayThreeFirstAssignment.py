#There are 323 lines, each 31 characters across
#Set initial variables
rowNum = 1
colNum = 0
tree = '#'
free = '.'
treesEncountered = 0
with open("DayThreeInput.txt") as pathways:
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

print("You hit ", treesEncountered, " trees total.")