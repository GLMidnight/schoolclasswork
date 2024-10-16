analysis=int(input("Input your marks from the analysis section: "))
design=int(input("Input your marks from the design section: "))
implementation=int(input("Input your marks from the implementation section: "))
evaluation=int(input("Input your marks from the evaluation section: "))
total_marks= analysis+design+implementation+evaluation
if total_marks <=4:
  print("Grade: U /n Marks till next band: ", (4-total_marks))
elif total_marks <=13:
  print("Grade: G /n Marks till next band: ", (13-total_marks))
elif total_marks <=22:
  print("Grade: F /n Marks till next band: ", (22-total_marks))
elif total_marks <=31:
  print("Grade: E /n Marks till next band: ", (31-total_marks))
elif total_marks <=41:
  print("Grade: D /n Marks till next band: ", (41-total_marks))
elif total_marks <=54:
  print("Grade: C /n Marks till next band: ", (54-total_marks))
elif total_marks <=67:
  print("Grade: B /n Marks till next band: ", (67-total_marks))
elif total_marks <80:
  print("Grade: A /n Marks till next band: ", (80-total_marks))
elif total_marks >= 80:
  print("Grade: A* \n Marks till next band: N/A")
