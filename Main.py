student = {}

while True:
    print("\n~~~~~~STUDENT_RESULT_MANAGER_APP~~~~~~")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        name=input("Enter student name:")
        marks=int(input("Enter marks:"))
        student[name]=marks
        print(f"{name} Successfully added!")
        
    elif choice == "2":
        if not student:
            print("no student found!:")
        else:
            for name, marks in student.items():
                print(f"Name: {name}, Marks: {marks}")
        
    elif choice == "3":
        name=input("Enter student name:")
        if name in student:
            marks=student[name]
            if marks>=90:
                print(f"{name} has scored A grade with marks {marks}")
            elif marks>=80:
                print(f"{name} has scored B grade with marks {marks}")
            elif marks>=70:
                print(f"{name} has scored C grade with marks {marks}")
            elif marks>=60:
                print(f"{name} has scored D grade with marks {marks}")
            else:
                print(f"{name} has failed with marks {marks}")
        else:
            print("Student not found!")

    elif choice == "4":
        print("Exiting the application...")
        break
    else:
        print("Invalid choice! Please try again.")