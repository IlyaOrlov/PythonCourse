def copyfile(source_f, destination_f):
    try:
        #fo = open(source_f,"r")
        with open(source_f, 'r') as fo:
            r =fo.read()
    except FileNotFoundError:
        return "File doesn't exist"
    except Exception as exc:
        return "Some unexpected error: {}".format(exc)
    else:
        try:
            with open(destination_f, "x") as fw:
                fw.write(r)
        except Exception as exc:
            return "Some unexpected error: {}".format(exc)
        else:
            #fo.close()
            return 'write to file2 done'

print(copyfile('./test/test1.txt', './test/file2.txt'))