from collections import defaultdict
import math

def factors(n: int) -> list[int]:
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)


def ns_fs_ms() -> dict:
    d = defaultdict(list)
    nlst = input("Enter a list of numbers separated by spaces: ").split()
    for n in nlst:
        if not n.isdigit():
            print(f'Ignoring {n}')
            continue
        n = int(n)
        for f in factors(n):
            d[f].append(n)
    return {k: sorted(v) for k, v in sorted(d.items())}

print(ns_fs_ms())


# Solution doesn't match spec:
# Ask the user to enter integers, separated by spaces. From this input,
# create a dict whose keys are the factors for each number, and the values
# are lists containing those of the users’ integers that are multiples of those factors.

def factors():
    output = defaultdict(list)

    numbers = input("Enter numbers, separated by spaces: ").split()

    for one_number in numbers:
        if not one_number.isdigit():
            print(f'Ignoring {one_number}')
            continue

        one_number = int(one_number)
        for i in range(1, one_number):
            if not one_number % i:
                output[one_number].append(i)

        output[one_number].append(one_number)

    return output

print(factors())