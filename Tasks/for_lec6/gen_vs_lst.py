# x = [n for n in range(10) if n % 2 == 0]
# print(x)
# print(type(x))
#
# x = (n for n in range(10) if n % 2 == 0)
# print(x)
# print(type(x))
# for i in x:
#     print(i)


lst = [2,3,5,6,3,6,7]
# lst = [2,3,5]  # negative case
s = [x for x in lst if lst.count(x) > 1][0]
print(s)

s = next((x for x in lst if lst.count(x) > 1), None)
print(s)
