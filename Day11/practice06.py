class Animal:
    def sound(self):
        print("Animal makes sound")


class Cat(Animal):    #Single Inheritance
    def sound(self):
        print("Meow")     #Overriding


c = Cat()
c.sound()