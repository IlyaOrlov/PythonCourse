def lenght(a):
    i = 0
    try:
        for j in a:
            i += 1
    except TypeError:
        print("Object is not iterable")
    finally:
        return i


arr = [1, 4, 5]
print(lenght(arr))
