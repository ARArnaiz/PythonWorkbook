
def gather_shells(filename) -> set[str]:

    with open(filename) as f:
        return { line.split(':')[-1].strip()
                 for line in f
                 if not line.startswith(('\n', '#')) }

print(gather_shells("../passwd.txt"))

def gather_shells_c(filename):
    with open(filename) as f:
        return {
            line.split(':')[-1].strip()   # split first, strip only last field
            for line in f
            if line.strip() and not line.lstrip().startswith('#')
            # line.strip() as the blank-line guard — catches \r\n, pure-whitespace
            # lines, not just \n
            # line.lstrip().startswith('#') — catches indented comments if needed
        }

print(gather_shells_c("../passwd.txt"))

def different_shells(filename):
    return {one_line.split(':')[-1].strip()
            for one_line in open(filename)
            if not one_line.startswith(('\n', '#'))}

print(different_shells("../passwd.txt"))