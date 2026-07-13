try:
    num = int(input("Enter Number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Zero not Allowed")

except ValueError:
    print("Invalid Number")   #finally block sob somoy cholbe error hok ba na hok