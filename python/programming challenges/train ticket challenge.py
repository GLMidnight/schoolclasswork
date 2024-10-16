train_fare=0
no_stations=int(input("Enter the number of stations you need to pass through: "))
adults=int(input("Enter the number of adults: "))
children=int(input("Enter the number of children: "))
time=int(input("Enter the time of day as a number in 24 hour clock: "))

if 6<=time<=9:
  for i in range(no_stations):
    train_fare=train_fare+5

if adults>0:
  for i in range(no_stations):
    train_fare=train_fare+20
    
if children>0:
  for i in range(no_stations):
    train_fare=train_fare+10
  
print("Your train fare costs £",train_fare)
