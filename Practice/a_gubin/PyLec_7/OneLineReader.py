import sys


def one_line_reader(file_name="test.txt"):
    try:
        with open(file_name) as file:
            for line in file:
                yield line
    except OSError:
        yield f"The file '{file_name}' openning failed\n"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for line in one_line_reader(sys.argv[1]):
            print(line, end='')
    else:
        print("The file name are missed")
