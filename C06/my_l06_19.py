
def passwd_to_dict(filename: str) -> dict:
    """Read a passwd file and return a dictionary of usernames and UIDs."""

    password_dict = {}
    try:
        with open(filename) as f:
            for line in f:
                if not line.startswith(("#", "\n")):
                    userinfo = line.split(":")
                    password_dict[userinfo[0]] = int(userinfo[2])
            return password_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}

def passwd_to_dictc(filename: str) -> dict:
    """
    Parse a Unix-style passwd file and return a mapping of usernames to UIDs.

    Reads the file line by line, skipping comment lines (starting with '#')
    and blank lines. Each valid line is split on ':' and the username (field 0)
    and UID (field 2) are extracted using iterable unpacking.

    Args:
        filename (str): Path to the passwd-formatted file to read.

    Returns:
        dict: A dictionary mapping each username (str) to its UID (int).
              Returns an empty dict if the file is not found.

    Raises:
        ValueError: Propagates if a UID field cannot be converted to an integer,
                or if a line contains fewer than 3 colon-separated fields.

    Example:
        passwd_to_dictc("passwd.txt")
        # Returns: {'root': 0, 'daemon': 1, 'nobody': 65534}
    """
    password_dict = {}
    try:
        with open(filename) as f:
            for line in f:
                # Skip comment lines and blank lines
                if not line.startswith(("#", "\n")):
                    # Unpack only username and UID (field index 2); discard the rest
                    try:
                        username, _, uid, *_ = line.split(":")
                        # Store username as key, UID converted to int as value
                        password_dict[username] = int(uid)
                    except ValueError as e:
                        raise ValueError(f"Invalid UID in line: {line.strip()!r}") from e

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    return password_dict #todo

def passwd_to_dictl(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users

print(passwd_to_dict("../passwd.txt"))
print(passwd_to_dictl("../passwd.txt"))
print(passwd_to_dictc("../passwd.txt"))