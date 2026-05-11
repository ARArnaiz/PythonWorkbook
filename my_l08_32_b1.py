from collections import Counter

string = "this is an easy test"
string2 = "aeiou AEIOU AAEEIIIOOUU AAAAAAAAAAAAAA AaAsAAaa"


def dict_word_V_count(string) -> dict:
    return {word: sum(Counter(char.lower()
                              for char in word
                              if char.lower() in "aeiou").values())
            for word in string.split()}


print(dict_word_V_count(string))
print(dict_word_V_count(string2))

VOWELS = frozenset("aeiouAEIOU")  # frozenset: O(1) lookup, avoids repeated .lower()


def word_vowels_c(s: str) -> dict[str, int]:
    return {
        word: sum(1 for c in word if c in VOWELS)
        for word in s.split()
    }


print(word_vowels_c(string))
print(word_vowels_c(string2))


def vowel_count(word):
    total = 0
    for one_letter in word.lower():
        if one_letter in 'aeiou':
            total += 1
    return total


def word_vowels(s):
    return {one_word: vowel_count(one_word)
            for one_word in s.split()}


print(word_vowels(string))
print(word_vowels(string2))
