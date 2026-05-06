from pathlib import Path
import glob
import hashlib


def getfilename_hashes(somedir: str | Path) -> dict[str, str]:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    try:
        return {str(item): hashlib.md5(str(item).encode()).hexdigest()
                for item in p.iterdir() if item.is_file()}
    except OSError as e:
        print(f"Error processing directory {somedir}: {e}")
        return {}


def getfilename_hashes_c(somedir: str | Path) -> dict[str, str]:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    hashes = {}
    for item in p.iterdir():
        if item.is_file():
            try:
                hashes[str(item)] = hashlib.md5(str(item).encode()).hexdigest()
            except OSError as e:
                print(f"Skipping {item}: {e}")
    return hashes

def hash_files(somedir: str | Path) -> dict[str, str]:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    hashes = {}
    for item in p.iterdir():
        if item.is_file():
            try:
                hashes[str(item)] = hashlib.md5(item.read_bytes()).hexdigest()
            except OSError as e:
                print(f"Skipping {item}: {e}")
    return hashes

def md5_files(dirname):
    output = {}

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            m = hashlib.md5()
            m.update(one_filename.encode())
            output[one_filename] = m.hexdigest()
        except:
            pass

    return output


if __name__ == '__main__':

    print(getfilename_hashes('..'))
    print(getfilename_hashes_c('..'))
    print(hash_files('..'))
    print(md5_files('.'))
