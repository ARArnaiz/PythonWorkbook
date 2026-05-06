from pathlib import Path
from collections import defaultdict

def shell_users(filename: str | Path, outfilename: str | Path) -> None:
    """Returns a dictionary of shells and users.

    :param filename: Path to the file to read (str or Path-like).
    :param outfilename: Path to the output file (str or Path-like).
    :raises FileNotFoundError: If the file does not exist.
    """
    p = Path(filename)
    if not p.exists():
        print(f"Error: File '{filename}' not found.")
    s_dict = {}
    with (open(filename) as fin, open(outfilename, 'w') as fout):
        for line in fin:
            if not line.startswith(("#", "\n")):
                username, *_, shellname = line.strip().split(":")
                s_dict.setdefault(shellname, []).append(username)
        for shell, user_list in s_dict.items():
           fout.write(f"{shell}: {', '.join(user_list)}\n")

shell_users("../linux-etc-passwd.txt", "C06/linux-etc-passwd-users.txt")

from collections import defaultdict
from pathlib import Path


def shell_users_c(
    filename: str | Path,
    outfilename: str | Path,
    encoding: str = 'utf-8',
) -> None:
    """Read a passwd-style file and write shells with their users to an output file.

    Each line of the output file contains a shell path followed by a
    comma-separated list of usernames that use that shell.

    Args:
        filename: Path to the passwd-style input file.
        outfilename: Path to the output file to write.
        encoding: File encoding to use (default: utf-8).

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f"File '{filename}' not found.")

    shells: defaultdict[str, list[str]] = defaultdict(list)

    with (
        open(p, 'r', encoding=encoding) as fin,
        open(outfilename, 'w', encoding=encoding) as fout,
    ):
        for line in fin:
            if line.startswith(('#', '\n')):
                continue
            username, *_, shell = line.strip().split(':')
            shells[shell].append(username)

        for shell, users in shells.items():
            fout.write(f'{shell}: {", ".join(users)}\n')

shell_users_c("../linux-etc-passwd.txt", "C06/linux-etc-passwd-users_c.txt")

def shell_users_l(filename, outfilename):
    shells = defaultdict(list)

    with open(filename) as passwd, open(outfilename, 'w') as outfile:
        for one_line in passwd:
            if one_line.startswith(('#', '\n')):
                continue

            username, *fields, shell = one_line.strip().split(':')
            shells[shell].append(username)

        for shell, all_users in shells.items():
            outfile.write(f'{shell}\t{",".join(all_users)}\n')

shell_users_l("../linux-etc-passwd.txt", "linux-etc-passwd-users_l.txt")