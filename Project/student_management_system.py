students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Sort Students")
    print("6. Count Students")
    print("7. Update Students")
    print("8. Clear All Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        count = int(input("Enter the number of students to add: "))
        for i in range(count):
            student_inp = input(f"Enter student name {i + 1}: ")
            students.append(student_inp)
        print("✅ Students added successfully.")
    
    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List: ")
            for i, student in enumerate(students, start=1): #enumerate
                print(f"{i}. {student}")

    elif choice == 3:
        search = input("Enter student name: ").strip().lower()

        student_list = [student.lower() for student in students]

        if search in student_list:
            print(f"✅ {search} found.")
        else:
            print(f"❌{search} not found.")

    elif choice == 4:
        remove_name = input("Enter student name to remove: ").strip()

        found = False

        for student in students:
            if student.lower() == remove_name.lower():
                students.remove(student)
                print(f"✅{student} removed successfully.")

                found = True
                break
        if not found:
            print(f"❌{remove_name} not found.")

    elif choice == 5:
        if len(students) == 0:
          print("No students found.")
        else:
          students.sort()
          print("\nSorted Students:")

        for i, student in enumerate(students, start=1):
         print(f"{i}. {student}")

    elif choice == 6:
        print(f"Total Students: {len(students)}")
    

    elif choice == 7:
        old_name = input("Enter old name: ")
        new_name = input("Enter new name: ")

        found = False

        for i, student in enumerate(students):
          if student.lower() == old_name.lower():
             students[i] = new_name
             print("✅ Student updated successfully.")
             found = True
             break

        if not found:
           print("❌ Student not found.")
    

    elif choice == 8:
        students.clear() #none value return kore
        print("✅ All students cleared successfully.")

    elif choice == 9:
        print("Thank you for using student management system.")
        break
    
   
    else:
     print("❌ Invalid choice. Please try again.")