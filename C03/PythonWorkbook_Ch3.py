import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Chapter 3: Strings
    ### Exercise 5: Pig Latin
    """)
    return


@app.cell
def _():
    def pig_latin(word: str) -> str:
        word = word.lower()
        if word[0] in "aeiou":
            return f"{word}way"
        else:
            return f"{word[1:]}{word[0]}ay"


    print(pig_latin("air"))
    print(pig_latin("Python"))
    return (pig_latin,)


@app.cell
def _():
    # Claude's improved version
    def pig_latin1(word: str) -> str:
        if not word:
            return word
        word = word.lower()
        return f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"


    print(pig_latin1("air"))
    print(pig_latin1("Python"))
    return


@app.cell
def _(pig_latin):
    sentence = "Python is an amazing language"
    result = " ".join(pig_latin(w) for w in sentence.split())
    print(result)
    return (sentence,)


@app.cell
def _(sentence):
    result1 = " ".join(
        f"{w}way" if w[0] in "aeiou" else f"{w[1:]}{w[0]}ay"
        for w in sentence.lower().split()
    )
    print(result1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beyond the exercise
    """)
    return


@app.cell
def _():
    # Deal with Capitalization
    def pig_latin2(word: str) -> str:
        if not word:
            return word
        is_capitalized = word[0].isupper()
        word = word.lower()
        result = f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"
        return result.capitalize() if is_capitalized else result


    print(pig_latin2("air"))
    print(pig_latin2("Python"))
    return


@app.cell
def _():
    # Deal with Capitalization, Claude
    def pig_latin2a(word: str) -> str:
        if not word:
            return word
        is_capitalized = word[0].isupper()
        word = word.lower()
        result = f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"
        return result[0].upper() + result[1:] if is_capitalized else result


    print(pig_latin2a("air"))
    print(pig_latin2a("Python"))
    return


@app.cell
def _():
    # Deal with end punctuation
    def pig_latin3(word: str) -> str:
        if not word:
            return word
        is_capitalized = word[0].isupper()
        ends_in_punc = word[-1] in ",.;:'\"!|-"
        if ends_in_punc:
            word, punc = word[:-1], word[-1]
        word = word.lower()
        result = f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"
        result = result[0].upper() + result[1:] if is_capitalized else result
        return result + punc if ends_in_punc else result


    print(pig_latin3("air,"))
    print(pig_latin3("Python!"))
    return


@app.cell
def _():
    # Claude's version
    def pig_latin3a(word: str) -> str:
        if not word:
            return word
        is_capitalized = word[0].isupper()
        punc = ""
        if word[-1] in ",.;:'\"!|-":
            word, punc = word[:-1], word[-1]
        word = word.lower()
        result = f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"
        result = result[0].upper() + result[1:] if is_capitalized else result
        return result + punc


    print(pig_latin3a("air,"))
    print(pig_latin3a("Python!"))
    return


@app.cell
def _():
    # Alternative Pig Latin
    def alt_pig_latin(word: str) -> str:
        vowels = set("aeiou")
        if not word:
            return word
        is_capitalized = word[0].isupper()
        punc = ""
        if word[-1] in ",.;:'\"!|-":
            word, punc = word[:-1], word[-1]
        word = word.lower()
        result = (
            f"{word}way"
            if len(set(word) & vowels) > 1
            else f"{word[1:]}{word[0]}ay"
        )
        result = result[0].upper() + result[1:] if is_capitalized else result
        return result + punc


    print(alt_pig_latin("air"))
    print(alt_pig_latin("Python"))
    print(alt_pig_latin("air,"))
    print(alt_pig_latin("Python!"))
    print(alt_pig_latin("wine"))
    print(alt_pig_latin("wind"))
    print(alt_pig_latin("aardvark"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 6: Pig Latin sentence
    """)
    return


@app.cell
def _():
    def pl_w(word: str) -> str:
        if not word:
            return word
        is_capitalized = word[0].isupper()
        punc = ""
        if word[-1] in ",.;:'\"!|-?":
            word, punc = word[:-1], word[-1]
        word = word.lower()
        result = f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"
        result = result[0].upper() + result[1:] if is_capitalized else result
        return result + punc


    print(pl_w("air,"))
    print(pl_w("Python!"))


    def pl_s(sentence: str) -> str:
        result = " ".join(pl_w(w) for w in sentence.split())
        return result


    sentence = "Python is an amazing language"
    print(pl_s(sentence))
    example = "this is a test translation"
    print(pl_s(example))
    example2 = "Hello, cruel and solitary world! Are you, moon, the same?"
    print(pl_s(example2))
    assert pl_s(example) == "histay isway away esttay ranslationtay"
    return (sentence,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beyond the exercise
    """)
    return


@app.cell
def _():
    # 1st attempt
    mysentence = []
    with open("../intro.txt", "r") as f:
        for count, line in enumerate(f, 1):
            if count < 11:
                words = line.strip().split(" ")
                if words != [""] and len(words) > 3:
                    # print (words)
                    mysentence.append(words[3])
    print(" ".join(mysentence))
    return


@app.cell
def _():
    # 2nd attempt
    mysentence2 = []
    with open("../intro.txt", "r") as f2:
        firstNlines = f2.readlines()[:11]
        for line2 in firstNlines:
            wordsx = line2.strip().split(" ")
            if wordsx != [""] and len(wordsx) > 3:
                mysentence2.append(wordsx[3])
    print(" ".join(mysentence2))
    return


@app.cell
def _():
    # Claude's improvements
    from itertools import islice

    mysentence3 = []
    with open("../intro.txt", "r") as f3:
        for line3 in islice(f3, 11):
            wordsxx = line3.strip().split()
            if len(wordsxx) > 3:
                mysentence3.append(wordsxx[3])
    print(" ".join(mysentence3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function that transposes a list of strings, in which each string contains multiple words separated by whitespace.

    Input: ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

    Output: ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']
    """)
    return


@app.cell
def _():
    # 1st version
    lst = ["abc def ghi", "jkl mno pqr", "stu vwx yz"]


    def ordered_shuffle(lst: list) -> list:
        res = []
        res2 = []
        for sent_idx, sentence in enumerate(lst):
            for wrd_idx, word in enumerate(sentence.split()):
                if sent_idx == 0:
                    res.append([word])
                else:
                    res[wrd_idx].append(word)
        for _ in res:
            res2.append(" ".join(_))
        return res2


    print(ordered_shuffle(lst))
    return (lst,)


@app.cell
def _(lst):
    # Claude's version
    lst2 = ["abc def ghi", "jkl mno pqr", "stu vwx yz"]


    def ordered_shuffle_c(lst: list) -> list:
        return [" ".join(list(col)) for col in zip(*[s.split() for s in lst2])]


    print(ordered_shuffle_c(lst))
    return


@app.cell
def _():
    with open("../mini-access-log.txt", "r") as l:
        for line in l:
            if " 404 " in line:
                print(line.split()[0])

    with open("../mini-access-log.txt", "r") as l:
        fzf = [line.split()[0] for line in l if " 404 " in line]
        print("\n".join(fzf))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Exercise 7: Ubbi Dubbi
    """)
    return


@app.cell
def _():
    # In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am). In theory, you only put an ub before every vowel sound, rather than before each vowel. Given that this is a book about Python and not linguistics, I hope that you’ll forgive this slight difference in definition.


    def ubbi_dubbi(word: str) -> str:
        ud_word = []
        for c in word:
            if c.lower() in "aeiou":
                ud_word.append("ub" + c)
            else:
                ud_word.append(c)
        return "".join(ud_word)


    print(f"milk → {ubbi_dubbi('milk')}")
    print(f"hello → {ubbi_dubbi('hello')}")
    print(f"python → {ubbi_dubbi('python')}")
    print(f"air → {ubbi_dubbi('air')}")
    print(f"aarvark → {ubbi_dubbi('aarvark')}")
    return


@app.cell
def _():
    # Claude's


    def ubbi_dubbi_c(word: str) -> str:
        return "".join(f"ub{c}" if c in "aeiou" else c for c in word)


    print(f"milk → {ubbi_dubbi_c('milk')}")
    print(f"hello → {ubbi_dubbi_c('hello')}")
    print(f"python → {ubbi_dubbi_c('python')}")
    print(f"air → {ubbi_dubbi_c('air')}")
    print(f"aarvark → {ubbi_dubbi_c('aarvark')}")
    return (ubbi_dubbi_c,)


@app.cell
def _(ubbi_dubbi_c):
    # Mine w/comprehension


    def ubbi_dubbi_cc(word: str) -> str:
        return "".join("ub" + c if c.lower() in "aeiou" else c for c in word)


    print(f"milk → {ubbi_dubbi_cc('milk')}")
    print(f"hello → {ubbi_dubbi_cc('hello')}")
    print(f"python → {ubbi_dubbi_c('python')}")
    print(f"air → {ubbi_dubbi_cc('air')}")
    print(f"aarvark → {ubbi_dubbi_cc('aarvark')}")
    return


@app.cell
def trans():
    def transform_word(word: str, transform_fn) -> str:
        """Apply any core transformation, preserving hyphens, punctuation, and case."""
        # Hyphen tokenization — recurse on each part
        if "-" in word:
            return "-".join(
                transform_word(part, transform_fn) for part in word.split("-")
            )
        if not word:
            return word
        # Strip trailing punctuation
        punc = ""
        if word[-1] in ",.;:'\"!|-":
            word, punc = word[:-1], word[-1]
        # Save original for case restoration
        original = word
        # Normalize and transform
        result = transform_fn(word.lower())
        # Restore case and reattach punctuation
        return restore_case(original, result) + punc


    def detect_case(word: str) -> str:
        """Return the case pattern of a word: 'upper', 'lower', 'inicap', or 'mixed'."""
        # if not word:
        #     raise ValueError("Empty string")
        if word.isupper():
            return "upper"
        if word.islower():
            return "lower"
        if word[0].isupper() and word[1:].islower():
            return "inicap"
        return "mixed"


    def restore_case(original: str, result: str) -> str:
        """Apply the case pattern of *original* to *result*."""
        pattern = detect_case(original)
        if pattern == "lower":
            return result
        if pattern == "upper":
            return result.upper()
        if pattern == "inicap":
            return result.capitalize()
        return apply_case_profile(original, result)  # mixed


    def apply_case_profile(original: str, result: str) -> str:
        """Reproduce the per-character case profile of *original* onto *result*.

        Characters in *result* beyond the length of *original* are left lowercase.
        """
        case_profile = [c.isupper() for c in original]
        return "".join(
            c.upper() if i < len(case_profile) and case_profile[i] else c
            for i, c in enumerate(result)
        )


    def pl(word: str) -> str:
        """Pig Latin: vowel-initial words get '-way' suffix; others move the first consonant to the end and add '-ay'."""
        return f"{word}way" if word[0] in "aeiou" else f"{word[1:]}{word[0]}ay"


    def ub(word: str) -> str:
        """ "Ubbi Dubbi: insert 'ub' before each vowel."""
        return "".join("ub" + c if c.lower() in "aeiou" else c for c in word)


    print(f"milk → {transform_word('milk', pl)} | {transform_word('milk', ub)}")
    print(f"hello → {transform_word('hello', pl)} | {transform_word('hello', ub)}")
    print(
        f"Python → {transform_word('Python', pl)} | {transform_word('Python', ub)}"
    )
    print(f"air → {transform_word('air', pl)} | {transform_word('air', ub)}")
    print(
        f"aarvark → {transform_word('aarvark', pl)} |{transform_word('aarvark', ub)}"
    )
    print(
        f"pre-Chomskian → {transform_word('pre-Chomskian', pl)} | {transform_word('pre-Chomskian', ub)}"
    )
    print(
        f"post-Aristotelian → {transform_word('post-Aristotelian', pl)} | {transform_word('post-Aristotelian', ub)}"
    )
    print(
        f"Post-Agustinian → {transform_word('Post-Augustinian', pl)} | {transform_word('Post-Agustinian', ub)}"
    )
    print(
        f"Post-Agustinian! → {transform_word('Post-Agustinian', pl)} | {transform_word('Post-Agustinian!', ub)}"
    )
    print(f"[empty] → {transform_word('', pl)} | {transform_word('', ub)}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Beyond the exercise
    """)
    return


@app.cell
def _():
    # with open("article001.txt", "r") as infile:
    #     text = infile.readlines()

    # names_to_redact = ["Chomsky", "Collins", "Jackendoff", "Johns","Johnson", "Lappin", "Levine", "Shalom", "Pollard", "Uriagareka", "Yang"]
    # robustlist = []

    # for n in names_to_redact:
    #     robustlist.append(n)
    #     robustlist.append(n.lower())
    #     robustlist.append(n.upper())

    # redacted = []
    # for line in text:
    #     for name in robustlist:
    #         line = line.replace(name, "_" * len(name))
    #     redacted.append(line)

    # with open("article001_redacted.txt", "w") as outfile:
    #     outfile.writelines(redacted)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    [Is there a better way to make the replacement case insensitive?]

    Yes — `re.sub` with `re.IGNORECASE` is the right tool here. Your `robustlist` approach also misses mixed case like `"cHoMsKy"`, and it scales poorly.

    ```python
    import re

    with open("article001.txt", "r") as infile:
        text = infile.readlines()

    names_to_redact = ["Chomsky", "Collins", "Jackendoff", "Johns", "Johnson",
                       "Lappin", "Levine", "Shalom", "Pollard", "Uriagareka", "Yang"]

    pattern = re.compile("|".join(re.escape(n) for n in names_to_redact), re.IGNORECASE)

    redacted = []
    for line in text:
        redacted.append(pattern.sub(lambda m: "_" * len(m.group()), line))

    with open("article001_redacted.txt", "w") as outfile:
        outfile.writelines(redacted)
    ```

    Key points:

    - **`re.escape`** handles any names that happen to contain regex special characters.
    - **Single compiled pattern** with `|` — one pass per line instead of N passes.
    - **`lambda m: "_" * len(m.group())`** preserves the matched length, so `"CHOMSKY"` (7 chars) becomes `"_______"` rather than the length of the canonical form in your list.
    - Worth noting: `Johns` will match inside `Johnson` depending on alternation order — regex tries alternatives left to right and stops at first match, so put longer names first, or better yet use word boundaries (`\b`) if you don't want partial matches.

    [Not clear why you need the lambda since the size is never going to change because of capitalization.]

    You're right. `len(m.group())` and `len(name)` are always equal since case variants have the same length. Just use the name's length directly:

    ```python
    pattern.sub(lambda m: "_" * len(m.group()), line)
    ```

    But then you still need the lambda because `sub` requires a callable or a plain replacement string — you can't pass a dynamic value without one. The simplest form if you want a fixed replacement string would require knowing the length upfront, which you don't since the pattern covers multiple names of different lengths.

    So the lambda stays, but your instinct is right that `len(m.group())` vs `len(name)` is the same value — it's just the cleanest way to get the length inside the callback without looking up which name matched.
    """)
    return


@app.cell
def _():
    import re

    with open("../article001.txt", "r") as infile:
        text = infile.readlines()

    names_to_redact = [
        "Chomsky",
        "Collins",
        "Jackendoff",
        "Johnson",
        "Lappin",
        "Levine",
        "Shalom",
        "Pollard",
        "Uriagareka",
        "Yang",
    ]

    pattern = re.compile(
        "|".join(re.escape(n) for n in names_to_redact), re.IGNORECASE
    )

    redacted = []
    for line in text:
        redacted.append(pattern.sub(lambda m: "_" * len(m.group()), line))

    with open("article001_redacted.txt", "w") as outfile:
        outfile.writelines(redacted)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    URL-encode characters —In URLs, we often replace special and nonprintable characters with a % followed by the character’s ASCII value in hexadecimal. For example, if a URL includes a space character (ASCII 32, aka 0x20), we replace it with %20. Given a string, URL-encode any character that isn’t a letter or number. For the purposes of this exercise, we’ll assume that all characters are in ASCII (i.e., 1 byte long) and not multibyte UTF-8 characters. It might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng.bz/nPxg) functions.
    """)
    return


@app.cell
def _():
    from string import ascii_letters, digits

    example, solution = "hello world", "hello%20world"
    a, b = "it's a test", "it%27s%20a%20test"


    def toURL(url: str) -> str:
        myurl = ""
        for char in url:
            if char not in ascii_letters + digits:
                myurl += "".join(f"%{ord(char):02x}")
            else:
                myurl += "".join(char)
        return myurl


    def fromURL(url: str) -> str:
        myurl = ""
        i = 0
        while i < len(url):
            if url[i] == "%" and i + 2 < len(url):
                myurl += chr(int(url[i + 1 : i + 3], 16))
                i += 3
            else:
                myurl += url[i]
                i += 1
        return myurl


    print(f"I: {example} - O: {toURL(example)}")
    print(f"I: {a} - O: {toURL(a)}")
    print(f"I: {solution} - O: {fromURL(solution)}")
    print(f"I: {b} - O: {fromURL(b)}")
    return fromURL, toURL


@app.cell
def _(fromURL, toURL):
    exs = []
    ix = '"'
    with open("url_pairs.txt", "r", encoding="utf8") as inf:
        text = inf.readlines()
    for line in text:
        line = line.strip()
        if line.startswith('"') and line.endswith('"'):
            (decoded, encoded) = line.split(" → ")
            exs.append(
                {"decoded" : decoded.removeprefix(ix).removesuffix(ix), 
                 "encoded" : encoded.removeprefix(ix).removesuffix(ix)}
            )

    for i,d in enumerate(exs, 1):
        print(f'[{i}]')
        print(f'I: {d['decoded']} - O: {toURL(d['decoded'])}')
        print(f'I: {d['encoded']} - O: {fromURL(d['encoded'])}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###Exercise 8: Sorting a string
    """)
    return


@app.cell
def _():
    string = 'ALFREDO'
    string2 = 'ARNAIZ'

    def strsort(astring: str) -> str:
        """Sort a string"""
        return "".join(sorted(astring))

    print(strsort(string))
    print(strsort(string2))
    return


@app.cell
def _():
    anotherstr = 'Tom Dick Harry'

    def snpcs(astring: str) -> str:
        """Sort string and print it comma-separated"""
        slst = astring.split()
        #return print(*sorted(slst), sep=",")
        return ",".join(sorted(slst))

    print(snpcs(anotherstr))
    return


@app.cell
def _():
    #Which is the last word, alphabetically, in a text file?
    #Which is the longest word in a text file?

    wordset = set()
    with open("../intro.txt", "r") as ff:
        for line in ff:
            line = line.strip()
            for w in line.split():
                wordset.add(w)

    print(f'Word set: {wordset}')
    sortedset = sorted(list(wordset))
    print(f'Sorted: {sortedset}')
    lenset = (sorted(list(wordset), key=len))
    print(f'Sorted by length: {lenset}')
    lensetr = (sorted(list(wordset), reverse=True, key=len))
    print(f'Reverse sorted by length: {lensetr}')

    print(f'Last token in sorted set: {sortedset[-1]}')
    print(f'Longest token in sorted set: {lenset[-1]}')
    print(f'Longest token in reverse sorted set: {lensetr[0]}')
            
    return


if __name__ == "__main__":
    app.run()
