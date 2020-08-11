def every_digit(x: int):
    for i in str(x):
        print(f"{str(x).index(i)+1} digit is {i}")


every_digit(76543)
