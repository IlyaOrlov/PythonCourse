import subprocess


def cat_file(file_name):
    process = subprocess.Popen(["type", file_name], shell=True)
    process.wait()
    result = process.communicate()

    if process.returncode:
        for line in result:
            print(line)


if __name__ == "__main__":
    cat_file("test.txt")   # this file into the dir, for other file has to be full path
