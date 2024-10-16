corporal = 100
sergeant = 300
staffsergeant = 700
warrantofficer = 1500
playerxp = 0
playerrank = 1
playerxp2 = 0
while playerxp2 < 2000:
  playerxp2= int(input("Enter your XP from last game: "))
  print("Your new XP level is:",playerxp+playerxp2)
  if playerxp2 >= 1500:
    print("Your player rank is Warrant Officer")
    playerxp = (warrantofficer - playerxp)
    print(playerxp)
  elif playerxp2 >= 700 and playerxp2 <= 1499:
    print("Your player rank is Staff Sergeant")  
    playerxp =(staffsergeant - playerxp)
    print(playerxp)
  elif playerxp2 >= 300 and playerxp2 <= 699:
    print("Your player rank is Sergeant")
    playerxp = (sergeant - playerxp)
    print(playerxp)
  elif playerxp2 >= 100 and playerxp2 <= 299:
    print("Your player rank is Corporal")
    playerxp = (corporal - playerxp)
    print(playerxp)
  elif playerxp2 <= 99:
    print("Your player rank is Private")
  else: 
    print("Please enter a valid number")
