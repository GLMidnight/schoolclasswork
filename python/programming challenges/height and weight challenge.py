def height(inches):
  cm = inches*2.54
  return cm
  
def weight(stones):
  kg = stones*6.364
  
def main():
  inches = int(input("Enter height in cm: "))
  stones = int(input("Enter weight in kg: "))
  print(height(inches))
  print(weight(stones))
  
main()
