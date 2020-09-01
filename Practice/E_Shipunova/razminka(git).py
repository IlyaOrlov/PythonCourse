import re


def get_git_commands(file_name):
    with open(file_name, "r") as f:
        commands = []
        for line in f:
            commands += re.findall('(git [a-z]+[^а-яА-Я)\n"]+)', line)

    i = 0
    for command in commands:
        correctly_line = re.search('(git .*git) ', command)  # but, in the second line I get command with " -"
        if correctly_line:
            commands[i] = correctly_line.group()
        print(commands[i])
        i += 1


if __name__ == "__main__":
    get_git_commands("git.txt")
