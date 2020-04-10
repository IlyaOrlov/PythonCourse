def dict_create():
    created_dict = {}
    while True:
        a = input("input key")
        if a == "stop":
            break
        b = input("input value")
        created_dict[a] = b
    return created_dict


r = dict_create()
#r = {'dog': 'sobaka', 'cat': 'koshka', 'mouse': 'mysh'} ////// test_dictionary
with open("222") as work_file:
    for str in work_file.readlines():
        prom = str.split()
        for each in prom:
            if r.get(each) != None:
                str = str.replace(each, r.get(each))
            else:
                print('no values in dict')
        print(str)
        with open("replacing", 'a') as new_file:
            new_file.writelines(str)

