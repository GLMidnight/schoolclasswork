def printname():
    name = input("What is your name? ")
    number = int(input("How many times do you want your name printed? "))
    for x in range (number):
        print(name)

print("Welcome to the name printing program")
print("**********************************")
printname()
input()
