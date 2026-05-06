from pathlib import Path
import string


def file_to_vs_cs(inputfile: str | Path,
                  vowels_file: str | Path,
                  consonants_file: str | Path,
                  encoding: str = 'utf-8') -> None:
    '''Reads an input file and writes the vowels to outputfileVs and consonants to outputfileCs preserves
    the original number of lines.

    :param inputfile: Path to the input file.
    :param vowels_file: Path to the output file for vowels.
    :param consonanats_file: Path to the output file for consonants.
    :param encoding: Encoding of the input and output files (default is 'utf-8').

    :raises FileNotFoundError: If the input file does not exist.'''

    p = Path(inputfile)
    if not p.exists():
        raise FileNotFoundError(f"Input file '{p}' does not exist")
    with (
        open(inputfile, 'r', encoding=encoding) as finput,
        open(vowels_file, 'w', encoding=encoding) as foutputVs,
        open(consonants_file, 'w', encoding=encoding) as foutputCs
    ):
        for line in finput:
            foutputVs.write(''.join([c for c in line if c.lower() in 'aeiou\n']))
            foutputCs.write(''.join([c for c in line if c.lower() in 'bcdfghjklmnpqrstvwxyz\n']))

file_to_vs_cs("../wcfile.txt", "wcfile_vs.txt", "wcfile_cs.txt")

VOWELS = frozenset('aeiou')
CONSONANTS = frozenset(string.ascii_lowercase) - VOWELS

def vowels_and_consonants(
    infilename: str | Path,
    vowel_filename: str | Path,
    consonant_filename: str | Path,
    encoding: str = 'utf-8',
) -> None:
    """Read a text file and split its letters into two output files.

    Each output file has the same number of lines as the input.
    Punctuation, digits, and whitespace (other than newlines) are ignored.

    Args:
        infilename: Path to the input text file.
        vowel_filename: Path to the output file for vowels.
        consonant_filename: Path to the output file for consonants.
        encoding: File encoding to use (default: utf-8).

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    p = Path(infilename)
    if not p.exists():
        raise FileNotFoundError(f"Input file '{p}' does not exist.")

    with (
        open(p, 'r', encoding=encoding) as infile,
        open(vowel_filename, 'w', encoding=encoding) as vowel_out,
        open(consonant_filename, 'w', encoding=encoding) as consonant_out,
    ):
        for line in infile:
            vowel_out.write(''.join(c for c in line if c.lower() in VOWELS or c == '\n'))
            consonant_out.write(''.join(c for c in line if c.lower() in CONSONANTS or c == '\n'))

file_to_vs_cs("../wcfile.txt", "wcfile_vs.txt", "wcfile_cs.txt")


def vowels_and_consonants(infilename, vowel_filename, consonant_filename):
    with open(infilename) as infile, open(vowel_filename, 'w') as vowel_out, open(consonant_filename,
                                                                                  'w') as consonant_out:
        for one_line in infile:
            for one_character in one_line:
                if one_character.lower() in 'aeiou':
                    vowel_out.write(one_character)
                elif one_character.lower() in string.ascii_lowercase:
                    consonant_out.write(one_character)


vowels_and_consonants("wcfile.txt", "wcfile_vs_l.txt", "wcfile_cs_l.txt")
