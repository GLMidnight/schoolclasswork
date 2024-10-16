num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))

final = num1/num2

print(final)

if final == float(final):
  print("It is not divisible")
elif final == int(final):
  print("It is divisible")
