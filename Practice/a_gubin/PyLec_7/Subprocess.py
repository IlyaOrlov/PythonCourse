import subprocess
import os
import sys


def read_file(file_name):
    res = subprocess.run(["cat", file_name], text=True, capture_output=True)
    print(*res.stdout.splitlines(), sep='\n')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("The file name not found")
    else:
        if os.path.exists(sys.argv[1]):
            read_file(sys.argv[1])
        else:
            print(f"The path '{sys.argv[1]}' doesn't exist")