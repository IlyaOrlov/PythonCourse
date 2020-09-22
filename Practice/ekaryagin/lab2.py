def who_is_bigger_print (first_num, second_num):
    if first_num > second_num:
        print(f'{first_num} is bigger')
    elif second_num > first_num:
        print(f'{second_num} is bigger')
    else:
        print(f'{first_num} are equal {second_num}')


who_is_bigger_print(7, 5)
who_is_bigger_print(5, 7)
who_is_bigger_print(7, 7)


def return_biggest_number(number_1, number_2):
    if number_1 > number_2:
        return number_1
    elif number_2 > number_1:
        return number_2
    else:
        return None


print(return_biggest_number(4, 5))
print(return_biggest_number(5, 4))
print(return_biggest_number(5, 5))

