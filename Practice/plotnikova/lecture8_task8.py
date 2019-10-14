import os

from Practice.plotnikova.lecture8_task7 import copyfile


def copydir(old_dir, new_dir):
    if not os.path.isdir(old_dir):
        return "Директория {} не найдена.".format(old_dir)
    for root, directories, files in os.walk(old_dir):
        [os.makedirs(os.path.join(new_dir, root, c)) for c in directories if not os.path.exists( os.path.join(new_dir, root, c))]
        [copyfile(os.path.join(root, c), os.path.join(new_dir, root, c)) for c in files]
    return "Директория {} успешно скопирована в директорию {}".format(old_dir, new_dir)

old_dir="old_dir"
new_dir="new_dir"
print(copydir(old_dir, new_dir))
