from collections import Counter
from pathlib import Path


def summarize_codes0(filename: str | Path) -> dict:
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')
    code_counts = {}
    with open(filename) as f:
        for line in f:
            code = line.strip().split()[8]
            code_counts[code] = code_counts.get(code, 0) + 1
    return sorted(code_counts.items(), key=lambda x: x[1], reverse=True)


print(summarize_codes0("../mini-access-log.txt"))


def summarize_codes(filename: str | Path) -> dict:
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')
    with open(filename) as f:
        code_counts = Counter(line.strip().split()[8] for line in f)
    return code_counts


print(summarize_codes("../mini-access-log.txt"))

def summarize_codes_c(filename: str | Path) -> Counter:
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')
    with open(p) as f:
        return Counter(
            parts[8]
            for line in f
            if len(parts := line.strip().split()) > 8
        )

print(summarize_codes_c("../mini-access-log.txt"))

def response_counts(filename):
    output = Counter()

    for one_line in open(filename):
        output[one_line.split()[8]] += 1

    return output


print(response_counts("../mini-access-log.txt"))
