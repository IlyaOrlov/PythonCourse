from lec8.t_7 import copyfile
import os


def copydir(src_dir, copy_to):
    if not os.path.isdir(src_dir):
        raise OSError('No such directory')
    for curr_dir, _, files in os.walk(src_dir):
        copy_path = curr_dir.replace(os.path.dirname(src_dir.rstrip('\\')),
                                     copy_to + '\\')
        os.mkdir(copy_path)
        for file_name in files:
            copyfile(os.path.join(curr_dir, file_name),
                     os.path.join(copy_path, file_name))


copydir(r'C:\p_test', r'C:\Games')
