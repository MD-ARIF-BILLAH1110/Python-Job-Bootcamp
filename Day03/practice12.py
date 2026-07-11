def math(a, b):
    return a + b, a * b

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

addition, multiplication = math(number1, number2)
print(f"Addition = {addition}")
print(f"Multiplication = {multiplication}")