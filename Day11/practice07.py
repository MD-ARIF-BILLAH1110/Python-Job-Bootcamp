class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def info(self):
        super().info()
        print(f"Department: {self.department}")

s = Student("Arif", "CSE")
s.info()