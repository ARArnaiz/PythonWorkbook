import json


def psswrd_to_json_dict(filename: str) -> dict:
    output = []
    keys = ['username', 'password', 'uid', 'gid', 'unknown1', 'unknown2', 'unknown3', 'name', 'homedir', 'shell']
    with open(filename) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            output.append(dict(zip(keys, line.split(":"))))
    return json.dumps(output, indent=2)


print(psswrd_to_json_dict('../passwd.txt'))

# 3. 🔑 Keys list contains placeholder names
# 'unknown1', 'unknown2', 'unknown3' suggest the actual field names for a /etc/passwd-like file are not known.
# The standard /etc/passwd format has only 7 fields: username, password, uid, gid, gecos (or name), homedir, shell
# — so 10 keys will cause misalignment for standard files.

def passwd_to_json_c(filename: str) -> str:
    keys = ['username', 'password', 'uid', 'gid', 'name', 'homedir', 'shell']
    output = []
    try:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                output.append(dict(zip(keys, line.strip().split(':'))))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return '[]'
    return json.dumps(output, indent=2)

print(passwd_to_json_c('../passwd.txt'))

def json_passwd_dict(filename):
    fields = ['username', 'password', 'uid', 'gid', 'name', 'homedir', 'shell']

    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(dict(zip(fields, one_line.split(':'))))

    return json.dumps(output, indent=2)

print(json_passwd_dict('../passwd.txt'))
