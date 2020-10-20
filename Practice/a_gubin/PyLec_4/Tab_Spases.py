def tabs_to_spases(string):
    return string.replace('\t', '    ')


def spases_to_tabs(string):
    return string.replace('    ', '\t')


string = '\tsome\ttext'
print(tabs_to_spases(string))
print(spases_to_tabs(tabs_to_spases(string)))
