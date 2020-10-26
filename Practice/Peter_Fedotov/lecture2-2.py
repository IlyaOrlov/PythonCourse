def test2 (a, b):
    if a > b:
        print(f"{a}")
    elif b > a:
        print(f"{b}")
    elif a == b:
        print(f"enter different values")
test2(3, 1)
test2(3, 5)
test2(3, 3)