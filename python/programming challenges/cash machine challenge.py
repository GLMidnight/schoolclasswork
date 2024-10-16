import random

accountnumber = random.randint(1000, 10000)
print (accountnumber)
withdraw = int(input("How much do you want to withdraw "))
if withdraw <= 250 and withdraw % 10 == 0:
  print ("The withdrawl request is accepted and",withdraw,"will be withdrawn")
else:
  print("The request is unacceptable")
