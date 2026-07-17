class Person:
    def introduce(self):
        print("I am a person.")


class Student(Person):    #Single Inheritance
    def study(self):
        print("I am studying.")


s = Student()
s.introduce()
s.study()