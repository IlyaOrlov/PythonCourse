def copyfile(file1, file2):
    try:
        with open(file1, 'r') as f1:
            with open(file2, 'x') as f2:
                f2.write(f1.read())
        
        for line in f2:
            print(line)

    except IOError:
        print("An IOError has occurred!")





copyfile('source.txt', 'destination.txt')