import random
import string
from typing import Callable


CHAR_SETS: dict[str, str] = {
    "upper":       string.ascii_uppercase,
    "lower":       string.ascii_lowercase,
    "digits":      string.digits,
    "punctuation": string.punctuation,
    "alpha":       string.ascii_letters,
    "alnum":       string.ascii_letters + string.digits,
}

def create_password_generator(characters: str | None = None,
                               key: str | None = None,
                               **min_counts: int) -> Callable[[int], str]:
    """Return a password generator closed over the resolved character set and minimum requirements."""
    if key is not None:
        if key not in CHAR_SETS:
            raise KeyError(f"Unknown key '{key}'. Choose from: {list(CHAR_SETS)}")
        characters = CHAR_SETS[key]
    if not characters:
        # default filler to the union of all guaranteed sets
        characters = ''.join(CHAR_SETS[k] for k in min_counts)
    for k in min_counts:
        if k not in CHAR_SETS:
            raise KeyError(f"Unknown key '{k}'. Choose from: {list(CHAR_SETS)}")

    def generate_password(length: int) -> str:
        # 1. Satisfy minimums first
        guaranteed = []
        for k, minimum in min_counts.items():
            guaranteed.extend(random.choices(CHAR_SETS[k], k=minimum))

        if len(guaranteed) > length:
            raise ValueError(f"Length {length} too short to satisfy minimums ({len(guaranteed)} required).")

        # 2. Fill the rest from the general character set
        remaining = length - len(guaranteed)
        filler = random.choices(characters, k=remaining)

        # 3. Shuffle so guaranteed chars aren't always at the front
        pool = guaranteed + filler
        random.shuffle(pool)
        return ''.join(pool)

    return generate_password

gen = create_password_generator(key="alnum", upper=2, lower=2, digits=2, punctuation=1)
print(gen(10))   # guaranteed 2 upper, 2 lower, 2 digits, 1 punctuation, rest random alnum

def create_password_checker(**min_counts: int) -> Callable[[str], bool]:
    """Return a password checker closed over the minimum character-type requirements.

    Keyword arguments are CHAR_SETS keys mapped to minimum counts, e.g.:
        create_password_checker(upper=1, digits=2, punctuation=1)
    """
    for key in min_counts:
        if key not in CHAR_SETS:
            raise KeyError(f"Unknown key '{key}'. Choose from: {list(CHAR_SETS)}")

    def check_password(password: str) -> bool:
        return all(
            sum(c in CHAR_SETS[key] for c in password) >= minimum
            for key, minimum in min_counts.items()
        )

    return check_password

is_valid = create_password_checker(upper=1, lower=5, digits=2, punctuation=1)

print(is_valid("Hello!99"))   # True
print(is_valid("hello!99"))   # False — no uppercase
gen = create_password_generator(key="alnum", upper=1, lower=5, digits=2, punctuation=1)
new_password = gen(10)
print(new_password)
print(is_valid(new_password))   # True — generated to meet the same requirements

def create_password_checker_l(min_uppercase, min_lowercase, min_punctuation, min_digits):
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    punctuation_set = set(string.punctuation)
    digits_set = set(string.digits)

    def check_password(password):

        if len([one_character
                for one_character in password
                if one_character in uppercase_set]) < min_uppercase:
            print(f'Not enough uppercase letters; min is {min_uppercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in lowercase_set]) < min_lowercase:
            print(f'Not enough lowercase letters; min is {min_lowercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in punctuation_set]) < min_punctuation:
            print(f'Not enough punctuation; min is {min_punctuation}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in digits_set]) < min_digits:
            print(f'Not enough digits; min is {min_digits}')
            return False
        else:
            return True
    return check_password

check_validity = create_password_checker_l(1, 5, 1, 2)
print(check_validity("HGertYr(22"))
print(check_validity("HGertYr(22xx"))