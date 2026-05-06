import csv
import random


def my_random_csv(outputfile: str, num_of_records: int = 20, num_of_fields: int = 10) -> None:
    """Write random integers to a CSV file, then print each row's sum and mean."""
    with open(outputfile, "w", newline='') as output:
        outfile = csv.writer(output)
        for recs in range(num_of_records):
            record = [random.randint(10, 100) for _ in range(num_of_fields)]
            outfile.writerow(record)

    with open(outputfile, newline='') as input:
        reader = csv.reader(input)
        for i, row in enumerate(reader, 1):
            introw = [int(x) for x in row]
            print(f'{i}: sum={sum(introw)}, mean={sum(introw) / len(row):.2f}')


my_random_csv("nums.csv")


def random_csv_c(csv_filename: str, num_records: int = 10, num_fields: int = 10) -> None:
    """Write random integers to a CSV file, then print each row's sum and mean."""
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(num_records):
            row = [random.randint(10, 100) for _ in range(num_fields)]
            writer.writerow(row)

    with open(csv_filename, newline='') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader, 1):
            numbers = [int(x) for x in row]
            total = sum(numbers)

            print(f'{i}: sum={total}, mean={total / len(numbers):.2f}')


random_csv_c("output_c.csv")


def random_csv(csv_filename):
    with open(csv_filename, 'w', newline='') as output:
        outfile = csv.writer(output)

        for i in range(10):
            output = []
            for j in range(10):
                output.append(random.randint(10, 100))

            outfile.writerow(output)

    for one_line in open(csv_filename, newline=''):
        numbers = [int(one_item)
                   for one_item in one_line.split(',')]

        print(f'sum = {sum(numbers)}, mean = {sum(numbers) / len(numbers)}')


random_csv("output.csv")
