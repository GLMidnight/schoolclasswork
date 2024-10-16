from random import randint
total=0
right=0

for i in range(10):
  n1 = randint (1,9)
  n2 = randint (1,9)
  total=n1*n2
  print(n1,"x",n2)
  answer=int(input("Enter the answer:" ))
  
  if answer==total:
    right=right+1

print("You got ",right,"problems right")