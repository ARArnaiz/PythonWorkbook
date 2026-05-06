import glob
from pathlib import Path
from collections import Counter


def get_most_common_letters(somedir: str | Path) -> list[str]:
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")

    char_count = Counter()
    for item in p.iterdir():
        if item.is_file():
            with open(item, errors='ignore') as f:
                for line in f:
                    char_count.update(char.lower() for char in line if char.isalpha())
    return [letter for letter, _ in char_count.most_common(5)]


print(get_most_common_letters('..'))


def most_common_letters(dirname):
    counts = Counter()

    for one_filename in glob.glob(f'{dirname}/*'):
        try:
            for one_line in open(one_filename):
                counts.update(one_line)
        except:
            pass

    return list(dict(counts.most_common(5)).keys())


print(most_common_letters('.'))
