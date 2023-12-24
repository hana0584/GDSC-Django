students = {}
def contin():
    pass
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))
    details = input("Enter  other details: ")
    students[name] = {"Age": age, "Grade": grade, "Details": details}
    print(f"{name} has been added to the database.")
def view_student():
    name = input("Enter student name: ")
    if name in students:
        print(f"Name: {name}\nAge: {students[name]['Age']}\nGrade: {students[name]['Grade']}\nDetails: {students[name]['Details']}")
    else:
        print(f"{name} is not in the database.")
def list_students():
    if len(students) == 0:
        print("There are no students in the database.")
    else:
        for name in students:
            print(f"Name: {name}\nAge: {students[name]['Age']}\nGrade: {students[name]['Grade']}\nDetails: {students[name]['Details']}\n")
def update_student():
    name = input("Enter student name: ")
    if name in students:
        field = input("Enter field to update (Age, Grade, Details): ")
        value = input(f"Enter new value for {field}: ")
        if field == "Age":
            students[name]['Age'] = int(value)
        elif field == "Grade":
            students[name]['Grade'] = int(value)
        elif field == "Details":
            students[name]['Details'] = value
        print(f"{name}'s {field} has been updated to {value}.")
    else:
        print(f"{name} is not in the database.")
        

def delete_student():
    name = input("Enter student name: ")
    if name in students:
        del students[name]
        print(f"{name} has been deleted from the database.")
    else:
        print(f"{name} is not in the database.")
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))
    details = input("Enter any other relevant details: ")
    students[name] = {"Age": age, "Grade": grade, "Details": details}
    print(f"{name} has been added to the database.")
def view_student():
    name = input("Enter student name: ")
    if name in students:
        print(f"Name: {name}\nAge: {students[name]['Age']}\nGrade: {students[name]['Grade']}\nDetails: {students[name]['Details']}")
    else:
        print(f"{name} is not in the database.")
def list_students():
    if len(students) == 0:
        print("There are no students in the database.")
    else:
        for name in students:
            print(f"Name: {name}\nAge: {students[name]['Age']}\nGrade: {students[name]['Grade']}\nDetails: {students[name]['Details']}\n")
def update_student():
    name = input("Enter student name: ")
    if name in students:
        field = input("Enter field to update (Age, Grade, Details): ")
        value = input(f"Enter new value for {field}: ")
        if field == "Age":
            students[name]['Age'] = int(value)
        elif field == "Grade":
            students[name]['Grade'] = int(value)
        elif field == "Details":
            students[name]['Details'] = value
        print(f"{name}'s {field} has been updated to {value}.")
    else:
        print(f"{name} is not in the database.")

        
def main():
    while True:
        print("Welcome to the Student Database Program!")
        print("Please select an option:")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit Program")
        choice = int(input("Enter your choice (1-6): "))
        if choice == 1:
            add_student()
            contin()
        elif choice == 2:
            view_student()
            contin()
        elif choice == 3:
            list_students()
            contin()
        elif choice == 4:
            update_student()
            contin()
        elif choice == 5:
            delete_student()
            contin()
        elif choice == 6:
            print("Thank you for using the Student Database Program!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
def contin():
      while True:
        print("**********************")
        print("Do you want to continue")
        print("1.Return to Main menu")
        print("2.Exit")  
choose=int(input("Enter your choice(1/2): "))
if choose==1:
    main()
elif choose==2:
  print("Thank you for using the Student Database Program!")
  exit
else : 
    print("Invalid choice.Please try again")
