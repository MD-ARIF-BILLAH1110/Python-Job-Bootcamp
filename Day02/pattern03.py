for i in range(5, 0, -1): # outer loop to print rows
    for j in range(i): # inner loop to print numbers in each row
        print("*", end=" ") # end=" " keeps the numbers on the same line 
    print()  # print a new line after each row