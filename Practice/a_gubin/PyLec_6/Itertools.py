import itertools


def chaining(ar1, ar2, ar3):
    return list(itertools.chain(ar1, ar2, ar3))


def len_less(seq, max=5):
    return list(itertools.filterfalse(lambda x: len(x) < max, seq))


def pswd_comb(pswd):
    return list(itertools.combinations(pswd, 4))


if __name__ == "__main__":
    ar1 = [1, 2, 3]
    ar2 = [4, 5]
    ar3 = [6, 7]
    print(f"chaining :\n{chaining(ar1, ar2, ar3)}\n")
    seq = ['hello', 'i', 'write', 'cool', 'code']
    print(f"len_less: \n{len_less(seq)}\n")
    pswd = 'password'
    print("pswd_comb:")
    print(*pswd_comb(pswd), sep='\n')
