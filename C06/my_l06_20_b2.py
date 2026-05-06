from pathlib import Path
import glob
import os

def get_file_sizes(somedir):
    fdict = {}
    p = Path(somedir)
    for item in p.iterdir():
        if item.is_file():
            fdict[item.name] = item.stat().st_size
    return fdict

print(get_file_sizes('.'))
print(get_file_sizes('c:/'))

def get_file_sizes_c(somedir: str | Path) -> dict[str, int]:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    return { item.name : item.stat().st_size
             for item in p.iterdir() if item.is_file() }

print(get_file_sizes_c('..'))
print(get_file_sizes_c('c:/'))


def file_sizes(dirname):
    counts = {one_filename: os.stat(one_filename).st_size
              for one_filename in glob.glob(f'{dirname}/*')
              if os.path.isfile(one_filename)}

    return counts

print(file_sizes('.'))
print(file_sizes('c:/'))