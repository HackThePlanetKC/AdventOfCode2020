target = 2020
with open("DayOneInput.txt") as numbers:
		for itemOne in numbers:
			with open("DayOneInput.txt") as numberTwo:
				for itemTwo in numberTwo:
					combined = int(itemOne) + int(itemTwo)
					#print(itemOne, " and ", itemTwo, " equal: ", combined)
					
					if int(itemOne) + int(itemTwo)==2020:
						print("Numbers are: ",itemOne,itemTwo)
						total= int(itemOne)*int(itemTwo)
						print("Solution is: ",total)
					#else:
						#print("No solutions found.")