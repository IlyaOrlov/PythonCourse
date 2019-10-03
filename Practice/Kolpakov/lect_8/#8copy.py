import os


def copyfile(source_f, destination_f):
    try:
        fo = open(source_f, "r")
    except FileNotFoundError:
        return "File doesn't exist"
    except Exception as exc:
        return "Some unexpected error: {}".format(exc)
    else:
        try:
            fw = open(destination_f, "x")
            fw.write(fo.read())
        except Exception as exc:
            return "Some unexpected error: {}".format(exc)
        else:
            return 'write to file2 done'
        finally:
            fo.close()


def copydir(source, destination):
    copyfiles = []
    try:
        for f in os.listdir(source):
            if os.path.isfile(os.path.join(source, f)):
                copyfiles.append(f)
    except FileNotFoundError:
        print("File doesn't exist")
    else:
        try:
            os.mkdir(destination)
        except FileExistsError:
            print("File exists")
        except Exception as exc:
            print("Some unexpected error: {}".format(exc))
        else:
            for f in copyfiles:
                source_f = os.path.join(source, f)
                destination_f = os.path.join(destination, f)
                copyfile(source_f, destination_f)
            print('file copying completed')
        #print(source_f, destination_f)


copydir('./test', './test2')
