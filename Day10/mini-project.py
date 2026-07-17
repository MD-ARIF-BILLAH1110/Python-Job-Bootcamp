class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print("\nStudent Information")
        print("-----------------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
department = input("Enter Department: ")

student = Student(name, age, department)
student.display()