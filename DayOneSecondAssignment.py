target = 2020
with open("DayOneInput.txt") as numbers:
		for itemOne in numbers:
			with open("DayOneInput.txt") as numberTwo:
				for itemTwo in numberTwo:
					with open("DayOneInput.txt") as numberThree:
						for itemThree in numberThree:
							combined = int(itemOne) + int(itemTwo) + int(itemThree)
							#print(itemOne, " and ", itemTwo, "and ", itemThree, " equal: ", combined)
							
							if int(itemOne) + int(itemTwo) + int(itemThree)==target:
								print("Numbers are: ",itemOne,itemTwo,itemThree)
								total= int(itemOne)*int(itemTwo)*int(itemThree)
								print("Solution is: ",total)
							#else:
								#print("No solutions found.")