text = input("Enter something:\n ")


if text.isdigit():
    total = 0
    for ch in text:
        digit = int(ch)
        total = total + digit
    print(total)

elif text.isalpha() :
    new_text = ""
    for ch in text:
            new_text = new_text + ch
    print(new_text)

else:
    numbers = ""
    letters = ""
    for char in text:
        if char.isdigit():
            numbers = numbers + char
        else:
            letters = letters + char
    print(f"[{numbers}] [{letters}]")