score = {"e":1, "a":2, "r":3,"i":4,"o":5,"t":6,"n":7,"s":8,"l":9,"c":10,"u":11,"d":12,"p":13,"m":14,"h":15,"g":16,"b":17,"f":18,"y":19,"w":20,"k":21,"v":22,"x":23,"z":24,"j":25,"q":26}
word = str(input("Enter your word: "))
def scrabble(word):
  total = 0
  for a in word:
    total += score[a.lower()]
  return total
print("The score for " +str(word) +" is " +str(scrabble(word)))