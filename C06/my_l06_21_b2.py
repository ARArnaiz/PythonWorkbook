import arrow
from pathlib import Path
import glob
import os

def get_files_dir_date(somedir: str | Path) -> dict[str, str]:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    files = {}
    for item in [p] + list(p.iterdir()):
        if item == p or item.is_file():
            try:
                mtime =  arrow.get(item.stat().st_mtime).humanize()
                files[str(item)] = mtime
            except OSError as e:
                print(f"Skipping {item}: {e}")
    return files

dirname = input("Enter a directory name: ")
print(get_files_dir_date(dirname))


def mod_times(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            mod_time = os.stat(one_filename).st_mtime
            output[one_filename] = (arrow.now() - arrow.get(os.stat(one_filename).st_mtime)).days

        except:
            pass

    return output

print(mod_times(dirname))


def get_files_dir_mod_c(somedir):
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")

    results = {}
    for item in [p] + list(p.iterdir()):
        if item == p or item.is_file():
            try:
                mtime = item.stat().st_mtime
                results[str(item)] = arrow.get(mtime).humanize()  # "3 days ago"
            except OSError as e:
                print(f"Skipping {item}: {e}")
    return results

print(get_files_dir_mod_c(dirname))