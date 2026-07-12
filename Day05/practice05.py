numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
 number = int(input(f"Enter number {i+1}: "))
 numbers.append(number)
 
numbers.sort()
print(f"\nSorted Number: ")
print(numbers)

numbers.sort(reverse=True)
print("\nReversed  Number: ")
for number in numbers:
   print(number)

print(f"\nTotal Numbers: {len(numbers)}")