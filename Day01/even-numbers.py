for i in range(1, 101):  # for i in range(1, 101, 2):  
                         # This would also work, but we are using the modulus operator to check for even numbers  
    if i % 2 == 0:
        print(f"{i} is an even number.")