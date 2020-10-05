def replace(source, action):
    if action == "tab":
        return source.replace("    ", "\t")
    elif action == "space":
        return source.replace("\t", "    ")
    else:
        return False

string = input("Enter your string: ")
action = input("Enter \n tab: replace tabs with spaces \n space: replace spaces with tabs ")
print(replace(string, action))

