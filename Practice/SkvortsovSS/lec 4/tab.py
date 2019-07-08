def tab(str):
    if str.find("\t")==True:
       print(str.expandtabs(4))
    elif str.find("    ")==True:
       print("fgf",str.replace("    ", "\t"))
    else:
        print("there are no spaces or tabs in the string")

tab('d\td')