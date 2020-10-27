def count_symbol(st, smb):
    a = 0
    for char in st:
        if char == smb:
            a += 1
    return a


