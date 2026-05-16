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

def funcfile(infile: str, outfile: str, func) -> None:
    """
    Takes three parameters as input: infile, outfile and func. infile is the name of the file to be read,
    and outfile is the name of the file to be written. func is a function that takes a string as input
    and returns a string as output.  Returns None.
    """
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        for line in fin:
            fout.write(func(line)+'\n')

funcfile("wcfile.txt", "wcfile_pl2.txt", pl_s)

def funcfile(filename, func):
    return ' '.join(func(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())