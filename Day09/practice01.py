file = open("text.txt", "w")
print(file.write("Python Developer"))
file.close()

file = open("text.txt", "w")
print(file.write("Django and Data Science"))
file.close()  #jodi with na use kora hy thle close use korte hobe


file = open("text.txt", "r")
print(file.readlines())
print(file.readlines())

file.close()