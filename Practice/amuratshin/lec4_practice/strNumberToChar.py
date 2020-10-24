
list_chars = input('Введите пятизначное число:  ')

def srtingNumberToChars(args):
    """функция выводит каждую цифру введенного пятизначного число в новой строке"""
    for i in range(1, 6):
        print(list(args))


srtingNumberToChars(list_chars)