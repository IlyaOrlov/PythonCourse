def v1_tab_or_spaces(line, tab_to_spaces=True):
    str_ = list(line)
    new_arr = []

    if tab_to_spaces is True:           # for '\t'=4spaces
        for char in str_:
            if char == '\t':
                new_arr.append("    ")
            else:
                new_arr.append(char)

        print("".join(new_arr))        # or return new_line

    else:                             # if tab_to_spaces==False for 4spaces='\t'
        count_spaces = 0
        flag = 0            # flag==1  - into word
        for char in str_:
            if char == ' ':
                flag = 0
                count_spaces += 1
                if count_spaces == 4:
                    new_arr.append("\t")
                    count_spaces = 0

            else:
                if count_spaces != 0:
                    new_arr.append(' ' * count_spaces)  # if 1, 2 or 3 spaces
                    new_arr.append(char)
                    flag = 1
                    count_spaces = 0

                else:
                    new_arr.append(char)
                    flag = 1
                    count_spaces = 0


        print("".join(new_arr))  # or return new_line


def v2_tab_or_spaces(line, tab_to_spaces=True):
    if tab_to_spaces is True:   # for '\t'=4spaces
        new_arr = line.split('\t')
        new_line = '    '.join(new_arr)
        print(new_line)        # or return

    else:                      # for 4spaces='\t'
        new_arr = line.split('    ')
        new_line = '\t'.join(new_arr)
        print(new_line)         # or return


def v3_tab_or_spaces(line, tab_to_spaces=True):
    if tab_to_spaces is True:  # for '\t'=4spaces
        # return line.expandtabs(tabsize=4) - it's the first idea,
        # but correctly only the first replacement and... v1 and v2 were made
        return line.replace("\t", "    ")

    return line.replace("    ", "\t")  # for 4spaces='\t'


line_tab = "\tOne\tTwo...Three\tFour\t...Five"
v1_tab_or_spaces(line_tab)
v2_tab_or_spaces(line_tab)
print(v3_tab_or_spaces(line_tab))

line_with_spaces = "    Five Four    Three  Two    One    "
v1_tab_or_spaces(line_with_spaces, tab_to_spaces=False)
v2_tab_or_spaces(line_with_spaces, tab_to_spaces=False)
print(v3_tab_or_spaces(line_with_spaces, tab_to_spaces=False))
