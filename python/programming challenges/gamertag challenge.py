print("The length of your gamertag will be checked.")
print("Gamertags must be less than 15 characters.")
gamertag = str(input("Please enter a gamertag."))
gamertag_length = len(gamertag)
while gamertag_length >= 15:
    print("Your gamertag is too long")
    print(gamertag)
if gamertag_length <= 15:
    print("Gamertag accepted.")
    gamertag = (gamertag)
print("Your gamertag is:")

import random
gamertagnumber = random.randint(1000,9999)

print(gamertag),('#'),(gamertagnumber)