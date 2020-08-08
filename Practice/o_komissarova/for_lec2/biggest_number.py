def get_biggest_number(number_1, number_2):
    if number_1 > number_2:
        print(number_1)
    elif number_2 > number_1:
        print(number_2)
    else:
        print('numbers are equal')


get_biggest_number(1, 2)
get_biggest_number(2, 1)
get_biggest_number(2, 2)


def return_biggest_number(number_1, number_2):
    if number_1 > number_2:
        return number_1
    elif number_2 > number_1:
        return number_2
    else:
        return "numbers are equal"


print(return_biggest_number(4, 5))
print(return_biggest_number(5, 4))
print(return_biggest_number(5, 5))
