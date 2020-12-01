target = 2020
with open("DayOneInput.txt") as numbers:
		for itemOne in numbers:
			for itemTwo in numbers:
				for itemThree in numbers:
					combined = int(itemOne) + int(itemTwo) + int(itemThree)
					#print(itemOne, " and ", itemTwo, "and ", itemThree, " equal: ", combined)
							
					if int(itemOne) + int(itemTwo) + int(itemThree)==target:
						print("Numbers are: ",itemOne,itemTwo,itemThree)
						total= int(itemOne)*int(itemTwo)*int(itemThree)
						print("Solution is: ",total)
					#else:
						#print("No solutions found.")
