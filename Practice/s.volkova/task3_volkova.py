# 04.11 - [ИО]:  Проверено (OK).
#for Python 3.6
#task 3

def sorting_func(my_list):
    '''Функция сортирует список, меняя местами наименьший элемент в неотсортированной части списка
    и первый неотсортированный элемент'''
    i = 0
    tostop = len(my_list)-1
    while i < tostop:
        #Находит наименьший элемент в неотсортированной части списка и его индекс внутри этой части
        the_min = min(my_list[i:]) 
        minilocindex = my_list[i:].index(the_min)
        #Проверяет, не стоит ли наименьший элемент уже на первом месте
        if minilocindex != 0:
            #Определяет индекс наименьшего неотсортированного элемента относительно всего списка
            miniglobalindex = minilocindex + i
            #Меняет местами первый неотсортированный элемент и наименьший неотсортированный
            (my_list[i], my_list[miniglobalindex]) = (my_list[miniglobalindex], my_list[i])
        i += 1
    return my_list
    

if __name__ == '__main__':
    print(sorting_func([0,3,24,2,3,7]))
