import random
score = 0

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)

if a == b == c :
  score = a + b + c
elif (a == b) and (b != c) and (a != c):
  score = a + b
  score = score - c
elif (a == c) and (a != b) and (c != b):
  score = a + c
  score = score - b
elif (b == c) and (b != a) and (c != a):
  score = a + c
  score = score - b
else:
  score = 0
print(a, b, c)
print(score)
