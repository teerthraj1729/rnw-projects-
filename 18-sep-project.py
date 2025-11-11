students = []
while True:
    print("Welcome to the Student Data Organizer")
    print()
    print("Select an option:")
    print("1. Add student")
    print("2. Display all student")
    print("3. Update student infromation")
    print("4. Delete student")
    print("5. Display students subject offered")
    print("6. Exit")
    print()
    choice = int(input("Enter choice:"))
    match choice:
        case 1:
            try:
                student_id = int(input("Enter Student ID:"))
                name = input("Enter name:")
                age = int(input("Enter age:"))
                grade = input("Enter Grade:")
                dob = input("Enter Date of birth (YYYY-MM-DD):")
                subjects = input("Enter Subjects (comma-separated):").split(",")

                unique_info = (student_id, dob)
                subject_set = set(sub.strip() for sub in subjects)
                student = {
                    "id_dob": unique_info,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "subjects": subject_set
                }
                students.append(student)
                print("Student added successfully!")
            except ValueError:
                print("Invalid input! Please enter correct values.")

        case 2:
            for s in students:
                sid, dob = s["id_dob"]
                print(f"ID: {sid} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
                print(f"| Subjects: {','.join(s['subjects'])} | DOB: {dob}")
        case 3:
            sid = int(input("Enter Student ID to update: "))
            for s in students:
                if s["id_dob"][0] == sid:
                    print("1. Update Age\n2. Update Subjects")
                    choice = input("Enter choice: ")
                    if choice == 1:
                        s["age"] = int(input("Enter new Age: "))
                        print("Age updated!")
                    elif choice == 2:
                        new_subjects = input("Enter new Subjects (comma-separated): ").split(",")
                        s["subjects"] = set(sub.strip() for sub in new_subjects)
                        print("Subjects updated!")
            print("Student not found.")
        case 4:
            sid = int(input("Enter Student ID to delete: "))
            for i, s in enumerate(students):
                if s["id_dob"][0] == sid:
                    del students[i]
                    print("Student deleted!")
                    break
            print("Student not found.")

        case 5:
            all_subjects = set()
            for s in students:
                all_subjects.update(s["subjects"])
            print("\n--- Subjects Offered ---")
            print(", ".join(all_subjects) if all_subjects else "No subjects available.")

        case 6:
            print("Thank you for using Student Data Organizer!")
            break

        case _:
            print("Invalid choice, try again.")
