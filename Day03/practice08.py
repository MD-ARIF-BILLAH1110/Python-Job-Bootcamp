def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number to check if it's even or odd: "))

result = even_odd(num)
print(f"The number {num} is: {result}")