students = {
    'Alice': {'age': 20, 'grades': [85, 90, 92]},
    'Bob': {'age': 21, 'grades': [75, 80, 78]},
    'Charlie': {'age': 19, 'grades': [95, 97, 93]}
}

print("Students:", list(students.keys()))

name = input("Which student do you want to update? ")

if name in students:
    # Ask what to edit
    choice = input("Do you want to edit 'age' or 'grades'? ").lower()

    if choice == "age":
        new_age = int(input("Enter the new age: "))
        students[name]['age'] = new_age
        print("updated!")

    elif choice == "grades":
        new_grades = input("Enter new grades separated by commas: ")
        grades_list = []
        for g in new_grades.split(","):
            grades_list.append(int(g))
        students[name]['grades'] = grades_list
        print("updated!")

    else:
        print("Invalid choice. Only 'age' or 'grades' allowed.")
else:
    print("Student not found.")

print("\nUpdated data:")
print(students)
