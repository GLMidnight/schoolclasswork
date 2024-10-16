x=[chr(x) for x in range(65,90) and (90,123)] #chr returns the string of the the unicode/ascii value 'x'

type=input("Enter 'a' if you want to encode into ROT13 and 'b' if you want to decode out of ROT13:")
if type=="a":
  word=str(input("Enter your word in English:"))
  for x in word:
    x=str(x) 
    ordx=ord(x) #ord converts the string into a unicode/ ascii value
    x=ordx+13 #adds 13 ascii values, which shifts it by this many places and gives it a new letter
    x=chr(x) #converts ascii value back to a string
    print(x)
elif type=="b":
  word=str(input("Enter your word in ROT13:b="))
  for x in word:
    x=str(x)
    ordx=ord(x)
    x=ordx-13
    x=chr(x)
    print(x)
else:
  print("Invalid Input")