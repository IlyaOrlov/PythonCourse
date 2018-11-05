arr = [0, 3, 24, 2, 3, 7]
print (arr)
minim=0
while minim<len(arr):
	i=minim+1
	while i<len(arr):
		if arr[minim]>arr[i]:
			arr[minim], arr[i] = arr[i], arr[minim]
		i += 1
	minim += 1
print (arr)
