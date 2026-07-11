for i in range(1, 6): # outer loop to print rows
    for j in range(1, i + 1): # inner loop to print numbers in each row
        print(f"{j}", end=" ") # end=" " keeps the numbers on the same line
    print()  # print a new line after each row