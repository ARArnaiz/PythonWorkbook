from collections import Counter

def char_types(string: str) -> dict[str, int]:
    """Return a dictionary with character types and their counts for each character in the string.
    Claude: Counter is the wrong tool here. It's designed for when you need per-character frequencies
     (e.g., {'H': 1, 'e': 1, ...}). You immediately throw that away.
     The equivalent — and simpler — expression is a generator sum:"""
    char_counts: dict[str, int] = {}

    #digits = sum(Counter(char for char in string if char.isdigit()).values())
    digits = sum(1 for char in string if char.isdigit())
    #alphas = sum(Counter(char for char in string if char.isalpha()).values())
    alphas = sum(1 for char in string if char.isalpha())
    #spaces = sum(Counter(char for char in string if char.isspace()).values())
    spaces = sum(1 for char in string if char.isspace())
    char_counts = {"isdigit": digits, "isalpha": alphas, "isspace": spaces}
    return char_counts

print(char_types("Hello, world!"))
print(char_types("123 456"))
print(char_types("   "))

def char_types_c(s: str) -> dict[str, int]:
    """Count digits, letters, and spaces in s using method-name dispatch."""
    counts: dict[str, int] = {"isdigit": 0, "isalpha": 0, "isspace": 0}

    for char in s:
        for method_name in counts:
            if getattr(char, method_name)():
                counts[method_name] += 1

    return counts

print(char_types_c("Hello, world!"))
print(char_types_c("123 456"))
print(char_types_c("   "))

def char_types_c2(s: str) -> dict[str, int]:
    methods = ["isdigit", "isalpha", "isspace"]
    return {m: sum(getattr(c, m)() for c in s) for m in methods}

print(char_types_c2("Hello, world!"))
print(char_types_c2("123 456"))
print(char_types_c2("   "))

def analyze_string(s):
    output = {'isdigit': 0,
              'isalpha': 0,
              'isspace': 0}

    for one_character in s:
        for methodname in output:
            if getattr(one_character, methodname)():  # a sneaky, cool trick!
                output[methodname] += 1

    return output

print(analyze_string("Hello, world!"))
print(analyze_string("123 456"))
print(analyze_string("   "))