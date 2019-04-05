import os


def copyfile(source, destination):
    a = None
    try:
        with open('source.txt', 'r') as f:
            a = f.readlines()
    except FileNotFoundError as nf:
        print(nf)
    if os.path.exists('source.txt') == True:
        # Python пишет, что выражение в 11 строке может быть упрощено,
        # но не пойму как.
        try:
            with open('destination.txt', 'x') as fl:
                fl.writelines(a)
        except IOError as ioe:
            print(ioe)


copyfile(source='source.txt', destination='destination.txt')
