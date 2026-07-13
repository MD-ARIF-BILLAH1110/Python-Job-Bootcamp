def factorial(n):   #Recursion function jodi nijeke call kore 
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))