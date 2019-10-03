def copyfile(source, destination):
    try:
        fo = open(source,"r")
    except FileNotFoundError:
        return "File doesn't exist"
    except Exception as exc:
        return "Some unexpected error: {}".format(exc)
    else:
        try:
            fw = open(destination, "x")
            fw.write(fo.read())
        except Exception as exc:
            return "Some unexpected error: {}".format(exc)
        else:
            return 'write to file2 done'
        finally:
            fo.close()



print(copyfile('./test/test1.txt', './test/file2.txt'))