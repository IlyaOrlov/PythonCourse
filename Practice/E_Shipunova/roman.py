
class NonValidInput(Exception):
    pass


def to_roman(num: int) -> str:

    if type(num) != int or num < 1 or num > 5000:    # check type of arg and value of arg
        print('Incorrect data!')
        raise NonValidInput()

    result = []
    number_line = str(num)                           # for processing each value according to the num_order
    num_order = 10**(len(number_line)-1)             # process starts with num_order of arg

    system_rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '_V_']
    system_arab = [1, 5, 10, 50, 100, 500, 1000, 5000]

    for n in number_line:
        n = int(n)                                   # for work with number

        if n == 0:
            num_order /= 10
            continue

        elif n <= 3:
            index = system_arab.index(num_order)
            for i in range(n):
                result.append(system_rom[index])

        elif n == 4:
            index = system_arab.index((n+1) * num_order)
            result.append(system_rom[index-1])
            result.append(system_rom[index])

        elif n == 5:
            index = system_arab.index(n * num_order)
            result.append(system_rom[index])

        elif 5 < n < 9:
            index = system_arab.index(5 * num_order)
            result.append(system_rom[index])
            for i in range(n-5):
                result.append(system_rom[index-1])

        elif n == 9:
            index = system_arab.index(5 * num_order)
            result.append(system_rom[index-1])
            result.append(system_rom[index+1])

        num_order /= 10                       # for move one order lower

    return ''.join(result)
