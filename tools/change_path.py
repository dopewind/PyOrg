import os


def c_path(dir_path):

    print("Current Working Directory ", os.getcwd())

    try:
        # Change the current working Directory
        os.chdir(dir_path)
        print(dir_path)
    except OSError:
        print("Can't change the Current Working Directory")
    print("Current Working Directory ", os.getcwd())

    # Check if New path exists
    if os.path.exists(dir_path):
        # Change the current working Directory
        os.chdir(dir_path)
    else:
        print("Can't change the Current Working Directory")

    print("Current Working Directory ", os.getcwd())


if __name__ == '__main__':
    c_path()
