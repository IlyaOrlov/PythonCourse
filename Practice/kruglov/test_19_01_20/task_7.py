# 7 function copy_file


def count_symbol(source='s', destination='d'):
    # source = input("Please enter source file name:")
    # destination = input("Please enter destination file name:")
    with open(source, "r") as f_src:
        # f_src.write("Hello")
        with open(destination, "w") as f_dst:
            f_dst.write(f_src.read())


count_symbol()
