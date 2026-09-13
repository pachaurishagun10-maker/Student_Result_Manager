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
        marks=marks(input("Enter marks:"))
        student[name]=marks
        print(f"{name} Successfully added!")
        
    elif choice == "2":
        if not student:
            print("no student found!:")
        else:
            for name, marks in student.items():
                print(f"Name: {name}, Marks: {marks}")
                