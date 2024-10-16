#1

question1 = int(input("How many hours do you play computer games a day? "))

if question1 < 2:
    print("That sounds okay.")
if question1 > 2:
    print("Too much")
if question1 > 4:                             #2
    print("Go outside and get some fresh air")
question2 = int(input("How old are you? "))

if question2 > 18:
    print("You can vote.")
if question2 < 18:
    print()
if question2 > 16:
    print("You can buy a lottery ticket.")
if question2 < 16:
    print("Too young.")
