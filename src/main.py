import os
import shutil
import sys

from copystatic import copy_files_recursive
from markdown import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    basepath = "/"
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")

    generate_pages_recursive(basepath, "content", "template.html", "docs")


main()