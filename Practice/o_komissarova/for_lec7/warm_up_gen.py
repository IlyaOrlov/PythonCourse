def my_gen(file_name):
    with open(file_name) as f:
        for line in f:
            yield line


for i in my_gen('text.txt'):
    print(i)
