print("Homework\n\nDue 17th October 2019\n")
# homework

# due 17 october 2019

# first task

# A shop is having a sale. They’re giving 10% off when a customer spends £10 or
# less and a 20% discount then they spend over £10. Write a program that asks
# for the amount spent and then displays the discount to be applied and then the
# final price (i.e. with the discount applied).

customerSpend = float(input("How much have they spent? "))
if customerSpend > 10: 
 discount = (customerSpend / 100) * 10
 print ("Discount is £",discount )
 print("Final Price is £",customerSpend )

elif customerSpend > 10: 
 discount = (customerSpend / 100) * 20
 print ("Discount is £",discount )
 print("Final Price is £",customerSpend )

# second task

# Write a program that asks a multiple choice question. If they get the answer
# correct then display “Well done”; if they get the answer wrong then display
# “Try again” and they repeat the question until they get it right.

questiona = input("What's the most tallest animal in the world? ")
if questiona == 'giraffe':
  print("Well done!")
else:                             # Dont know about repeating the question.  
  print ("Try again!")

# third task

# There are two Lions called A and B. Ask the keeper if each Lion is smiling (you
# will have to ask two separate questions, i.e. is Lion A smiling, is Lion B smiling).
# If both Lions are smiling then the keeper must be afraid as the Lions are plotting
# something and you must tell the keeper it is not safe to enter the cage. If
# neither Lion is smiling then the keeper must also be afraid as the Lions are
# angry at something and you must tell them it is not safe to enter the cage. If
# one Lion is smiling and the other isn’t smiling then you can tell the keeper it is
# safe to enter the cage.

from random import randint

print("The Keeper is with the lion A and B.")
keeperquestion = input("You: Hey Keeper, is Lion A smiling right now? (press enter to ask) ")

keeper = randint(1,2)
#print(keeper)

if keeper == 1:
    print("Keeper: Yes.")
if keeper == 2:
    print("Keeper: No.")

keeperquestion2 = input("You: Okay, and is Lion B smiling right now? (press enter to ask) ")
keeper1 = randint(1,2)
#print(keeper1)

if keeper1 == 1:
    print("Keeper: Yes.")
if keeper1 == 2:
    print("Keeper: No.")

yourplayerchoice = input("Keeper: Would it be safe if I enter the cage? ")

if yourplayerchoice == "no":
    print("Keeper: Ok, thank you. Not entering the cage until they stop. Am afraid.")
if yourplayerchoice == "yes":
    print("Keeper: Ok, thank you. Let me unlock this cage.")



# fourth task

# When squirrels get together for a party they like to eat acorns. A squirrel party
# is successful when the number of acorns is between 40 and 60, inclusive, unless
# it is the weekend, in which case there is no upper limit on the number of
# acorns. Write a program which will find out when the party is and how many
# acorns there are. Return “Good Party” if the party is within the rules or
# “Terrible Party” if they have the wrong number of acorns.

squirrelquestion = int(input("How many acorns you've got for the squirrel party? "))

if squirrelquestion < 40:
    print("Terrible Party")
if squirrelquestion > 40:
    print("Good Party")
if squirrelquestion > 60:                                               # i do not get this. 
    print("Too High!")

    
