from dev.lint_check import c_lint
import os

root_dir = os.path.realpath('main.py')
print('Setting current dir to root of project')
print('Root of project is at', root_dir)

c_lint(root_dir)
