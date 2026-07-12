cars = ["BMW", "Suzuki", "Toyota"]

position = int(input("Enter position: "))
car_name = input("Enter car name: ")
cars.insert(position, car_name)

print(cars)