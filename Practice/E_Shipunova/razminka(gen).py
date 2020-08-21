def file_reader(file_name):
    with open(file_name,"r") as f:
        for line in f:
            yield line


if __name__ == "__main__":
    generator = file_reader("test.txt")
    print(next(generator))
    print(next(generator))
    print(next(generator))
