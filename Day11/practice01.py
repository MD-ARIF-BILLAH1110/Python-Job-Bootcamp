class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):          #Inheritance
    pass


dog = Dog()
dog.sound()
