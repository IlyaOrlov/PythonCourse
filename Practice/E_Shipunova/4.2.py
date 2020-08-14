def every_digit(x: int):
    for i in str(x):
        print(f"{str(x).index(i)+1} digit is {i}")


def v2_every_digit(x: int):
    step = 1  # static var

    def rec_get_num(num):
        nonlocal step
        if num//10 == 0:
            return print(f"{step} is digit = {num}")  # print the first

        rec_get_num(num//10)
        step += 1
        return print(f"{step} is digit = {num % 10}")

    rec_get_num(x)


if __name__ == "__main__":
    every_digit(76543)
    v2_every_digit(12345)
    v2_every_digit(7777777)
