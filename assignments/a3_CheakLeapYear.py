year = int(input("\nEnter year: "))
if((year % 400 == 0) or
	(year % 100 != 0) and
	(year % 4 == 0)):
	print(year,"is leap year\n")
else:
	print(year,"is NOT leap year\n")

