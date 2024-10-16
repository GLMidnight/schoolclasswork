NitrateLevel = float(input("Please enter the level of nitrates in the water (between 1 and 50) "))
if NitrateLevel > 10:
  print("You should dose 3ml of Carbon source")
elif NitrateLevel > 2.5:
  print("You should dose 2ml of Carbon source")
elif NitrateLevel > 1:
  print("You should dose 1ml of Carbon source")
else:
  print("You should dose 0.5ml of Carbon Source")
