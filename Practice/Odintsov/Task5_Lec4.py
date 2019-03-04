x = {1:"one", 2:"two", 3:"three", 4:"four"}

y = "I have 3 pets: 1 dog and 2 cats."

for key in x.keys():
    y = y.replace(str(key), str(x[key]))

print(y)
