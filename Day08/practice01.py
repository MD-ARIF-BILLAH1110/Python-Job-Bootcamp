# square = lambda x: x * x

# print(square(5))


# add = lambda a, b: a + b  #short function

# print(add(10, 20))


numbers = [10, 20, 30, 40, 50, 60, 70]

# result = list(map(lambda x: x * 2, numbers))  #map list er sob filer item er opor eksathe  kaj kore
# print(result)


result = list(filter(lambda x: x > 30, numbers))
print(result)