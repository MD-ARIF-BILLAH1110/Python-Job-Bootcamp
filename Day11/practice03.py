class Grandfather:
    def land(self):
        print("Grandfather's land")

class Father(Grandfather):    #Single Inheritance
    def house(self):
        print("Father's house")

class Son(Father):          #Multilevel Inheritance
    def bike(self):
        print("Son's bike")


obj = Son()

obj.land()
obj.house()
obj.bike()

    