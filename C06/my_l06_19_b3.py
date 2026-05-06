def userdicts(filename) -> dict:
    output = {}
    try:
        with open(filename) as f:
            for line in f:
                if line.startswith(('#', '\n')):
                    continue
                username, _, uid, *ignore, homedir, shell = line.strip().split(':')
                output[username] = {
                    "uid": uid,
                    "homedir": homedir,
                    "shell": shell
                }
        return output
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}


my_result = userdicts("../passwd.txt")
print(my_result, len(my_result))


def user_info(filename):
    output = {}

    for one_line in open(filename):
        if one_line.startswith(('#', '\n')):
            continue
        username, passwd, uid, *ignore, homedir, shell = one_line.strip().split(':')

        output[username] = {'uid': uid,
                            'homedir': homedir,
                            'shell': shell}

    return output


l_result = (user_info("../passwd.txt"))
print(l_result, len(l_result))
