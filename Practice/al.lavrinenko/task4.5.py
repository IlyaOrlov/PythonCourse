def replacement(string, format_dict):
    str_list = string.split()
    return ' '.join([format_dict[str_list[i]] if str_list[i] in format_dict
                     else str_list[i] for i in range(len(str_list))])


some_string = "Красная армия располагала 670 тысячами солдат, 7 тысячами " \
              "орудий, 700 танками и 700 самолётами"
some_dict = {'670': 'шестьсот семьюдесятью', '7': 'семью', '700': '700-ами'}
print(replacement(some_string, some_dict))
