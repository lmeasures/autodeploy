
import errno
import os


def get_most_recently_modified_directory(search_path):
    return max([f for f in os.scandir(search_path)], key=lambda x: x.stat().st_mtime).path


def mkdir_p(path):
    print("||| Attempting to create directory", path)
    try:
        os.makedirs(path)
        print("|| Success")
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            print("|| Directory Exists")
            pass
        else: raise
        