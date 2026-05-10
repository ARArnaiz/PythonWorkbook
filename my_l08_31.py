
def pl_w(word: str) -> str:
    """
    Takes a string as input. It should be a single
word.  Returns a string, the input word translated into
Pig Latin.
"""
    if not word:
        return word
    if word.isdigit():
        return word
    is_capitalized = word[0].isupper()
    punc = ""
    if word[-1] in ",.;:'\"!|-?":
        word, punc = word[:-1], word[-1]
    word = word.lower()
    result = f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"
    result = result[0].upper() + result[1:] if is_capitalized else result
    return result + punc

def pl_s(sentence: str) -> str:
    """
    Takes a string as input. It should be a sentence.  Returns a string,
    the input sentence translated into Pig Latin.
    """
    result = " ".join(pl_w(w) for w in sentence.split())
    return result

def pl_file(infile: str, outfile: str) -> None:
    """
    Takes two strings as input: infile and outfile. infile is the name of the file to be read,
    and outfile is the name of the file to be written.  Returns None.
    """
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        for line in fin:
            fout.write(pl_s(line)+'\n')

pl_file("wcfile.txt", "wcfile_pl.txt")


def plword(word):
    """Takes a string as input. It should be a single
word.  Returns a string, the input word translated into
Pig Latin.
"""
    if word[0] in 'aeiou':
        return word + 'way'

    return word[1:] + word[0] + 'ay'


def plfile(filename):
    """Takes a filename as input. Returns a string
containing the file's contents, with each word
translated into Pig Latin.
"""
    return ' '.join(plword(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())

print(plfile("wcfile.txt"))