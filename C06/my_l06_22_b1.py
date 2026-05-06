import csv
from pathlib import Path


def format_to_csv(inputfile: str | Path,
                  outputfile: str | Path,
                  fields: list[int] = [0, 1],
                  udelimiter: str = ','
                  ) -> object:
    p = Path(inputfile)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {inputfile}')
    with open(p) as finput, open(outputfile, "w", newline='') as foutput:
        infile = csv.reader(finput, delimiter=':')
        outfile = csv.writer(foutput, delimiter=udelimiter)
        for record in infile:
            if len(record) > 1:
                userfields = []
                try:
                    for field in fields:
                        userfields.append(record[field])
                except IndexError:
                    print(f"Field {field} is out of range, skipping row.")
                outfile.writerow(userfields)

format_to_csv("../passwd.txt", "C06/passwd.csv", [0, 2], '\t')


def passwd_to_csv(passwd_filename, csv_filename, fields_to_pass='1 2', delimiter='\t'):
    fields_to_pass = [int(one_item)
                      for one_item in fields_to_pass.split()]

    with open(passwd_filename) as passwd, open(csv_filename, 'w', newline='') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=delimiter)
        for record in infile:

            if len(record) > 1:
                fields = [one_field
                          for index, one_field in enumerate(record)
                          if index in fields_to_pass]

                outfile.writerow(fields)

passwd_to_csv("../passwd.txt", "C06/passwd_l.csv", '0 2', '\t')