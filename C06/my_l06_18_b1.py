def get_int_tokens_total(filename: str) -> int:
     with open(filename) as f:
        total = 0
        for line in f:
            ints = [int(i) for i in line.strip().split() if i.isdigit()]
            total += sum(ints)
        return total

print(get_int_tokens_total("../apache_logs.txt"))

def get_int_tokens_total2(filename: str) -> int:
    """Alternative implementation of get_int_tokens_total that uses a
     generator expression instead of a list comprehension. This avoids creating an intermediate
     list of integers, which can save memory if there are many integers in the file."""
    with open(filename) as f:
        total = 0
        for line in f:
            total += sum (int(i) for i in line.split() if i.isdigit())
        return total

print(get_int_tokens_total2("../apache_logs.txt"))

def sum_ints(filename):
    total = 0

    for one_line in open(filename):
        for one_word in one_line.split():
            if one_word.isdigit():
                total += int(one_word)

    return total

print(sum_ints("../apache_logs.txt"))

def get_int_tokens_total_c(filename: str) -> int:
    """Claude's alternative implementation of get_int_tokens_total that uses a
    single generator expression to sum all integers in the file in one pass. This is the most
    concise and memory-efficient approach, as it avoids creating any intermediate lists or variables."""
    with open(filename) as f:
        return sum(
            int(word)
            for line in f
            for word in line.split()
            if word.isdigit()
        )

print(get_int_tokens_total_c("../apache_logs.txt"))