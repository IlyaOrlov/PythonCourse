# def chargen():
#     while True:
#         for c in '0123456789':
#             yield c
# words = [c+c for c in chargen()][:10]

def fun():
    lst = [12,34,56]
    i = 0
    while i < len(lst):
        yield lst[i]
        i += 1

res = []
for i in fun():
    res.append(i)
print(res)
