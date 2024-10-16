sentence = "Quick brown fox jumps over the lazy dog."
print("Quick brown fox jumps over the lazy dog.")
word = input("Please choose a word to extract? ")

length = len(word)
length2 = len(sentence)
position = sentence.find(word)
position2 = position + length
half1 = sentence[:position]
half2 = sentence[position2:]
print(half1 + half2)
