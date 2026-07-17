class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def grade(self):
          if self.marks >= 80:
            return "A+"
          elif self.marks >= 70:
            return "A"
          elif self.marks >= 60:
            return "A-"
          elif self.marks >= 50:
            return "B"
          else:
            return "F"
          
    def show(self):
       print("\nName:", self.name)
       print("Marks:", self.marks)
       print("Grade:", self.grade())

      

name = input("Enter Name: ")
marks = int(input("Enter Mark: "))

student = Student(name, marks)
student.show()
