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
print("5. Exit")


choice = int(input("Choose (1-5): "))
             
if choice == 5:
    print("Thank you for using Calculator")

else:
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

    print(f"Result = {result}")

