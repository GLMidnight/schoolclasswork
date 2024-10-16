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
    if guess > 100:
        guess= int(input("Too high! Try again: "))
    if guess < 1:
        guess= int(input("Too low! Try again: "))

print("Correct, you took ...", NumGuess, "turns to guess that correctly.")
