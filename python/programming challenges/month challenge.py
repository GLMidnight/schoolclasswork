year = int(input("What year is it? "))

yes = (year % 4)

month = int(input("Enter a number between 1 and 12: "))

if yes == 0:
	print("It is a leap year")
	if month == 2:
		print("February, 29 days")
		
if month == 1:
	print("January, 31 days")
if month == 2:
	print("February, 28 days")
if month == 3:
	print("March, 31 days")
if month == 4:
	print("April, 30 days")
if month == 5:
	print("May, 31 days")
if month == 6:
	print("June, 30 days")
if month == 7:
	print("July, 31 days")
if month == 8:
	print("August, 31 days")
if month == 9:
	print("September, 30 days")
if month == 10:
	print("October, 31 days")
if month == 11:
	print("November, 30 days")
if month == 12:
	print("December, 31 days")
