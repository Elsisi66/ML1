number= input("enter your numbers")
nlist= []
for n in number.split(","):
    nlist.append(int(n))
output_list = []
for n in nlist:
    if n %2 == 0 :
        continue
    output_list.append(n)
print(output_list)    