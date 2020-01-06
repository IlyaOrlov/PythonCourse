if __name__ == '__main__':

    message = "0 - replace  tab with space\n1 - replace space with tab"
    print(message)
    direction = int(input())

    string = "2    34\t234\tdf    sf\t3sfv"
    print(string)

    if direction is 0:
        string = string.replace('\t', '    ')
    elif direction is 1:
        string = string.replace('    ', '\t')
    else:
        print ("Âinput correct action")

    print(string)