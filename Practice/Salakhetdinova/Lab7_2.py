import subprocess

def read_file(new_file):
    process = subprocess.Popen(['type', new_file], shell=True)
    process.wait()
    result = process.communicate()
    if process.returncode:
        return result[1]
    return result[0]

file = 'file.txt'
print(read_file(file))