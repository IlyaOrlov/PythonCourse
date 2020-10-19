import os
import shutil
import sys


def copydir(src, dst):

    def copying(src_root, dst_root):
        level = os.scandir(src_root)
        for item in level:
            if item.is_dir():
                os.mkdir(os.path.join(dst_root, item.name))
                copying(os.path.join(src_root, item.name), os.path.join(dst_root, item.name))
            elif item.is_file():
                shutil.copyfile(os.path.join(src_root, item.name), os.path.join(dst_root, item.name))

    if not os.path.exists(src):
        raise OSError
    if not os.path.exists(dst):
        raise OSError
    os.mkdir(os.path.join(dst, os.path.basename(src)))
    copying(src, os.path.join(dst, os.path.basename(src)))


# def copying(src_root, dst_root):
#     level = os.scandir(src_root)
#     for item in level:
#         if item.is_dir():
#             os.mkdir(os.path.join(dst_root, item.name))
#             copying(os.path.join(src_root, item.name), os.path.join(dst_root, item.name))
#         elif item.is_file():
#             shutil.copyfile(os.path.join(src_root, item.name), os.path.join(dst_root, item.name))


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[1]
    copydir(src, dst)
