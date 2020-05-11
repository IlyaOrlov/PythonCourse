# Не совсем понял задание. Сделал в двух вариантах. Первый вариант:
a = dict(cat='кошка', dog='собака')
cat = a['cat']
dog = a['dog']
b = f"I have a {cat} and my friends have a {dog}."
print(b)


# Второй вариант:
def my_func_replace(dictionary, string):
    for key, value in dictionary.items():
        string = string.replace(key, value)
    print(string)


a = {'dog': 'собака', 'cat': 'кошка'}
b = "I have a cat and my friends have a dog."
print(my_func_replace(a, b))

