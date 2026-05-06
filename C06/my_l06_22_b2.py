import csv

mydict = {'John': 35, 'Mary': 28, 'Alice': 22, 'Bob': 30, 'Anne': 'unknown'}


def process_dict_to_csv(d: dict, outputfile: str):
    with open(outputfile, "w", newline='') as foutput:
        outfile = csv.writer(foutput)
        for key, value in d.items():
            # outfile.writerow([record, value, 'int' if isinstance(value, int) else 'str'])
            outfile.writerow([key, value, type(value).__name__])


process_dict_to_csv(mydict, "mydict.csv")


def dict_to_csv(d, csv_filename, delimiter=','):
    with open(csv_filename, 'w', newline='') as output:
        outfile = csv.writer(output, delimiter=delimiter)

        for key, value in d.items():
            outfile.writerow([key, value, type(value)])


dict_to_csv(mydict, "mydict_l.csv")


def dict_to_csv_c(d: dict, csv_filename: str, delimiter: str = ',') -> None:
    """Write a dictionary to a CSV file with key, value, and type name columns."""
    with open(csv_filename, 'w', newline='') as output:
        outfile = csv.writer(output, delimiter=delimiter)
        for key, value in d.items():
            outfile.writerow([key, value, type(value).__name__])

dict_to_csv_c(mydict, "mydict_c.csv")