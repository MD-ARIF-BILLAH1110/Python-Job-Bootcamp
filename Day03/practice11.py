def calculator(a, b):
    return a - b, a / b

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

Difference, Division = calculator(number1, number2)

print(f"Difference = {Difference}")
print(f"Division = {Division}")