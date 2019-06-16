def tab_and_space(arr, key):
    if key == '\t':
        arr = arr.expandtabs(tabsize=4)
        print(arr)
    elif key == '    ':
        arr = arr.replace('    ', '\t')
        print(arr)
    else:
        print("Unknown key")


buf1 = "    Hello, World!    World!    Hello"
tab_and_space(buf1, '    ')
buf2 = "\tHello, World!\tWorld!\tHello"
tab_and_space(buf2, '\t')
