def printNumber(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]

if __name__ == '__main__':
    nums = [0,3,24,2,3,7]
    print (nums)
    printNumber(nums)
    print (nums)