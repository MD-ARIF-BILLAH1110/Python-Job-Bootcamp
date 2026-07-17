class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def gass(self):
        print("Car Running")
       


c = Car()
c.start()
c.gass()