def rectangle(length, width):
    return length * width, (2 * (length + width))

leng = int(input("Enter length: "))
wid = int(input("Enter width: "))


area, perimeter = rectangle(leng, wid)
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")