def replace_space_on_tab(stroka):
    tab = '\t'
    space = '    '
    if space or tab in stroka:
        print('have this symbol')
        new_stroka = stroka.replace('    ', '\t')
        print(new_stroka)
    else:
        print('not')


def replace_tab_on_space(stroka):
    tab = '\t'
    space = '    '
    if space or tab in stroka:
        print('have this symbol')
        new_stroka = stroka.replace('\t', '    ')
        print(new_stroka)
    else:
        print('not')


replace_space_on_tab('sa    ddas    dasd    ds')
replace_tab_on_space('asdas\tasdasd\ta\te')