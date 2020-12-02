passCount = 0
validPass = 0
with open("DayTwoInput.txt") as password:
	for item in password:
		passRange,letter,passwd = item.split(" ")
		passLow,passHigh = passRange.split("-")
		letter = letter[:-1]
		passCount = passwd.count(letter)
		#Test for working
		print("Range is ", passLow, " and ", passHigh)
		print("letter is ", letter)
		print("Count is ", passCount)
		if int(passLow) <= int(passCount) <= int(passHigh):
			validPass = validPass + 1
			print("There are ", validPass, " valid passwords.")