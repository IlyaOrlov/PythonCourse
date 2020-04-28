import subprocess

def filerider(name):
    subprocess.run(['type', name], shell=True)

filerider("proba")