from pathlib import Path

def count_my_words_o(filename: str | Path) -> str:

    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')

    user_words = input("Enter the words to count (separated by spaces): ").split()
    word_counts = { w : 0 for w in user_words }
    if not word_counts:
        return "No words to count."
        quit()

    with open(p) as f:
        for line in f:
            for w in line.split():
                if w in word_counts:
                    word_counts[w] += 1
        return (f"[{p}]\n" +
                "\n".join(f"{w}: {c}" for w, c in word_counts.items()))

# print(count_my_words_o("wcfile.txt"))
# print(count_my_words_o("article001.txt"))

def count_my_words() -> str:
    userinput = input("Enter a filename and the words to count (separated by spaces): ")
    if not userinput:
        return None

    filename, *user_words = userinput.split()

    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')

    word_counts = { w : 0 for w in user_words }
    if not word_counts:
        return "No words to count."

    with open(p) as f:
        for line in f:
            for t in line.split():
                w = t.strip('.,!?";:')
                if w in word_counts:
                    word_counts[w] += 1
        return (f"[{p}]\n" +
                "\n".join(f"{w}: {c}" for w, c in word_counts.items()))

print(count_my_words())
print(count_my_words())

def count_words_in_file() -> dict[str, int] | str:
    """Claude"""
    parts = input("Enter a filename and words to count (space-separated): ").split()

    if not parts:
        return "No input provided."

    filename, *words = parts

    if not words:
        return "No words to count."

    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    counts = dict.fromkeys((w.lower() for w in words), 0)

    with open(p) as f:
        for line in f:
            for token in line.split():
                token = token.strip('.,!?";:').lower()
                if token in counts:
                    counts[token] += 1

    return counts

# print(count_words_in_file())

def count_certain_words():
    s = input("Enter a filename, and then words you want to track: ").strip()

    if not s:
        return None

    filename, *words = s.split()

    counts = dict.fromkeys(words, 0)

    for one_line in open(filename):
        for one_word in one_line.split(): #split() was missing
            if one_word in counts:
                counts[one_word] += 1

    return counts

# print(count_certain_words())
# print(count_certain_words())