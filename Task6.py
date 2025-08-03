word = str(input("please enter the letters"))
l_count = 0
U_count = 0
for l in word:
    if l.islower():
        l_count +=1
    elif l.isupper():
        U_count +=1
if l_count > U_count:
    print(word.upper())
elif U_count> l_count:
    print(word.lower())