def my_reversed(a):
    b = a[::-1]
    return b

lst = [x*2 for x in range(2, 18, 3)]
# lst = [2]
print(lst)
print(' ==  answer == ')
print('The reversed list is  ' + str(my_reversed(lst)))