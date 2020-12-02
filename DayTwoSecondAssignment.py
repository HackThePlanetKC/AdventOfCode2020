passCount = 0
validPass = 0
passLow = int
passHigh = int
#passCount = int
with open("DayTwoInput.txt") as password:
	for item in password:
		passRange,letter,passwd = item.split(" ")
		passLow,passHigh = passRange.split("-")
		letter = letter[:-1]

		#Don't need the count anymore for second assignment
		#passCount = passwd.count(letter)

		#Decrementing the range to get index value
		passLow = int(passLow) - 1
		passHigh = int(passHigh) - 1

		#Finding all the index positions of the letter
		indices = [i for i, a in enumerate(passwd) if a == letter]
		

		#Test for working	
		print("\n",passwd)
		print("Original range was: ", passRange)	
		print("Index values are: ", passLow, " and ", passHigh)
		print("letter is ", letter)
		print(indices)
		if (passLow in indices) is not (passHigh in indices):
			print("Here's one!")
			passCount = passCount + 1
			print("There are ", passCount, "valid passwords!")
		else:
						print("No match")
		
#All of the below was trying to iterate through.
#I kept returning thousands of results because each check counted.
		#for position in indices:
			#print("Checking position ",position)
			#if int(position) == passLow:
				#for position2 in indices:
					#if (int(position) == passLow) is not (int(position2) == passHigh):
						#print("Here's one!")
						#passCount = passCount + 1
						#print("There are ", passCount, "valid passwords!")
					#else:
						#print("No match")
						
			#print("Count is ", passCount)
		#if int(passLow) <= int(passCount) <= int(passHigh):
			#validPass = validPass + 1
			#print("There are ", validPass, " valid passwords.")