import random
import string
from typing import Callable

# Version 1 (create_password_generator) accepts a named key ("upper", "lower", etc.)
# and maps it to a character set via an internal dict. The redundancy is the main
# issue: that dict is rebuilt on every call to generate_password,
# not just once per factory call. The list comprehension [x for x in sdict[key]]
# is also pointless — random.choice already works on strings directly.

def create_password_generator(key:str) -> callable:
    """Return a function that generates a random password from the given string."""
    def generate_password(length: int) -> str:
        """Generate a random password of the specified length."""
        sdict = { "upper": string.ascii_uppercase,
                  "lower": string.ascii_lowercase,
                  "digits": string.digits,
                  "punctuation": string.punctuation }
        return ''.join(random.choice([x for x in sdict[key]]) for _ in range(length))
    return generate_password

gen_password = create_password_generator("upper")
print(gen_password(10))
gen_password = create_password_generator("lower")
print(gen_password(20))
gen_password = create_password_generator("digits")
print(gen_password(15))
gen_password = create_password_generator("punctuation")
print(gen_password(10))

def create_password_generator_c(key: str) -> callable:
    CHAR_SETS = {
        "upper": string.ascii_uppercase,
        "lower": string.ascii_lowercase,
        "digits": string.digits,
        "punctuation": string.punctuation,
    }
    if key not in CHAR_SETS:
        raise KeyError(f"Unknown key '{key}'. Choose from: {list(CHAR_SETS)}")

    characters = CHAR_SETS[key]  # resolved once, closed over

    def generate_password(length: int) -> str:
        return ''.join(random.choice(characters) for _ in range(length))

    return generate_password

gen_password = create_password_generator_c("upper")
print(gen_password(10))
gen_password = create_password_generator_c("lower")
print(gen_password(20))
gen_password = create_password_generator_c("digits")
print(gen_password(15))
gen_password = create_password_generator_c ("punctuation")
print(gen_password(10))

# Claude's Best
# Two things worth noting here:
# random.choices(characters, k=length) replaces the generator loop. It's a
# single C-level call — faster and more readable.
# random.choices vs random.choice: for security-sensitive passwords, neither is appropriate —
# use secrets.choice instead. random is fine for exercises or non-sensitive use, but worth knowing.

CHAR_SETS: dict[str, str] = {
    "upper":       string.ascii_uppercase,
    "lower":       string.ascii_lowercase,
    "digits":      string.digits,
    "punctuation": string.punctuation,
    "alpha":       string.ascii_letters,
    "alnum":       string.ascii_letters + string.digits,
}

def create_password_generator_Cbest(characters: str | None = None,
                               key: str | None = None) -> Callable[[int], str]:
    """Return a password generator closed over the resolved character set.

    Provide either `characters` (a raw string) or `key` (a preset name).
    """
    if key is not None:
        if key not in CHAR_SETS:
            raise KeyError(f"Unknown key '{key}'. Choose from: {list(CHAR_SETS)}")
        characters = CHAR_SETS[key]
    if not characters:
        raise ValueError("Character set cannot be empty.")

    def generate_password(length: int) -> str:
        """Generate a random password of `length` characters."""
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        return ''.join(random.choices(characters, k=length))

    return generate_password

upper_gen  = create_password_generator_Cbest(key="upper")
custom_gen = create_password_generator_Cbest(characters="abc123!@#")

print(upper_gen(10))
print(custom_gen(8))

# Version 2 (create_password_generator_l) accepts the character string directly,
# which is simpler and more flexible (you're not locked into preset keys).
# The for loop with .append() is idiomatic but verbose compared to a
# generator expression.

def create_password_generator_l(characters):
    def create_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password

alpha_password = create_password_generator_l('abcdef')
symbol_password = create_password_generator_l('!@#$%')

print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))

# Version 3 (create_password_generator_q) is the strongest of the three.
# It accepts characters directly like v2, adds input validation, uses a clean
# generator expression, and has proper docstrings. This is essentially the "corrected"
# version of v1 stripped of its unnecessary dict abstraction.

def create_password_generator_q(characters: str) -> callable:
    """Return a function that generates a random password from the given string of allowed characters."""

    if not characters:
        raise ValueError("The set of characters cannot be empty.")

    def generate_password(length: int) -> str:
        """Generate a random password of the specified length using the provided characters."""
        return ''.join(random.choice(characters) for _ in range(length))

    return generate_password


alpha_password = create_password_generator_q('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numeric_password = create_password_generator_q('0123456789')
symbolic_password = create_password_generator_q('!@#$%^&*()_+-=[]{}|;:,.<>?')

print(alpha_password(5))  # Generates a 5-character long password with alphabetic characters
print(numeric_password(10))  # Generates a 10-character long password with numeric characters
print(symbolic_password(7))  # Generates a 7-character long password with symbolic characters