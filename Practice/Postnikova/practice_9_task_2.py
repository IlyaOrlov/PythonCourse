import multiprocessing

# Task_2

def summarize_anythig(*args):
    sum_int = 0
    sum_string = ''
    sum_list = []
    for index in range(len(args)):
        if type(args[index]) is not type(args[index-1]):
            print('Sorry, types of all arguments should be the same!')
            break
        elif isinstance(args[index], int):
            sum_int += args[index]
        elif isinstance(args[index], str):
            sum_string = f'{sum_string} {args[index]}'
        elif isinstance(args[index], list):
            sum_list += args[index]
    return sum_int, sum_string, sum_list


all_values = [(1, 2, 3, 88), ['Python', 'is', 'a', 'programming', 'language'], [[1, 2, 3], [5, 8, 9], [22, 77, 12]]]
all_processes = []

if __name__ == "__main__":
    for my_range in all_values:
        p = multiprocessing.Process(target=summarize_anythig, args=my_range)
        p.start()
        all_processes.append(p)

    for p in all_processes:
        p.join()
        print('Process {} is joined'.format(p))