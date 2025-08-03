frequencies = input("please enter frequencies")
factor = int(input("please enter the factor"))
nums = frequencies.split(",")
lst = []
for f in nums:
    if int(f) not in lst and int(f)>factor :
        lst.append(int(f))
print(lst)