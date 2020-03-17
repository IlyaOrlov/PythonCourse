def bolchee_chiclo(a, b):
    if a > b:
        print(a)
    elif a <= 10:
        print(b)
    if a == b:
        print('chicla ravni')
    return



print(bolchee_chiclo(130, 55))
print(bolchee_chiclo(1, 41))
print(bolchee_chiclo(181, 1))
print(bolchee_chiclo(1, 1))


a = int(input('insert a:'))
b = int(input('insert b:'))
bolchee_chiclo(a, b)



