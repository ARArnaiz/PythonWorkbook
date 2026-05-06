from collections import Counter

VOWELS = "aeiou"
ES_VOWELS = "aáeéiíoóuúü"

def v_counter(filename: str) -> Counter:
    """Count vowels in a file and return as a dictionary."""
    try:
        with open(filename) as f:
            v_dict = Counter()
            for line in f:
                v_dict.update(Counter(v for v in line.lower() if v in VOWELS))
            return v_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}

print(v_counter("../article001.txt"))

def v_counter_c(filename: str) -> Counter:
    """Claude's Count vowels in a file and return as a Counter."""
    try:
        with open(filename) as f:
            v_dict = Counter()
            for line in f:
                v_dict.update(v for v in line.lower() if v in VOWELS)
            return v_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return Counter()

print(v_counter_c("../article001.txt"))
print()

def count_vowels(filename):
    output = dict.fromkeys('aeiou', 0)

    for one_line in open(filename):
        for one_character in one_line.lower():
            if one_character in output:
                output[one_character] += 1

    return output

print(count_vowels("../article001.txt"))

def v_counter_ES(filename: str, vlist: str) -> Counter:
    """Claude's Count vowels in a file and return as a Counter."""
    try:
        with open(filename, encoding='utf8') as f:
            v_dict = Counter()
            for line in f:
                v_dict.update(v for v in line.lower() if v in vlist)
            return v_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return Counter()

print(v_counter_ES(r"C:\Users\ARA\OneDrive\Workspace\Data\Quijote_PG.txt", ES_VOWELS))