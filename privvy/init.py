import os, shutil
from subprocess import Popen

from .sync import sync

ROOT = os.path.join(os.path.dirname(__file__), "..")

def append_files(file1, file2):
    if os.path.exists(file1):
        with open(file1, 'ab') as f:
            f.write("\n")
            f.write(open(file2, 'rb').read())
    else:
        with open(file1, 'wb') as g:
            g.write(open(file2, 'rb').read())

if __name__ == "__main__":
    if not os.path.exists(".git"):
        print("Please run this command in the root directory of a git repository")

    dst = os.path.join(".git", "hooks")
    src = os.path.join(os.path.dirname(__file__), "..", "hooks")

    for hook in os.listdir(src):
        dst_hook = os.path.join(dst, hook)
        src_hook = os.path.join(src, hook)
        append_files(dst_hook, src_hook)
