import subprocess


def cat_file(file_name):
    process = subprocess.Popen(["type", file_name], shell=True)
    process.wait()
    result = process.communicate()

    if process.returncode:
        for line in result:
            print(line)


if __name__ == "__main__":
    cat_file("C:\Users\Виктор\PycharmProjects\L7T2\example.txt")