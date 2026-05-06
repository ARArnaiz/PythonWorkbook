numbers = [1, 2, 3, 1, 2, 3, 4, 1]

def count_unique(lst : list) -> int:
    uq = set(lst)
    return len(uq)

print(count_unique(numbers))