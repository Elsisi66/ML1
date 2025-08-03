my_list = list(input("enter your list"))
if len(my_list) == 0:

    print("The list is empty.")
else:
    print("Original list:", my_list)
    my_list.sort()
    print("Sorted list:", my_list)