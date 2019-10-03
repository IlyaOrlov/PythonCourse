def my_gen_read(file):
    with open(file) as f:
        for lines in f:
            yield lines.strip()


for line in my_gen_read('test.txt'):
    print(line)
