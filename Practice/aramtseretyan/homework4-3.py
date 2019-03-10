arr = [0,3,24,2,3,7]
b = []
def fact (b):
    if len(arr) !=0:
	    a = arr.index (min(arr))
	    b.append(arr[a])
	    del arr[a]
	    fact (b)
    else :
	    print('Список: {}'. format(b))
fact (b)
