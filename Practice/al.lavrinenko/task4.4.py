def string_conversion(e_string, e_type):
    if e_type == 1:
        return e_string.replace('\t', '    ')
    elif e_type == 2:
        return e_string.replace('    ', '\t')
    else:
        print('Error: wrong edit type')


while True:
    input_type = int(input("Enter 1 if you want to edit the file or 2 if you want to edit the string: "))
    if input_type == 1:
        file_path = input('Enter the file path (name): ')
        with open(file_path, 'r') as file:
            string_to_edit = file.read()
        break
    elif input_type == 2:
        string_to_edit = input('Enter the string: ')
        break
    else:
        print("Error: there's no 1 or 2, try again")

while True:
    edit_type = int(input("Enter 1 for 'Tabs to 4 spaces' conversion or 2 for '4 spaces to tabs conversion': "))
    if edit_type != 1 and edit_type != 2:
        print("Error: there's no 1 or 2, try again")
    else:
        edited_string = string_conversion(string_to_edit, edit_type)
        if input_type == 1:
            with open(file_path, 'w') as file:
                file.write(edited_string)
        else:
            print(edited_string)
        break
