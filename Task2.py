word = input("Enter the word\n")
vowels = ["a","e","u","o","i"]
for letter in vowels:
    if letter in word:
        index = word.find(letter)
        print(f"there is {letter} (vowel character) in index {index}")
