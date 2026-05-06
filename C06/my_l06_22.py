import csv
from pathlib import Path

def pass_to_csv(filename: str | Path) -> object:
    p = Path(filename)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {filename}')
    new_path = p.with_suffix('.csv')
    with open(p) as f, open(new_path, "w", newline='') as csvfile:
        of = csv.writer(csvfile, delimiter="\t")
        for line in f:
            if not line.startswith(("#", "\n")):
                username, _, userid, *ignore = line.strip().split(":")
                of.writerow([username, userid])

pass_to_csv("../passwd.txt")

def passwd_to_csv(passwd_filename, csv_filename):
    """Function that takes the filename of a
Unix-style passwd file to be read from, and the
name of a file that will be created and written to.
The username and user ID from the passwd file will
be written to the second file in CSV format, with
a tab separator.
"""
    with open(passwd_filename) as passwd, open(csv_filename, 'w', newline ='') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

passwd_to_csv("../passwd.txt", "C06/passwd_l.csv")
