# rev_1

arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)):
    x = min(arr[i:])
    m = arr.index(x, i)
    arr[i], arr[m] = arr[m], arr[i]
print(arr)

# rev_2
# def sorting(args):
#     a = []
#     while len(args) > 0:
#         a.append(min(args))
#         args.remove(min(args))
#     return a
#
#
# arr = [0, 3, 24, 2, 3, 7]
# print(sorting(arr))

# rev_3
# arr = [0, 3, 24, 2, 3, 7]
# for i in range(len(arr)):
#     k = min(arr[:len(arr)-i])
#     m = arr.index(k)
#     arr.append(arr.pop(m))
# print(arr)

