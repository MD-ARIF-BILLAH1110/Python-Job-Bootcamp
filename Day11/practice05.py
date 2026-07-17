class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):  #Inheritance and super() to parent class
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")


s = Student("Arif", 1)
s.show()