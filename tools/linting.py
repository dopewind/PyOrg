from os import chdir
import subprocess  # To run pyflakes and get output
import os
import glob
from subprocess import STDOUT


def c_lint():
    dir_now = os.getcwd()
    print(dir_now)
    os.chdir(dir_now[0:len(dir_now) - 5])
    print(os.getcwd())
    py_files = glob.glob('./**/*.py', recursive=True)
    for files in py_files:
        if "Deprecated" in files:
            py_files.remove(str(files))
            print(files)
            print(' ')
    print(' ')
    print(py_files)
    for file in py_files:
        subprocess.run(['pyflakes', file],
                       stdout=subprocess.PIPE).stdout.decode('utf-8')
    return STDOUT


passed = (c_lint())
print(passed)
# os.environ['lint_status'] = passed
