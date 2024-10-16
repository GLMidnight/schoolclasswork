def payment(hrs,toys):
  hrs = hrs * 12
  toys = toys * 0.60
  total = hrs + toys
  return total

def main ():
  hrs = float (input("Enter how many hours you've worked for "))
  toys = int (input("Enter how many trains you made. "))
  print (payment(hrs,toys))

main ()
