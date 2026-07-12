numbers = []
count = int(input("How many numbers do you want to enter? "))
for i in range(count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

if count > 0: 
    smallest = min(numbers)
    largest = max(numbers)
    total= len(numbers)

    print(f"\nSmallest Number: {smallest}")
    print(f"Largest Number: {largest}")
    print(f"Total Number: {total}")


    search_number = int(input("Enter a number to search: "))
    if search_number in numbers:   #Nested 
       print(f"{search_number} is in the list.")
    else:
       print(f"{search_number} is not in the list.")

else:
    print("No numbers entered.")