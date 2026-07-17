class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width) 
    

result = Rectangle(10, 20)
result.area()
        