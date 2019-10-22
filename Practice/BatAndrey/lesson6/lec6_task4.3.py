from itertools import combinations


def combi(a):
    combi_res = list(combinations(a, 4))
    return combi_res


print(combi('password'))
