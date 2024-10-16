menu = ("Menu | 1 = Play Game. 2 = Instructions. 3 = Quit.")
print(menu)
choose = int(input("Choose 1, 2 or 3 from the menu"))
if choose == 1:
  print("Loading...")
elif choose == 2:
  print("Instructions")
elif choose == 3:
  print("Goodbye")
else:
  print(menu, "Please enter a valid number")