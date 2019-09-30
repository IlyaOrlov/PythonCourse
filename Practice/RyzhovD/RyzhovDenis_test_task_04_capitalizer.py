def capitalizer(lst):
    if lst[0] != ' ':  # Capitalize first letter
        lst = lst[0].swapcase() + lst[1:]
    for k in range(0, len(lst)-1):
        # print(str(k)+'/'+str(len(lst)))
        if lst[k] == ' ':
            lst = lst[0:k+1] + lst[k+1].swapcase() + lst[k+2:]
        # if lst[len(lst)-2] == ' ':  # finish letter
        #     # print(lst[0:len(lst)])
        #     lst = lst[0:len(lst)-1] + lst[len(lst)-1].swapcase()

    return lst


### TEST
lst_t = ' admiral aral  vorkosigan j  '
print('')
print(lst_t)
print('=== CAPITALIZED ' + '='*(len(lst_t)-16))
print(capitalizer(lst_t))