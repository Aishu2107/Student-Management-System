students = []

while True:
    print("\n-------- STUDENT MANAGEMENT SYSTEM --------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        dept = input("Enter Department: ")

        student = {
            "Name": name,
            "Roll": roll,
            "Department": dept
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Student Records Found!")
        else:
            print("\nStudent Records")
            for student in students:
                print("------------------------")
                print("Name:", student["Name"])
                print("Roll:", student["Roll"])
                print("Department:", student["Department"])

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        found = False

        for student in students:
            if student["Roll"] == roll:
                print("\nStudent Found")
                print("Name:", student["Name"])
                print("Roll:", student["Roll"])
                print("Department:", student["Department"])
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")
        found = False

        for student in students:
            if student["Roll"] == roll:
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")