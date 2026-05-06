from os import listdir, path
import json

def get_extensions(dirname: str) -> set:
    return { path.splitext(f)[1] for f in listdir(dirname) }

print(get_extensions('.'))