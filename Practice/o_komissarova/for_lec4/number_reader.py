# Составить программу, которая будет считывать введённое пятизначное число.
# После чего, каждую цифру этого числа необходимо вывести в новой строке:

def read_number(number):
    if not str(number).isdigit():
        print("incorrect input")
        return False
    numbers = list(str(number))
    print("Число: " + str(number) + "\n" +
          "1 цифра равна " + numbers[0] + "\n" +
          "2 цифра равна " + numbers[1] + "\n" +
          "3 цифра равна " + numbers[2] + "\n" +
          "4 цифра равна " + numbers[3] + "\n" +
          "5 цифра равна " + numbers[4] + "\n")


read_number(10819)
