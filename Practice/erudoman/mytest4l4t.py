with open('for_mytest4l4t.txt') as file_old:
    newtext = file_old.read()

newtext = newtext.replace("\t", "    ")

with open("for_mytest4l4t_new.txt", "w") as file_new:
    file_new.write(newtext)