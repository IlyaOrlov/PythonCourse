import os.path


def copyfile(source_name, dest_name, rewrite=True):
    if source_name.find("/") < 0:
        source_name = "./{}".format(source_name)
    if dest_name.find("/") < 0:
        dest_name = "./{}".format(dest_name)
    try:
        with open(source_name) as source_file:
            if rewrite:
                mode = "w"
            else:
                mode = "x"
            with open(dest_name, mode) as dest_file:
                for each in source_file.readlines():
                    dest_file.writelines(each)
    except IOError as e:
        print("Fail opening file {}: {}".format(e.filename, e.strerror))
    else:
        if os.path.exists(dest_name):
            print("Copying is finished")
        else:
            print("File was not copied")


if __name__ == "__main__":
    copyfile("source7-7.txt", "dest7-7.txt")
