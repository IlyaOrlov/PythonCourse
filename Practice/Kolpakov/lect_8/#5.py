#Num 5
def count_symbol(s,k):
    bukv = 0
    for i in range(len(s)):
        if s[i] == k:
            bukv += 1
    return bukv


s = 'dhhj df55 ghk 346'
print(count_symbol(s, 'd'))