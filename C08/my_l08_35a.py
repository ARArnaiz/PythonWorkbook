import string

def gematria_dict() -> dict[str,int]:
    return { char: num for num, char in enumerate(string.ascii_lowercase, 1) }

print(gematria_dict())

import string

def gematria_dict_l():
    return {char: index
             for index, char
                in enumerate(string.ascii_lowercase,
                             1)}

print(gematria_dict_l())