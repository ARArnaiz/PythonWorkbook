from pathlib import Path


def word_count(filename: str | Path) -> str:
    """Accepts a filename and returns counts of lines,
    characters, words (whitespace-delimited) and unique words
    (case-sensitive)."""
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')
    word_set = set()
    count_words = 0
    count_lines = 0
    count_chars = 0

    with open(p) as f:
        for line in f:
            count_lines += 1
            count_chars += len(line)
            words = line.split()
            count_words += len(words)
            word_set.update(words)
    return (f'Number of characters: {count_chars}\n'
            f'Number of words: {count_words}\n'
            f'Number of lines: {count_lines}\n'
            f'Number of unique words: {len(word_set)}')



def word_count2(filename: str | Path) -> str:
    """Accepts a filename and returns counts of lines,
    characters, words (whitespace-delimited) and unique words
    (case-sensitive)."""
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')
    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    word_set = set()

    with open(p) as f:
        for line in f:
            counts['lines'] += 1
            counts['characters'] += len(line)
            words = line.split()
            counts['words'] += len(words)
            word_set.update(words)
    return (f"[{p}]\n"
            f"Number of characters: {counts['characters']}\n"
            f"Number of words: {counts['words']}\n"
            f"Number of lines: {counts['lines']}\n"
            f"Number of unique words: {len(word_set)}")


print(word_count2("../wcfile.txt"))
print(word_count2("../article001.txt"))


def wordcount(filename):
    """Accepts a filename as an argument. Prints the number of lines,
characters, words (separated by whitespace) and different words
(case sensitive) in the file."""

    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()

    for one_line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())

        unique_words.update(one_line.split())

    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')


wordcount("../wcfile.txt")
wordcount("../article001.txt")
