from collections import defaultdict

def shells_to_dict(filename: str) -> dict:

    shells_dict = {}
    try:
        with open(filename) as f:
            for line in f:
                if not line.startswith(("#", "\n")):
                    try:
                        username, *_, shellname = line.strip().split(":")
                        shells_dict[shellname] = shells_dict.get(shellname, []) + [username]
                    except ValueError as e:
                        raise ValueError(f"Invalid UID in line: {line.strip()!r}") from e
            return shells_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}

print(shells_to_dict("../passwd.txt"))

def shells_to_dict_c(filename: str) -> dict:

    shells_dict = {}
    try:
        with open(filename) as f:
            for line in f:
                if not line.startswith(("#", "\n")):
                    username, *_, shellname = line.strip().split(":")
                    shells_dict.setdefault(shellname, []).append(username)
            return shells_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}

print(shells_to_dict_c("../passwd.txt"))

def shells_users(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, *ignore, shell = one_line.strip().split(':')

        output[shell].append(username)

    return output

print(shells_users("../passwd.txt"))
print(shells_to_dict("../passwd.txt") == shells_users("../passwd.txt") == shells_to_dict_c("../passwd.txt"))