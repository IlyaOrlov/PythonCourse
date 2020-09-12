import re


def find_git(path):
    with open(path) as f:
        text = f.read()
        result = set(re.findall('git [a-z,A-Z]+', text))
        print(result)


find_git('../dir/README.md')
