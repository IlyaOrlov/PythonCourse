import ex7_7
import os


def copydir(source_name, dest_name = "copy", rewrite=True):
    if source_name.find("/") < 0:
        source_name = "./{}".format(source_name)
    if dest_name == "copy":
        dest_name = "{}/copy".format(source_name)
    if dest_name.find("/") < 0:
        dest_name = "./{}".format(dest_name)
    try:
        lst = os.listdir(source_name)
        for each in lst:
            if os.path.isdir("{}/{}".format(source_name, each)):
                new_dir_path = "{}/{}".format(dest_name, each)
                os.makedirs(new_dir_path, exist_ok=rewrite)
                # print("{} directory was copied to {}"
                # .format(each, new_dir_path))
                copydir("{}/{}".format(source_name, each),
                        new_dir_path, rewrite)
            elif os.path.isfile("{}/{}".format(source_name, each)):
                new_file_path = "{}/{}".format(dest_name, each)
                ex7_7.copyfile("{}/{}".format(source_name, each),
                               new_file_path, rewrite)
                # print("{} file was copied to {}"
                # .format(each, new_file_path))
    except FileNotFoundError as e:
        print("Source directory {} not founded", e.filename)
    except FileExistsError as e:
        print("Destination directory {} already exist", e.filename)
        print("Maybe should use another rewrite mode?")
    else:
        for each in lst:
            if os.path.exists("{}/{}".format(dest_name, each)):
                print("File or folder {}/{} is copied/rewrited"
                      .format(dest_name, each))
            else:
                print("File or folder {}/{} is  not copied/rewrited"
                      .format(dest_name, each))


if __name__ == "__main__":
    copydir("ex7_8sd", "ex7_8dd")
