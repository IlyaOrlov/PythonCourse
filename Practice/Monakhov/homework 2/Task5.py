def replacer(S, D):
    for key in D.keys():
        S = S.replace(key, str(D[key]))
    return S


d = {'one': 1, 'two': 2}
s = 'one plus two is 3'
s = replacer(s, d)
print(s)
