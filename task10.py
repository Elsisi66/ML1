sentence = str(input("Enter your sentence \n"))
words = sentence.split()
if "car" in words:
    position = words.index("car") + 1
    print(f"The word 'car' is in position {position} in the text.")
else:
    print("The word 'car' is not in the sentence.")

