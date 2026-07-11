def math(a, b):
    return a + b, a * b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result, product_result = math(num1, num2)

print(f"Sum = {sum_result}")
print(f"Product = {product_result}")
