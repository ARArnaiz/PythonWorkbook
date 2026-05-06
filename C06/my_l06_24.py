from pathlib import Path


def format_file_in_reverse(filename: str | Path, outputfile: str | Path) -> None:
    '''Reads a file and writes its lines in reverse order to another file.'''
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File {filename} does not exist.")
    with open(filename, 'r', encoding='utf-8') as finput, open(outputfile, 'w', encoding='utf-8') as foutput:
        for line in finput:
            foutput.write(line.strip()[::-1] + '\n')


def reverse_lines_c(
        infilename: str | Path,
        outfilename: str | Path,
        encoding: str = 'utf-8',
) -> None:
    """Read a file and write each line reversed (character-wise) to another file.

    Leading whitespace is preserved; only trailing whitespace is stripped.

    Args:
        infilename: Path to the input file.
        outfilename: Path to the output file.
        encoding: File encoding to use (default: utf-8).

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    p = Path(infilename)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {infilename}")

    with (
        open(p, 'r', encoding=encoding) as infile,
        open(outfilename, 'w', encoding=encoding) as outfile,
    ):
        for line in infile:
            outfile.write(f'{line.rstrip()[::-1]}\n')


def reverse_lines(infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')


if __name__ == "__main__":
    format_file_in_reverse('../article001.txt', 'output_article001.txt')
    reverse_lines_c('../article001.txt', 'output_article001_c.txt')
    reverse_lines('article001.txt', 'output_article001_l.txt')
