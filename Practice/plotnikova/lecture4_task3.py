#найти наименьший элемент в массиве
def find_min_arr(data,ii):
    min_arr = data[ii]
    for i in range(ii, len(data)):
       if min_arr>data[i]:
           min_arr=data[i]
    return min_arr

def sort(data):
    t=len(data)
    for i in range(t):
        min_arr_index= data.index(find_min_arr(data, i))
        data[i], data[min_arr_index] = data[min_arr_index], data[i]
    return data


arr=[-12, 33, 155, 0,3,24,2,-103,7, -14]
print(sort(arr))


