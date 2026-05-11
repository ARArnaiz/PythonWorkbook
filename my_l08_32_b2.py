from pathlib import Path
import glob
import os

def get_file_sizes(somedir):
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    return { item.name : item.stat().st_size for item in p.iterdir() if item.is_file() }

print(get_file_sizes('.'))
print(get_file_sizes('c:/'))

def file_info(dirname):
    return {one_filename: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}

print(file_info('.'))
print(file_info('c:/'))