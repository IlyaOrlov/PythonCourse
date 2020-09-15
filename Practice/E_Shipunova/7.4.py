import os
import datetime
from pathlib import Path


def del_all(path_to_dir):
    '''
    The function creates infinity('while: True') tracking for maximally introduced dir,
    while the dir has files and dirs, and deletes dir only it is empty. After the function
    goes to less nested level.
    For testing were created: dir test(f1.txt and dir p1(f2.txt, dir p2(empty), dir p3(f131.txt, f132.txt)).
    :argument is path_to_dir
    :return is None
    '''
    static_main_dir = path_to_dir                                     # for remember name of our main dir
    print(static_main_dir)

    def del_in_dir(path_to_dir):
        while True:
            for i in os.listdir(path_to_dir):
                path_of_item = os.path.join(path_to_dir, i)           # for reading
                if os.path.isfile(path_of_item):
                    print(f" ' {i} ' is file")                        # for testing
                    time_of_create = datetime.datetime.fromtimestamp(os.path.getctime(path_of_item))
                    min_of_live = (datetime.datetime.now() - time_of_create).seconds // 60  # [min]
                    if min_of_live >= 1:  # >= 1 [min]
                        print(f"delete file {i}")                      # for testing
                        os.remove(path_of_item)                        # delete file
                    else:                                              # for testing
                        print(f"{i} is young")

                else:
                    print(f"' {i} '  is dir")                           # for testing
                    #is_empty = not bool(sorted(Path(path_of_item).rglob('*')))
                    #if not is_empty:                                   # only if the dir isn't empty
                    print(f"======> go to into {path_of_item}")         # for testing
                    del_in_dir(path_of_item)                            # go into this dir

                    # after  'go to into dir'
                    time_of_create = datetime.datetime.fromtimestamp(os.path.getctime(path_of_item))
                    min_of_live = (datetime.datetime.now() - time_of_create).seconds // 60  # [min]
                    if min_of_live >= 2:                               # >= 2 [min]
                        print(f"delete dir {i}")                       # for testing
                        try:
                            os.rmdir(os.path.join(path_to_dir, i))     # delete only empty dir, else it trows Exception
                        except OSError:
                            print(f"Dir({i}) is not empty! I can not delete it.")
                    else:                                              # for testing
                        print(f"dir {i} is young")

            is_empty = not bool(sorted(Path(path_to_dir).rglob('*')))
            if is_empty and path_to_dir != static_main_dir:            # if dir is empty and it isn't main dir
                break

    del_in_dir(path_to_dir)


if __name__ == "__main__":
    del_all('./test')
