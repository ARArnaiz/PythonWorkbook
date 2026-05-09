def show_certain_lines(filename: str) -> list[str]:
    with open(filename) as f:
        return [line for line in f if set('AaEeIiOoUu') & set(line) and len(line) > 20]


for item in show_certain_lines("wcfile.txt"):
    print(item, end='')

VOWELS = frozenset('aeiouAEIOU')
# Claude
def lines_with_vowel_and_length(filename: str, min_length: int = 20) -> list[str]:
    """Return lines containing at least one vowel and meeting the minimum length."""
    with open(filename) as f:
        return [
            line for line in f
            if len(line) >= min_length and any(c in VOWELS for c in line)
        ]

for item in lines_with_vowel_and_length("wcfile.txt"):
    print(item, end="")


def lines_with_1v20c(filename):
    return [one_line
            for one_line in open(filename)
            if len(one_line) >= 20 and
            len(set('aeiou') & set(one_line)) >= 1]


for item in lines_with_1v20c("wcfile.txt"):
    print(item, end='')
