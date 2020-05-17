def copyfile(source, destination):
    with open(source, 'r') as f_s:
        data = f_s.read()
        with open(destination, 'x') as f_d:
            f_d.write(data)


if __name__ == "__main__":
    # copyfile('no_file.txt', 'd.txt')
    copyfile('s1.txt', 'd1.txt')
    copyfile('s1.txt', 'd1.txt')
