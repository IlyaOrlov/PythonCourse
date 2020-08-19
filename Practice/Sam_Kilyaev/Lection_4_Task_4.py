import re

your_string = input("Write your string: ")
your_want = input("1:Replace tabs with spaces 2:Replace spaces with tabs - ")


def replace(string, want):
    if want == "1":
        result = re.sub('\t', '    ', string)
        print(result)
    elif want == "2":
        result = re.sub(' {4}', '\t', string)
        print(result)


replace(your_string, your_want)
