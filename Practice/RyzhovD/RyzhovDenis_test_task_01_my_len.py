'''
My realization of len function
'''
def my_len(a):
    length = 0
    for x in a:
        length += 1
    return length


### Here the realization 'ab initio', i.e.,
### assuming I do not know range and for x in list
# def my_len(a):
#     k = 0
#     length = 0
#     check = True
#     while check:
#         try:
#             a[k]*2
#             length += 1
#             k += 1
#             check = True
#         except:
#             check = False
#
#     return length


### TEST
lst = [x*2 for x in range(3, 8)]
print(lst)
print(' ==  answer == ')
print('The length is ' + str(my_len(lst)))