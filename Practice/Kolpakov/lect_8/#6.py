def rep(s, *args,):
    kol= s.count('{}')
    for i, arg in enumerate(args):
        key = '{' + str(i) + '}'
        if key in s:
            if len(s.split()) == len(args):
                s = s.replace(key, arg)
            else:
                return 'ERROR'
        else:
            if kol == len(args):
                s = s.replace('{}', arg, 1)
            else:
                return 'ERROR'
    return s



print(rep('{1}, {2}, {0}', 'a', 'b', 'c'))
print(rep('coordinates: {}, {}', '37.4N', '18.3W'))





