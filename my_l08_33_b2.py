
def username_uid_dict(lst: list[(str,int)]) -> dict[str, int]:
    return {x[0]: x[1] for x in lst}

with open("passwd.txt") as f:
    user_lst = []
    for line in f:
        if ":" in line:
            user, _, uid, *_ = line.strip().split(":")
            user_lst.append((user, int(uid)))

print(username_uid_dict(user_lst))

def passwd_to_dict(filename: str) -> dict[str, int]:
    with open(filename) as f:
       return { parts[0]: int(parts[2]) for line in f if ":" in line
                for parts in (line.strip().split(":"),) }

print(passwd_to_dict("passwd.txt"))

def passwd_to_dict_c(filename: str) -> dict[str, int]:
    def parse(line):
        user, _, uid, *_ = line.strip().split(":")
        return user, int(uid)
    with open(filename) as f:
        return dict(parse(line) for line in f if ":" in line)

print(passwd_to_dict_c("passwd.txt"))