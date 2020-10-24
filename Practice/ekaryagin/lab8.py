import os


# task 1
def my_len(my_list):
    length = 0
    for i in my_list:
        length += 1
    return length


# task 2
def reverse(my_list):
    return my_list[::-1]


# task 3
def my_range(*args):
    for i in args:
        if not str(i).isdigit():
            try:
                int(str(i))
            except ValueError:
                return "Invalid input data"

    start = 0
    step = 1
    stop = 0
    result = []
    if len(args) == 1:
        stop = int(str(args[0]))
    elif len(args) >= 2:
        start = int(str(args[0]))
        stop = int(str(args[1]))
        if len(args) == 3:
            step = int(str(args[2]))
            if step == 0:
                return "The step cannot be zero"
    if step > 0:
        while start <= stop:
            result.append(start)
            start += step
        return result
    else:
        while start >= stop:
            result.append(start)
            start += step
        return result


# task 4
def to_title(string):
    words = string.split(" ")
    new_string = ""
    for word in range(len(words)):
        new_string += words[word].capitalize() + " "
    return new_string


# task 5
def count_symbol(string, symbol):
    count = 0
    for s in string:
        if s == symbol:
            count += 1
    return count


# task 6
def my_format(*args):
    template = args[0]
    n = 1
    i = 0
    while i < len(template):
        # для 'не позиционного' форматирования
        if template[i] == '{' and template[i + 1] == '}':
            if len(args) <= n:
                raise AttributeError("the argument is missing")
            template = template[:i] + args[n] + template[i + 2:]
            n += 1

        # для 'позиционного' формативарования
        elif template[i] == '{' and template[i + 1] != '}':
            temp = i
            while template[temp] != '}':
                temp += 1
            if len(args) < int(template[i + 1:temp]) + 1:
                raise AttributeError("the argument is missing")
            template = template[:i] + args[int(template[i + 1:temp]) + 1] + template[temp + 1:]
        i += 1
    return template


# task 7
def copy_file(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError
    if os.path.exists(destination):
        raise FileExistsError

    with open(source, 'r') as file_for_read:
        content = file_for_read.read()
    with open(destination, 'x') as file_for_write:
        file_for_write.write(content)


# task 9
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age

    def get_Name(self):
        return self.name
    def get_Age(self):
        return self.age


class Worker(User):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def set_Salary(self, salary):
        self.salary = salary

    def get_Salary(self):
        return self.salary


if __name__ == "__main__":
    print('task 1:', my_len([0, 1, 2, 3, 4]))
    print('task 2:', reverse([1, 2, 3, 4, 5]))
    print('task 3:', my_range(0, '20', 1))
    print('task 3:', my_range(15, 2, -2))
    print('task 4:', to_title('hello world'))
    print('task 5:', count_symbol('hello world', 'l'))
    print('task 6:', my_format('{1}, {0}, {2}', 'a', 'b', 'c'))
    print('task 6:', my_format('coordinates: {}, {}', '37.4N', '18.3W'))
    #copy_file('Hello1.txt', 'result.txt')
    # task 9
    john = Worker("John", 25, 1000)
    jack = Worker("Jack", 26, 2000)
    print('task 9:', f"Amount of salaries : {john.get_Salary() + jack.get_Salary()}")
