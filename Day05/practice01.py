# cars = ["BMW", "Toyota", "Honda"]

cars = []

number = int(input("Enter how many car add in list: "))

for i in range(number):
    car = input(f"Enter car name {i + 1}: ")
    cars.append(car)

print(f"\nCars list:")

for car in cars:
    print(car)

remove_input = input("\nWhich car do you want remove?  ")
cars.remove(remove_input)
print("\nUpdated car List: ")

for car in cars:
   print(car)

print(f"\nTotal Cars: {len(cars)}")

# car_input1 = input("Enter car name 1: ")
# car_input2 = input("Enter car name 2: ")
# car_input3 = input("Enter car name 3: ")

# cars.append(car_input1)
# cars.append(car_input2)
# cars.append(car_input3)

# print(cars)