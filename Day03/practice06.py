def cube(number):
    return number * number * number

num = int(input("Enter a number to find its cube: "))

result = cube(num)
print(f"The cube of {num} is: {result}")