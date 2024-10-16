hours = int(input("How many hours did you work this week? "))
rate = float(input("What is your hourly rate of pay? "))

if hours > 60:
	print("Unaccepted.")

total = (hours * rate)

if hours > 40:
	total = total + (((hours - 40) * rate) * 1.5)
	
	
print("Your total pay is",total)
