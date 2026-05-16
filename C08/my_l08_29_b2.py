'''
Spec:
In the United States, phone numbers have 10 digits—a three-digit area code,
followed by a seven-digit number. Several times during my childhood, area
codes would run out of phone numbers, forcing half of the population to get
a new area code. After such a split, XXX-YYY-ZZZZ might remain XXX-YYY-ZZZZ,
or it might become NNN-YYY-ZZZZ, with NNN being the new area code.
The decision regarding which numbers remained and which changed was often
made based on the phone numbers’ final seven digits. Use a list comprehension
to return a new list of strings, in which any phone number whose YYY begins
with the digits 0–5 will have its area code changed to XXX+1. For example,
given the list of strings ['123-456-7890', '123-333-4444', '123-777-8888'],
we want to convert them to ['124-456-7890', '124-333-4444','124-777-8888'].
'''
AC_TO_CHANGE = frozenset(range(6))

def adjust_area_codes(lst: list) -> list:

    return [item[:2] + str(int(item[2]) + 1) + item[3:]
            if int(item[4]) in AC_TO_CHANGE
            else item
            for item in lst]


lst = ['123-456-7890', '123-333-4444', '123-777-8888']
print(adjust_area_codes(lst))

# Claude
EXCHANGES_TO_CHANGE = frozenset(range(6))  # 0–5

def increment_area_code_c(phone: str) -> str:
    area_code, exchange, last = phone.split('-')
    if int(exchange[0]) in EXCHANGES_TO_CHANGE:
        area_code = str(int(area_code) + 1)
    return f'{area_code}-{exchange}-{last}'

def increment_all_area_codes_c(phones: list[str]) -> list[str]:
    return [increment_area_code_c(phone) for phone in phones]

print(increment_all_area_codes_c(lst))

# Lerner

def increment_area_code(full_phone_number):
    area_code, phone_number = full_phone_number.split('-', 1)

    if area_code[0] in '012345':
        area_code = str(int(area_code) + 1)

    return f'{area_code}-{phone_number}'


def increment_all_area_codes(area_codes):
    return [increment_area_code(one_phone_number)
            for one_phone_number in area_codes]


print(increment_all_area_codes(lst))
