from grades_manager import *

print("Welcome to the Student Grades Manager!\n")

my_grades = {}

while True:
    print("Select an option:")
    print("1. Add a student")
    print("2. Print student grade averages")
    print("3. Exit")

    op = input()

    if op == "1":
        my_grades = add_student(my_grades)

    elif op == "2":
        print("Select an option:")
        print("a. Display all students")
        print("b. Display selected students")

        sub = input()

        if sub == "a":
            avg_by_student(my_grades)
        elif sub == "b":
            names = input("Enter student names (comma-separated):\n").split(",")
            names = [n.strip() for n in names]
            avg_by_student(my_grades, names)
        else:
            print("Invalid option selected!")

    elif op == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected!")