import re


def my_format(string, *argv):
    patterns = {*re.findall(r"{\d+}", string)}
    print("patterns: " + str(patterns))
    for pat in patterns:
        index = int(pat[1:-1])
        if index >= len(argv):
            print(f"incorrect index {{{index}}}")
            return None
        string = string.replace(pat, str(argv[index]))
    return string


if __name__ == "__main__":
    string = ' sdfdf {1} saf {0} so {1}'
    print(my_format(string, 23, 'some'))
