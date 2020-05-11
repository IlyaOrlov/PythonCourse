# def multiplier(m=1, source=[1, 2, 3]):
#     result = source
#     for i, x in enumerate(source):
#         result[i] *= m
#     return result
#
#
# h = multiplier(5)
# print(h)



def multiplier(m=1, source=[1, 2, 3]):
    result = []
    i = 0
    while i < len(source):
        result.append(source[i]*m)
        i += 1
    return result


h = multiplier(5)
print(h)

#Честно не понял чем плоха исходная реализация, но тем не менее написал свой вариант.