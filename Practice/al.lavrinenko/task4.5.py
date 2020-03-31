def replacement(string, format_dict):
    for pattern in sorted(format_dict, key=len, reverse=True):
        string = string.replace(pattern, format_dict[pattern])
    return string


some_string = "Красная армия располагала 670 тысячами солдат, 7 тысячами орудий, 700 танками и 700 самолётами"
some_dict = {'670': 'шестьсот семьюдесятью', '7': 'семью', '700': 'семьюстами'}
print(replacement(some_string, some_dict))
