s = '\tРавным образом повышение уровня\t гражданского сознания представляет\t \n' \
    '\tсобой интересный\t эксперимент проверки системы обучения к \n' \
    '\tкадров, соответствующей насущным\t потребностям?'


def deploy(text):
    return text.expandtabs(4)


def redeploy(text):
    space = "    "
    if space in text:
        return text.replace(space, '\t')


print(deploy(s))
