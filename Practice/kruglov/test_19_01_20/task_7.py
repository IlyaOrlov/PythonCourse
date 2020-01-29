# 7 function copy_file
import os.path


def copy_file(
    source=input('Please enter source file name:'),
    destination=input('Please enter destination file name:')
):
    try:
        with open(source, "r") as f_src:
            if os.path.isfile('d'):
                print("Error: File existing!")
            else:
                with open(destination, "w") as f_dst:
                    f_dst.write(f_src.read())
    except FileNotFoundError:
        print("Error: Please create 'source' file!")


copy_file()
