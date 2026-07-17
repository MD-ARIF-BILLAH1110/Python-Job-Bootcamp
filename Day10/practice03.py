class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def employee_details(self):
        print(f"\nEmployee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")


name = input("Enter Name: ")
salary = float(input("Enter Employee Salary: "))

employee = Employee(name, salary)
employee.employee_details()