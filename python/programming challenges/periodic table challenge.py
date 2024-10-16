search = input("Please enter a group or element")
number = search.isalpha()

if number == True:
    search = search.upper()

Lithium = "Element: Lithium\nAtomic Weight: 6.94\nGroup: 1"
Sodium = "Element: Sodium\nAtomic Weight: 22.98\nGroup: 1"
Potassium = "Element: Potassium\nAtomic Weight: 33.09\nGroup: 1"
Beryllium = "Element: Beryllium\nAtomic Weight: 9.01\nGroup: 2"
Magnesium = "Element: Magnesium\nAtomic Weight: 24.30\nGroup: 2"
Calcium = "Element: Calcium\nAtomic Weight: 40.07\nGroup: 2"

if search == ("LITHIUM" or "LI"):
    print()
    print(Lithium)
elif search == ("SODIUM" or "NA"):
    print()
    print(Sodium)
elif search == ("POTASSIUM" or "K"):
    print()
    print(Potassium)
elif search == ("BERYLLIUM" or "BE"):
    print()
    print(Beryllium)
elif search == ("MAGNESIUM" or "MG"):
    print()
    print(Magnesium)
elif search == ("CALCIUM" or "CA"):
    print()
    print(Calcium)
elif search == ("GROUP 1" or 1):
    print()
    print(Lithium)
    print()
    print(Sodium)
    print()
    print(Potassium)
elif search == ("GROUP 2" or 1):
    print()
    print(Beryllium)
    print()
    print(Magnesium)
    print()
    print(Calcium)
else:
    print("Error")
