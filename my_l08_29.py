import operator

words = 'this is a bunch of words'.split()
x = map(len, words)
print(sum(x))


def is_a_long_word(one_word):
    return len(one_word) > 4


x = filter(is_a_long_word, words)
print(' '.join(x))



letters = 'abcd'
numbers = range(1,5)
x = map(operator.mul, letters, numbers)
print(' '.join(x))

print(' '.join(operator.mul(one_letter, one_number)
               for one_letter, one_number in zip(letters, numbers)))


def sum_numbers(string) -> int:
    return sum(int(one_number) for one_number in string.split() if one_number.isdigit())

print(sum_numbers('10 abc 20 de44 30 55fg 40'))

# numbers = input("Enter a string of numbers space-separated: ").strip()
# print(sum_numbers(numbers))

# s = input('Enter a number: ').strip()
# if s.isdigit():
#     n = int(s)
#     print(f'You entered {n}. 2*{n} = {2*n}.')
# else:
#     print(f'{s} is not numeric.')

# s = input('Enter a number: ').strip()

# try:
#     n = int(s)
#     print(f'You entered {n}. 2*{n} = {2 * n}.')
# except ValueError:
#     print(f'{s} is not numeric.')

def sum_numbers_l (numbers):
    return sum(int(number)
                for number in numbers.split()
                if number.isdigit())

print(sum_numbers('1 2 3 a b c 4'))