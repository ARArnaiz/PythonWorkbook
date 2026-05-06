from pathlib import Path
import os

def get_longest_word(filename) -> str:
    """
    Return the longest word found in a text file.

    Strips common punctuation from each word before comparing lengths.
    In the event of a tie, the later word wins (>=).

    Args:
        filename: Path to the file to read (str or Path-like).

    Returns:
        The longest word found, or an empty string if the file is empty.
    """
    lword = ''
    with open(filename, errors='ignore') as f:
        for line in f:
            for word in line.split():
                word = word.strip('\'.,!?";:()[]—-')
                if len(word) >= len(lword):
                    lword = word
    return lword

def get_dir_longest_words(somedir: str | Path) -> dict[str, str]:
    """
    Return the longest word from each .txt and .md file in a directory.

    Iterates over the immediate contents of `somedir` (non-recursive),
    calling get_longest_word() on each qualifying file.

    Args:
        somedir: Path to the directory to scan (str or Path-like).

    Returns:
        A dict mapping each file's string path to its longest word.

    Raises:
        NotADirectoryError: If `somedir` does not point to a directory.
    """
    p = Path(somedir)
    if not p.is_dir():
        raise NotADirectoryError(f"Not a directory: {somedir}")
    lwords = {}
    for item in p.iterdir():
        if item.is_file() and item.suffix in ('.txt', '.md'):
            lwords[str(item)] = get_longest_word(item)
    return lwords



def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename, errors='ignore'):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word

def find_all_longest_words(dirname):
    return {filename:
            find_longest_word(os.path.join(dirname,
                                    filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname,
                                    filename))}


if __name__ == '__main__':
    print(get_dir_longest_words('..'))
    print(find_all_longest_words('.'))
