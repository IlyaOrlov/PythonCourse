def multiplier(m=1, source=[1,2,3]):                                #  m -----> 1
    return [m * x for x in source]                                  # source ---> [1,2,3]

print(multiplier(5))
print(multiplier(5))
print("-------------")
lst = [1,2]
print(multiplier(12, lst))
print(multiplier(12, lst))
