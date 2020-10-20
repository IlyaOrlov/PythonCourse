import re


s1 = 'Hello World'
s2 = "Python Programming!"
print("s1[0]:", s1[0])
print("s2[1:5]:", s2[1:5])
print(s1 + s2)
print(s1 * 2)
print('Pro' in s2, '!' not in s1)
print(
    R'сырая строка \n' 
    '\n несырая \t строка \n '
)
print('%s: Привет Мир, %s: Программирование на Python!' % (s1, s2))
print('{}: приветствие'.format(s1))
print('{:,.2f}'.format(296999.2567))



def prints(arg):
    """функция печатает каждую подстроку состоящую из одного чимвола в новой строке"""
    for i in range(0, len(arg)-1):
        print(arg[i])
        i += 1


match = re.match('Hello[ \t]*(.*) world', 'Hello Python     is world')
print(match.group(1))

print(s1.strip('  '))
print(s1.swapcase())

