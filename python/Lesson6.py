import random
CompChoice = random.randint(1,10)

name = input("Please enter your name: ")
print()
print("Hello",name)
print()
print(name, "I am thinking of a number between 1 and 100...")
print("Can you guess what it is?")
print()
guess=int(input("Enter your first guess: "))
NumGuess = 1

while guess != CompChoice:
    guess= int(input("Wrong, try again: "))
    NumGuess = NumGuess + 1

print("Correct, you took ...", NumGuess, "turns to guess that correctly.")
