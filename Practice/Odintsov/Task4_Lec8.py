x = "orlov ilya evgenyevich"
y = list(x)
z = [-1]

for id, item in enumerate(y):
    if item == " ":
        z.append(id)

for i in z:
    y[i+1] = y[i+1].upper()

x = "".join(y)
print(x)
