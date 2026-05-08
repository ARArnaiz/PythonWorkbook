numbers = range(15)


def join_numbers(numbers: list[int]) -> str:
    return ",".join(str(n) for n in numbers)


print(join_numbers(numbers))


# 28 b1
def join_numbers_if(numbers: list[int]) -> str:
    return ",".join(str(n) for n in numbers if n <= 10)


print(join_numbers_if(numbers))

hex_numbers = [hex(n) for n in range(15)]


# 28 b2
def sumhex(numbers: list[str]) -> int:
    return sum(int(n, 16) for n in numbers)


print(sumhex(hex_numbers))

lst = ["Yo no me llamo Javier", "Deja ya de joder"]
print(lst)


# 28 3
# def reverse_wo(lst: list) -> list:
#     # return [" ".join(item.split()[::-1]) for item in lst]
#     return [" ".join(reversed(item.split())) for item in lst]

def reverse_wo(filename: str) -> list:
    """
    Reads a file and returns a list of lines with word order reversed.
    """
    with open(filename) as f:
        return [' '.join(reversed(line.split())) for line in f]

"""One improvement worth making: trailing newlines. When you read lines from a file, 
each one carries a \n at the end. After split() and ' '.join(), 
that newline disappears from the middle of the line but may affect the last token depending 
on the content. The safe habit is:

pythonreturn [' '.join(reversed(line.rstrip().split())) for line in f]

rstrip() instead of strip() — you only want to trim the right side; leading whitespace 
could be meaningful (indentation, etc.).
A second thought on the return type: returning a list eagerly reads the whole file 
nto memory. If the file is large, a generator is more appropriate:"""

def reverse_words_c(filename: str):
    with open(filename) as f:
        for line in f:
            yield ' '.join(reversed(line.rstrip().split()))

"""For your typical linguistics/NLP use case — processing a corpus line by line — 
the generator version is the more professional pattern. The tradeoff is that the 
caller can only iterate it once, so if you need to reuse the result, the list version is fine."""

def reverse_words(filename):
    return [' '.join(reversed(one_line.split()))
            for one_line in open(filename)]

print(reverse_wo("wcfile.txt"))
print(reverse_words("wcfile.txt"))
print(list(reverse_words_c("wcfile.txt")))
