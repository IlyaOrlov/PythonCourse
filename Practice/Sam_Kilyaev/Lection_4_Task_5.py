string = input("Wrote your string: ")
dictionary = {"Ivan": "Gandalf", "Sergey": "Aragorn",
              "Nikolay": "Golum", "Vladimir": "Sauron",
              "Dmitriy": "Frodo", "Maksim": "Teodan"}


def replace_name(string, dictionary):
    for key, value in dictionary.items():
        string = string.replace(key, value)


print(replace_name(string))
