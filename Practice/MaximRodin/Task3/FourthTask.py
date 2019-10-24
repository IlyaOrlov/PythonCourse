
def tab_in_prob(a):
    a = input('Введите строку: ')

    new_str = a.replace('    ', '\t')

def tab_in_prob(str):
    str = input('Введите строку: ')

    new_str = str.replace('    ', '\t')

    print(new_str)


tab_in_prob(str)

def prob_in_tab(a):
    a = 'English\tis good\t\tlanguage\t\ttest!'
    new_str = a.replace('\t', '    ')

def prob_in_tab(str):
    str = 'English\tis good\t\tlanguage\t\ttest!'
    new_str = str.replace('\t', '    ')

    print(new_str)
prob_in_tab(str)
