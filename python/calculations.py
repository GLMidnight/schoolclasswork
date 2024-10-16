# enter 2 numbers that can be reused in 4 calculations below:
number1=int(input("Enter first number: "))
number2=int(input("Enter 2nd number: "))


# make calculations
power_of_result = number1 ** number2
division_result = number1 / number2
integer_division_result = number1 // number2
modulus_result = number1 % number2

# output results
print()
print(number1,"to the power of",number2,"%",power_of_result)
print(number1,"divided by",number2,"is",division_result)

print(number1,"divided by",number2,"is",integer_division_result)
print(number1,"divided by",number2,"has a remainder of",modulus_result)

if modulus_result == (): # == is equal
    print("That means it was a whole number")
