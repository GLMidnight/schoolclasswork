a = 0
b = 1
for counter in range (0,21):
    if counter <= 1:
        c = counter
    else:
        c = a + b
        a = b
        b = c
        print(str(c))
