"""
This module provides a Spanish syllabifier that breaks Spanish words into syllables
using regular expressions based on Spanish phonological rules.
"""
import re


def es_syllabify(data):
    """
    Syllabifies Spanish words using a regex-based approach.

    Accepts a single word, a list of words, or a dictionary (uses keys as words).
    Returns a dictionary mapping each word to its list of syllables.

    Args:
        data (str | list | dict): A single word (str), a list of words,
                                  or a dictionary whose keys are words.

    Returns:
        dict: A dictionary of the form {word: [syllable1, syllable2, ...]}.

    Raises:
        TypeError: If input is not a str, list, or dict.

    Examples:
        >>> es_syllabify("trabajo")
        {'trabajo': ['tra', 'ba', 'jo']}
        >>> es_syllabify(["casa", "perro"])
        {'casa': ['ca', 'sa'], 'perro': ['pe', 'rro']}
    """

    # --- Syllable regex pattern ---
    # Matches one syllable at a time using Spanish phonological structure:
    # Onset + Nucleus (vowel/diphthong/triphthong) + optional Coda
    syllable = re.compile(
        # ONSET: the consonant(s) that begin a syllable
        # To do:
        # ^sh-, -sh-
        # Loans: lobby, byte
        # prefixes: pneumo[noul]tramicroscopicosilicovolcanoconiosis
        r'(:?[bcdfghjklmnñpqrstvwxyz]{0,1}'  # single consonant (optional)
        r'|(?:[bcfglpt]l){0,1}'               # consonant + l clusters (e.g. bl, cl, fl)
        r'|(?:[bcdfglpt]r){0,1}'              # consonant + r clusters (e.g. br, cr, dr)
        r'|(?:ch){0,1}'                        # digraph ch
        r'|(?:^mn|^p[sn]|rr))'                # word-initial mn, ps, pn; or rr

        # NUCLEUS/RYME: the vowel core of the syllable
        # Includes simple vowels, diphthongs, and triphthongs
        r'(?:[aáeéiíoóuú]'        # simple vowels (stressed and unstressed)
        r'|[aá][iu]'              # diphthongs: ai, au, ái, áu
        r'|[eé][iu]'              # diphthongs: ei, eu, éi, éu
        r'|i[aáeéoóuú]'          # diphthongs starting with i
        r'|o[iu]'                 # diphthongs: oi, ou
        r'|[uü][aáeéiíoó]'       # diphthongs starting with u/ü
        r'|[iuü][aá][iu]'        # triphthongs: iai, iau, uai, uau
        r'|[iuü][eé][iu]'        # triphthongs: iei, ieu, uei, ueu
        r'|ui[aá]'               # triphthongs: uia, uía
        r'|ui[eé]'               # triphthongs: uie, uié
        r'|ui[oó]'               # triphthongs: uio, uió
        r'|uai[ae])'             # triphthongs: uaia, uaie

        # CODA: optional consonant(s) closing the syllable
        r'[bcdfgjklmnprsxyz]{0,2}$',  # up to 2 closing consonants
        re.IGNORECASE
    )

    # --- Normalize input to a list of words ---
    if isinstance(data, str):
        words = [data]          # single word → wrap in list
    elif isinstance(data, list):
        words = data            # already a list
    elif isinstance(data, dict):
        words = list(data.keys())  # use dictionary keys as words
    else:
        raise TypeError("Input must be a string, list, or dictionary")

    results = {}

    for word in words:
        w = word.lower()   # normalize to lowercase for regex matching
        sylls = []

        # Scan the word right-to-left, matching one syllable at a time
        while w:
            m = syllable.search(w)
            if not m:
                # Pending: Add error messages!
                # If no match found, treat remainder as a single syllable
                sylls.append(w)
                break
            syl = m.group()         # extract matched syllable
            w = w[:m.start()]       # trim matched portion from right of string
            sylls.append(syl)

        results[word] = sylls[::-1]  # reverse to restore left-to-right order

    return results


def show_es_syls(results):
    """
    Pretty-prints the syllabification results in a formatted table.

    Args:
        results (dict): Output from es_syllabify(), mapping words to syllable lists.

    Returns:
        None. Prints directly to stdout.

    Example output:
        Word                 | Syllables
        ----------------------------------------
         1. trabajo          | tra-ba-jo
    """
    print(f"{'Word':<20} | {'Syllables'}")
    print('-' * 40)
    for i, (word, sylls) in enumerate(results.items(), start=1):
        print(f"{i:>2}. {word:<17} | {'-'.join(sylls)}")

# Pending: Add way to deal with goldsets and json fiiles
