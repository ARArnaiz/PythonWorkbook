from pathlib import Path


def file_encode(filename: str | Path, outputfile: str | Path, encoding: str = 'utf-8') -> None:
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File {filename} does not exist.")
    with (open(filename, 'r', encoding=encoding) as finput,
          open(outputfile, 'w', encoding=encoding) as foutput
          ):
        for line in finput:
            ordinals = [ord(c) for c in line]
            foutput.write(','.join(str(i) for i in ordinals) + '\n')

file_encode("../wcfile.txt", "wcfile_encoded.txt")

def file_decode(filename: str | Path, outputfile: str | Path, encoding: str = 'utf-8') -> None:
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File {filename} does not exist.")
    with (open(filename, 'r', encoding=encoding) as finput,
          open(outputfile, 'w', encoding=encoding) as foutput
          ):
        for line in finput:
            line = [chr(int(i)) for i in line.strip().split(',')]
            foutput.write(''.join(line))

file_decode("wcfile_encoded.txt", "wcfile_decoded.txt")

def file_encode_c(
    filename: str | Path,
    outputfile: str | Path,
    encoding: str = 'utf-8',
) -> None:
    """Encode a text file by writing each character's ordinal value.

    Each line is written as comma-separated integers, with the
    newline character excluded from encoding.

    Args:
        filename: Path to the input text file.
        outputfile: Path to the output encoded file.
        encoding: File encoding to use (default: utf-8).

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File {filename} does not exist.")

    with (
        open(p, 'r', encoding=encoding) as finput,
        open(outputfile, 'w', encoding=encoding) as foutput,
    ):
        for line in finput:
            ordinals = [ord(c) for c in line.rstrip('\n')]
            foutput.write(','.join(str(i) for i in ordinals) + '\n')


def file_decode_c(
    filename: str | Path,
    outputfile: str | Path,
    encoding: str = 'utf-8',
) -> None:
    """Decode a file produced by file_encode back to plain text.

    Args:
        filename: Path to the encoded file.
        outputfile: Path to the output decoded text file.
        encoding: File encoding to use (default: utf-8).

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If a line contains non-integer values.
    """
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File {filename} does not exist.")

    with (
        open(p, 'r', encoding=encoding) as finput,
        open(outputfile, 'w', encoding=encoding) as foutput,
    ):
        for lineno, line in enumerate(finput, start=1):
            try:
                chars = [chr(int(i)) for i in line.strip().split(',')]
            except ValueError as e:
                raise ValueError(f"Malformed data on line {lineno}: {e}") from e
            foutput.write(''.join(chars) + '\n')


def encrypt(filename, text):
    with open(filename, 'w') as outfile:
        for one_character in text:
            outfile.write(f'{ord(one_character)}\n')


def decrypt(filename):
    characters = [chr(int(one_character))
                  for one_character in open(filename)
                  if one_character.strip().isdigit()]
    return ''.join(characters)
