# for lesson
# logic errors

grade = int(input("Please enter the test result: "))

if grade > 0:
    print("Fail")
elif grade > 50:
    print ("C Grade")
elif grade > 75:
    print("B Grade")
else:
    print("A Grade")
