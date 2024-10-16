mark = int(input("What did you score out of 100? "))
if mark <= 40:
  print("FAIL")
elif mark > 40 and mark < 60:
  print("PASS")
elif mark >= 60 and mark < 80:
  print("MERIT")
elif mark >= 80:
  print("DIISTINCTION")
