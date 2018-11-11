def get_member():
    return input("Please enter number, if you want to stop - 'end': ")


def get_array():
    ar = []
    x = get_member()
    while x != "end":
        if x.isdigit():
            ar.append(int(x))
        else:
            print("Not number!")
        x = get_member()
    else:
        return ar


array = [5, 3, 4, 0, 1, 1, 100, 8, 56]
#array = get_array()
print("Array", array)
for i in range(0, len(array)):
    splitted_array = array[i:len(array)]
    for j in range(0, len(splitted_array)):
        if splitted_array[j] == min(splitted_array):
            min_index = j + i
            break
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp
print("Sorted Array", array)
