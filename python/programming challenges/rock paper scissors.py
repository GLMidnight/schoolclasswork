rounds=int(input("How many rounds do you want to play? 3-10."))

while rounds not in range (3,11):
    try:
        rounds = int(input("How many rounds do you want to play? 3-10"))
    except:
        print("ERROR")
print("")
print("Welcome to RPS.")
print("")
print("You will be against a computer.")
print("")

computer_score=0
user_score=0

computer_score=int(computer_score)
user_score=int(user_score)

for x in range (1,rounds+1):
  print("")
  user_input=input("Choose Rock, Paper or Scissors:")
  
  import random
  choice=random.randint(1,3)
  
  answer1="rock"
  answer2="paper"
  answer3="scissors"

  if choice == 1:
    answer = answer1
  elif choice == 2:
    answer = answer2
  elif choice == 3:
    answer = answer3

  lowercase=user_input.lower()

  print("I Choose...", answer)

  if lowercase == answer:
    print("It's a draw")
    computer_score+=1
    user_score+=1

  if answer == answer2:
    if lowercase == answer3:
      print("Scissors Beats Paper, You Win")
      user_score+=1

  if answer == answer2:
    if lowercase == answer1:
      print("Paper Beats Rock, You Lose")
      computer_score+=1

  if answer == answer3:
    if lowercase == answer2:
      print("Scissors Beats Paper, You Lose")
      computer_score+=1
  
  if answer == answer3:
    if lowercase == answer1:
      print("Rock Beats Scissors, You Win")
      user_score+=1

  if answer == answer1:
    if lowercase == answer3:
      print("Rock Beats Scissors, You Lose")
      computer_score+=1

  if answer == answer1:
    if lowercase == answer2:
      print("Paper Beats Rock, You Win")
      user_score+=1

print("")

if computer_score > user_score:
  print("You Lost!", computer_score, "-", user_score)
if user_score > computer_score:
  print("You Won!", computer_score, "-", user_score)
if user_score == computer_score:
  print("It's A Tie!", computer_score, "-", user_score)
