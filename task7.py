number = (input("please enter the number\n"))
number_reverse = number[::-1]
if number == number_reverse:
    print("its a pailndrome")
else:
    print("its not a pailndrome number")
armstrong_sum =0
for num in number:
    armstrong_sum += int(num)**3
if armstrong_sum == number:
    print("its armstrong")
else:
    print("its not armstrong number")
