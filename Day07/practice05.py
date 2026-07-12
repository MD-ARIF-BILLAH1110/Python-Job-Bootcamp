def calculate(a, b, c):
    return a + b + c, (a + b + c)/3

total, average = calculate(10, 20, 30)

print(f"Sum: {total}")
print(f"Average: {average}")