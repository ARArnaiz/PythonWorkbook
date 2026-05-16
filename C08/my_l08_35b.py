import string

def gematria_dict() -> dict[str,int]:
    return { char: num for num, char in enumerate(string.ascii_lowercase, 1) }

GEMATRIA_DICT = gematria_dict()

def gematria_for(word: str) -> int:
    g_dict = GEMATRIA_DICT
    return sum(g_dict.get(char, 0) for char in word)

def gematria_equal_words(word: str, dictname:str) -> list[str]:
    en_dict = set()
    with open(dictname) as f:
        en_dict = {line.strip() for line in f}
    word = gematria_for(word)
    return [w for w in en_dict if gematria_for(w) == word]

ex1 = gematria_equal_words("cat", "en_words.txt")
print(len(ex1))
print(ex1)

def gematria_for_c(word: str) -> int:
    return sum(GEMATRIA_DICT.get(char, 0) for char in word)
    # no .lower() — uppercase chars score 0 by design

def gematria_equal_words_c(word: str, dictname: str) -> list[str]:
    target = gematria_for_c(word)
    with open(dictname) as f:
        return [
            line.strip()
            for line in f
            if gematria_for_c(line.strip()) == target
        ]

ex3 = gematria_equal_words_c("cat", "en_words.txt")
print(len(ex3))
print(ex3)

def gematria_dict_l():
    return {char: index
            for index, char
                in enumerate(string.ascii_lowercase,
                             1)}

GEMATRIA = gematria_dict_l()

def gematria_for_l(word):
    return sum(GEMATRIA.get(one_char, 0)
                for one_char in word)


def gematria_equal_words_l(input_word):
    our_score = gematria_for_l(input_word.lower())
    return [one_word.strip()
            for one_word in
                open('../en_words.txt')
            if gematria_for_l(one_word.lower()) ==
                our_score]

ex2 = gematria_equal_words_l("cat")
print(len(ex2))
print(ex2)