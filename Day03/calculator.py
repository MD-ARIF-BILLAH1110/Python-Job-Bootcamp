def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("===== Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = int(input("Choose (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    result = add(num1, num2)

elif choice == 2:
    result = subtract(num1, num2)

elif choice == 3:
    result = multiply(num1, num2)

elif choice == 4:
    result = divide(num1, num2)

else:
    result = "Invalid Choice"
    

print(f"Result = {result}")

