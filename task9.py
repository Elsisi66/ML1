n = int(input("Enter the number of terms: "))
total = 0
expression = ""

for i in range(1, n + 1):
    term = (i ** 2) * ((-1) ** (i + 1))
    total += term

    if i == 1:
        expression += f"{i**2}"
    elif term > 0:
        expression += f" + {i**2}"
    else:
        expression += f" - {i**2}"

print(f"{expression} = {total}")
