import subprocess  # To run pyflakes and get output
import glob
import tools.change_path as change_path


def c_lint(dir_path):
    change_path.c_path(dir_path)
    py_files = glob.glob('*.py', recursive=True)
    print(py_files)
    for file in py_files:
        subprocess.run(['pyflakes', file],
                       stdout=subprocess.PIPE).stdout.decode('utf-8')
