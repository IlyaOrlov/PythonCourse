def test1 (a, b):
    if a > b:
        print(f"{a}more, than {b}")
    elif b > a:
        print(f"{b} more, than {a}")
    elif a == b:
        print(f"{a} equal {b}")
test1(3, 4)
test1(5, 6)
test1(7, 7)

