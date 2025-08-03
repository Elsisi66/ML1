working_days = int(input("please enter the number of working days\n"))
absent_days= int(input("please enter the number of absent days\n"))
Total_classes= working_days + absent_days
if working_days/Total_classes >= 0.75:
    print("You can attend the exam")
else:
    print("You can't attend the exam")